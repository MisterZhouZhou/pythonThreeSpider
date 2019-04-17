import requests
from retrying import retry
from douyinspider.config import retry_max_number, retry_min_random_wait, retry_max_random_wait, fetch_timeout

# 需要多次重试请求，这种情况下，如果想优雅的实现功能，可以使用retrying
'''
    在@retry()装饰器中，比较重要的几个参数如下：
    stop_max_attempt_number：在停止之前尝试的最大次数，最后一次如果还是有异常则会抛出异常，停止运行，默认为5次
    wait_random_min：在两次调用方法停留时长，停留最短时间，默认为0,单位毫秒
    wait_random_max：在两次调用方法停留时长，停留最长时间，默认为1000毫秒
    retry_on_result：指定一个函数，如果指定的函数返回True，则重试，否则抛出异常退出
    retry_on_exception: 指定一个函数，如果此函数返回指定异常，则会重试，如果不是指定的异常则会退出
'''


#  指定一个函数，如果此函数返回指定异常，则会重试，如果不是指定的异常则会退出
def need_retry(exception):
    """
    need to retry
    :param exception:
    :return:
    """
    result = isinstance(exception, (requests.ConnectionError, requests.ReadTimeout))
    if result:
        print('Exception', type(exception), 'occurred, retrying...')
    return result

# 网络请求
def fetch(url, **kwargs):
    @retry(stop_max_attempt_number=retry_max_number, wait_random_min=retry_min_random_wait,
           wait_random_max=retry_max_random_wait, retry_on_exception=need_retry)
    def _fetch(url, **kwargs):
        """
        fetch api response
        :param url: fetch url
        :param kwargs: other requests params
        :return: json of response
        """
        print(kwargs)
        kwargs.update({'verify': False})
        kwargs.update({'timeout': fetch_timeout})
        response = requests.get(url, **kwargs)
        if response.status_code != 200:
            raise requests.ConnectionError('Expected status code 200, but got {}'.format(response.status_code))
        return response.json()

    try:
        result = _fetch(url, **kwargs)
        return result
    # give up retrying
    except (requests.ConnectionError, requests.ReadTimeout):
        return {}
