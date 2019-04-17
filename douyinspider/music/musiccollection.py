# -*- coding:utf-8 -*-
from douyinspider.utils import fetch
from douyinspider.url.urls import URL
from douyinspider.config import common_headers
from douyinspider.utils.tranform import data_collection_to_music
from douyinspider.structures import MusicCollection

# from contextlib import closing
# import requests, json, time, re, os, sys, time
#
#
# class douyin(object):
#     """docstring for douyin"""
#
#     def __init__(self):
#         super(douyin, self).__init__()
#         self.headers = {
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#             'accept-encoding': 'gzip, deflate, br',
#             'accept-language': 'zh-CN,zh;q=0.9',
#             'cache-control': 'max-age=0',
#             'upgrade-insecure-requests': '1',
#             'user-agent': 'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; MI 4S Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.1.3',
#         }
#
#     def get_music_urls(self, mc_id):
#         music_names = []
#         music_urls = []
#         user_url = 'https://api.amemv.com/aweme/v1/music/list/?iid=34451996099&device_id=52982221132&os_api=18&app_name=aweme&channel=App%20Store&idfa=00000000-0000-0000-0000-000000000000&device_platform=iphone&build_number=18504&vid=386F3505-7B99-444A-845A-E5EEA12C5936&openudid=e01e26ddeb822fd95f6599de43b7547cfe1a26ea&device_type=iPhone7,2&app_version=1.8.5&version_code=1.8.5&os_version=11.3&screen_width=750&aid=1128&ac=WIFI&cursor=0&mc_id=' + str(
#             mc_id)
#         req = requests.get(user_url, headers=self.headers)
#         html = json.loads(req.text)
#         for each in html['music_list']:
#             share_desc = each['title']
#             music_names.append(share_desc + '.mp3')
#             music_urls.append(each['play_url']['uri'])
#         return music_names, music_urls
#
#     def music_downloader(self, music_url, music_name):
#         """
#         下载
#         """
#         size = 0
#         with closing(requests.get(music_url, headers=self.headers, stream=True)) as response:
#             chunk_size = 1024
#             content_size = int(response.headers['content-length'])
#             if response.status_code == 200:
#                 sys.stdout.write('  [文件大小]:%0.2f MB\n' % (content_size / chunk_size / 1024))
#                 with open(music_name, "wb") as file:
#                     for data in response.iter_content(chunk_size=chunk_size):
#                         file.write(data)
#                         size += len(data)
#                         file.flush()
#                         sys.stdout.write('  [下载进度]:%.2f%%' % float(size / content_size * 100) + '\r')
#                         sys.stdout.flush()
#
#     def run(self):
#         """
#         运行函数
#         Parameters:
#             None
#         Returns:
#             None
#         """
#         mc_id = 0
#
#         collection = requests.get(music_collection_url(), headers=self.headers)
#         js_collection = json.loads(collection.text)
#         for mc in js_collection['mc_list']:
#             mc_id = mc['id']
#             mc_name = mc['mc_name']
#             music_names, music_urls = self.get_music_urls(mc_id)
#             # print(mc_name)
#             if mc_name not in os.listdir('/Users/admin/Desktop/'):
#                 os.mkdir(mc_name)
#             print('下载中:共有%d个作品!\n' % len(music_urls))
#             for num in range(len(music_urls)):
#                 if '\\' in music_names[num]:
#                     music_name = music_names[num].replace('\\', '')
#                 elif '/' in music_names[num]:
#                     music_name = music_names[num].replace('/', '')
#                 else:
#                     music_name = music_names[num]
#                 if os.path.isfile(os.path.join(mc_name, music_name)):
#                     print('%s 已存在' % mc_name)
#                 else:
#                     self.music_downloader(music_urls[num], os.path.join(mc_name, music_name))
#                 print('\n')
#         print('下载完成!')


def get_music_urls(mc_id):
    musics = []
    result = fetch(URL.music_collection_list(mc_id), headers=common_headers, verify=False)
    music_list = result.get('music_list', [])
    for item in music_list:
         music = data_collection_to_music(item)
         musics.append(music)
    return musics



# 获取音乐榜数据
def music_collection():
    result = fetch(URL.music_collection_url(), headers=common_headers, verify=False)
    mc_list = result.get('mc_list', [])
    collection_list = []
    for mc in mc_list:
        mc_id = mc['id']
        mc_name = mc['mc_name']
        print('正在拉取', mc_name, '...')
        mc_musics = get_music_urls(mc_id)
        musicCollection = MusicCollection(
            mc_id=mc_id,
            mc_name=mc_name,
            mc_musics=mc_musics
        ) if id else None
        collection_list.append(musicCollection)
        print(mc_name, '拉取完毕')
    return collection_list