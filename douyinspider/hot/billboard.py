from douyinspider.utils import fetch
from douyinspider.url.urls import URL
from douyinspider.config import common_headers
from douyinspider.utils.tranform import data_to_video

# 获取广告信息
def billboard():
    result = fetch(URL.billboard(),headers=common_headers, verify=False)
    aweme_list = result.get('aweme_list')
    videos = []
    for item in aweme_list:
        # 视频列表有4个视频地址，前两个web可以打开，后面两个只能用手机或者模拟器打开
        video = data_to_video(item.get('aweme_info', {}))
        videos.append(video)
    return videos