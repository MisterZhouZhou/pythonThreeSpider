from douyinspider.utils import fetch
from douyinspider.url.urls import URL
from douyinspider.config import person_post_headers
from douyinspider.utils.tranform import data_to_video
import requests
import re

# 获取用户签名
def getSignatureParams(user_id):
    import subprocess
    signature = subprocess.getoutput('node signature.js %s' % user_id)
    url = "https://www.iesdouyin.com/share/user/{}".format(user_id)
    # 获得dytk
    reponse = requests.get(url, headers=person_post_headers)
    reponse.encoding = 'utf-8'
    dytk = re.search("dytk: '(.*?)'", reponse.text).group(1)
    queryParams = {
        'user_id': str(user_id),
        'count': '21',
        'max_cursor': '0',
        'aid': '1128',
        '_signature': signature,
        'dytk': dytk
    }
    return queryParams


# 递归获取所有的提交视频
def get_aweme_list(queryParams):
    user_video_list = []
    max_cursor = 0
    while True:
        if max_cursor:
            queryParams['max_cursor'] = str(max_cursor)
        result = fetch(URL.person_post_url(), headers=person_post_headers, params=queryParams, verify=False)
        print(result)
        aweme_list = result.get('aweme_list', [])
        if aweme_list != None and len(aweme_list)!=0:
            user_video_list.extend(aweme_list)
        if result.get('has_more') != 1:
            break
        else:
            max_cursor = result.get('max_cursor')
    return user_video_list

# 获取用户提交的视频
def post(user_id, user_name):
    print("正在拉取", user_name if user_name else user_id, '提交的抖音视频...')
    queryParams = getSignatureParams(user_id)
    user_video_list = get_aweme_list(queryParams)
    print(user_name if user_name else user_id, '喜欢的抖音视频拉取完成')
    videos = []
    for item in user_video_list:
        video = data_to_video(item)
        videos.append(video)
    return videos
