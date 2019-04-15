from douyinspider.utils import fetch
from douyinspider.url.urls import URL
from douyinspider.config import common_headers
from douyinspider.utils.common import parse_datetime
from douyinspider.utils.tranform import data_to_music, data_to_topic

# define trend query params
query = {
    'version_code': '2.9.1',
    'count': '10',
}


'''
 name: 获取分类
 maxCursor: 最大拉取偏移量
'''
def category(maxCursor=50):
    """
    get trend result
    :return:
    """
    offset = 0
    # 单个例子测试
    # query['cursor'] = str(offset)
    # result = fetch(URL.category_list(), headers=common_headers, params=query, verify=False)
    # category_list = result.get('category_list')
    # datetime = parse_datetime(result.get('extra', {}).get('now'))
    # final = []
    # for item in category_list:
    #     # process per category
    #     if item.get('desc') == '热门话题':
    #         print('===热门话题')
    #         final.append(data_to_topic(item))
    #     if item.get('desc') == '热门音乐':
    #         print('===热门音乐')
    #         final.append(data_to_music(item.get('music_info', {})))
    # return final

    # 获取所有的
    while True:
        query['cursor'] = str(offset)
        result = fetch(URL.category_list(), headers=common_headers, params=query, verify=False)
        category_list = result.get('category_list')
        datetime = parse_datetime(result.get('extra', {}).get('now'))
        final = []
        for item in category_list:
            # process per category
            if item.get('desc') == '热门话题':
                final.append(data_to_topic(item))
            if item.get('desc') == '热门音乐':
                final.append(data_to_music(item.get('music_info', {})))
        if result.get('has_more') != 1:
            break
        else:
            if offset > maxCursor: # 不想拉取很多可以设置这个参数
                break
            offset += 10
    return final