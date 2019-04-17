import requests
from douyinspider.utils.downloaderUtil import downloadBillboard, downloadCategory, downloadFavorite, downloadPost, downloadMusicCollection
from douyinspider.hot import hotSearchWord,getVideoOfHotSearchWord
from douyinspider.structures import Word,Video,MusicCollection,Music
from douyinspider.person import favorite,post, person
from douyinspider.music import music_collection

from douyinspider.utils import fetch
from douyinspider.url.urls import URL
from douyinspider.config import person_post_headers
from douyinspider.hot import hotSearchWord
from douyinspider.config import common_headers

# 递归获取所有的提交视频
def get_aweme_list():
    user_video_list = []
    url='https://aweme.snssdk.com/aweme/v1/challenge/aweme/?iid=30373511894&device_id=35781128184&os_api=18&app_name=aweme&channel=App%20Store&idfa=811A8841-030F-4AEA-B934-C2A56489C32D&device_platform=iphone&build_number=17805&vid=A4BB3AF4-7981-4805-995B-78419881DC11&openudid=99bf2b608173e21cefd562496d2cf21fa8eba580&device_type=iPhone7,2&app_version=1.7.8&version_code=1.7.8&os_version=11.3&screen_width=750&aid=1128&ac=WIFI&ch_id=1574030716416014&count=21&cursor=0&pull_type=2&query_type=0&type=5&mas=001469ed4a7a3f61de046e21c8c7ae8bcb64a983471da18ec0c8d1&as=a1c5206d9e676a38ee4960&ts=1524500606'
    offset, count = 0, 0
    while True:
        # define cursor
        result = fetch(url, headers=person_post_headers, verify=False)
        print(result)
        if result.get('has_more') != 1:
            break


if __name__ == '__main__':
    get_aweme_list()


    # for musicCollection in music_collection():
    #     if isinstance(musicCollection, MusicCollection):
    #         print(musicCollection.mc_name)
    #         musics = musicCollection.mc_musics if musicCollection.mc_musics else []
    #         for music in musics:
    #             if isinstance(music, Music):
    #                print(music.name,'===',music.play_url)

    # get_aweme_list()
    # downloadCategory()
    # 拉取抖音用户列表
    # person()
    # 下载陈赫喜欢的视频
    # downloadFavorite(84990209480, '陈赫')
    # 下载陈赫上传的视频
    # downloadPost(84990209480, '陈赫')
    # downloadPost(88445518961, 'Dear-迪丽热巴')



    # getVideoOfHotSearchWord('巴黎圣母院大火')
    # downloadCategory()
    # for word in hotSearchWord():
    #     if isinstance(word, Word):
    #         print(word.word)

    # response = requests.get(URL.billboard(), headers=common_headers).json()
    # print(response)
