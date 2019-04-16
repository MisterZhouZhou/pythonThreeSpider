import requests
from douyinspider.utils.downloaderUtil import downloadBillboard, downloadCategory, downloadFavorite, downloadPost
from douyinspider.hot import hotSearchWord,getVideoOfHotSearchWord
from douyinspider.structures import Word,Video
from douyinspider.person import favorite,post

from douyinspider.utils import fetch
from douyinspider.url.urls import URL
from douyinspider.config import person_post_headers
from douyinspider.hot import hotSearchWord

# 递归获取所有的提交视频
def get_aweme_list():
    user_video_list = []
    url = 'https://api.amemv.com/aweme/v1/challenge/aweme/?cursor=10&ch_id=1628348168113166&count=20'

    while True:
        result = fetch(url, headers=person_post_headers, verify=False)
        print(result)
        aweme_list = result.get('aweme_list', [])
        if aweme_list != None and len(aweme_list)!=0:
            user_video_list.extend(aweme_list)
        if result.get('has_more') != 1:
            break
    return user_video_list

if __name__ == '__main__':
   hots = hotSearchWord()
   print(hots)
    # 下载陈赫喜欢的视频
    # downloadFavorite(84990209480, '陈赫')
    # 下载陈赫上传的视频
    # downloadPost(84990209480, '陈赫')



    # getVideoOfHotSearchWord('巴黎圣母院大火')
    # downloadCategory()
    # for word in hotSearchWord():
    #     if isinstance(word, Word):
    #         print(word.word)

    # response = requests.get(URL.billboard(), headers=common_headers).json()
    # print(response)
