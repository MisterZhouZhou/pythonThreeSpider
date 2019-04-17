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
    url='https://api.amemv.com/aweme/v1/music/aweme/'
    query = {
        'device_id': '33333333',
        'music_id': 'bed600035a486a062310',
        'count': '18',
    }
    offset, count = 0, 0
    while True:
        # define cursor
        query['cursor'] = str(offset)
        result = fetch(URL.music2video_url(), params=query, headers=common_headers, verify=False)
        print(result)
        if result.get('has_more') != 1:
            break


if __name__ == '__main__':

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
    person()
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
