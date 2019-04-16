from douyinspider.utils import fetch
from douyinspider.url.urls import URL
from douyinspider.config import common_headers
from douyinspider.utils.tranform import data_to_video
import requests
import re

# 获取dytk及参数
def getParams(user_id):
    url="https://www.iesdouyin.com/share/user/{}".format(user_id)
    # 获得dytk
    reponse = requests.get(url,headers=common_headers)
    reponse.encoding='utf-8'
    dytk= re.search("dytk: '(.*?)'",reponse.text).group(1)
    # 组装数据
    params={
        'user_id': user_id,
        'count':'21',
        'max_cursor': '0',
        'aid': 1128,
        'dytk': dytk
    }
    return params


# 获取个人账号喜欢的视频数据
def favorite(user_id, user_name=None):
    print("正在拉取", user_name if user_name else user_id, '喜欢的抖音视频...')
    # 组装数据
    params = getParams(user_id)
    favorite_video_list = []
    max_cursor = None
    while True:
        if max_cursor:
            params['max_cursor'] = str(max_cursor)
        # 请求数据
        result = fetch(URL.favorite_url(), headers=common_headers, params=params, verify=False)
        #修改全局变量的值
        aweme_list = result.get('aweme_list')
        if aweme_list != None and len(aweme_list)!=0:
            favorite_video_list.extend(aweme_list)
        if result.get('has_more') != 1:
            break
        else:
            max_cursor = result.get('max_cursor')
    print(user_name if user_name else user_id, '喜欢的抖音视频拉取完成')
    videos=[]
    for item in favorite_video_list:
        video = data_to_video(item)
        videos.append(video)
    return videos