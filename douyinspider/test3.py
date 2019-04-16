import requests

user_id = '58841646784' # 6556303280


# 获取小姐姐的所有作品
"""
 signature = _bytedAcrawler.sign('用户ID')
 douyin_falcon:node_modules/byted-acrawler/dist/runtime
"""
import subprocess
signature = subprocess.getoutput('node signature.js %s' % user_id)

user_video_list = []

# ############################# 获取个人作品 ##########################
user_video_params = {
    'user_id': str(user_id),
    'count': '21',
    'max_cursor': '0',
    'aid': '1128',
    '_signature': signature,
    'dytk': 'b4dceed99803a04a1c4395ffc81f3dbc' # '114f1984d1917343ccfb14d94e7ce5f5'
}

# 递归获取所有的提交视频
def get_aweme_list(max_cursor=None):
    if max_cursor:
        user_video_params['max_cursor'] = str(max_cursor)
    res = requests.get(
        url="https://www.douyin.com/aweme/v1/aweme/post/",
        params=user_video_params,
        headers={
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'x-requested-with':'XMLHttpRequest',
            'referer':'https://www.douyin.com/share/user/58841646784',
        }
    )
    content_json = res.json()
    aweme_list = content_json.get('aweme_list', [])
    user_video_list.extend(aweme_list)
    #  拉取所有用户提交的视频
    if content_json.get('has_more') == 1:
        return get_aweme_list(content_json.get('max_cursor'))


get_aweme_list()
print(user_video_list)

#
# # ############################# 获取喜欢作品 ##########################
#
#
# favor_video_list = []
#
# favor_video_params = {
#     'user_id': str(user_id),
#     'count': '21',
#     'max_cursor': '0',
#     'aid': '1128',
#     '_signature': signature,
#     'dytk': 'b4dceed99803a04a1c4395ffc81f3dbc'
# }
#
#
# def get_favor_list(max_cursor=None):
#     if max_cursor:
#         favor_video_params['max_cursor'] = str(max_cursor)
#     res = requests.get(
#         url="https://www.douyin.com/aweme/v1/aweme/favorite/",
#         params=favor_video_params,
#         headers={
#             'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#             'x-requested-with':'XMLHttpRequest',
#             'referer':'https://www.douyin.com/share/user/58841646784',
#         }
#     )
#     content_json = res.json()
#     aweme_list = content_json.get('aweme_list', [])
#     favor_video_list.extend(aweme_list)
#     if content_json.get('has_more') == 1:
#         return get_favor_list(content_json.get('max_cursor'))
#
#
# get_favor_list()
#
#
# # ############################# 视频下载 ##########################
# for item in user_video_list:
#     video_id = item['video']['play_addr']['uri']
#
#     video = requests.get(
#         url='https://aweme.snssdk.com/aweme/v1/playwm/',
#         params={
#             'video_id':video_id
#         },
#         headers={
#             'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#             'x-requested-with': 'XMLHttpRequest',
#             'referer': 'https://www.douyin.com/share/user/58841646784',
#         },
#         stream=True
#     )
#     file_name = video_id + '.mp4'
#     with open(file_name,'wb') as f:
#         for line in video.iter_content():
#             f.write(line)
#
#
# for item in favor_video_list:
#     video_id = item['video']['play_addr']['uri']
#
#     video = requests.get(
#         url='https://aweme.snssdk.com/aweme/v1/playwm/',
#         params={
#             'video_id':video_id
#         },
#         headers={
#             'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#             'x-requested-with': 'XMLHttpRequest',
#             'referer': 'https://www.douyin.com/share/user/58841646784',
#         },
#         stream=True
#     )
#     file_name = video_id + '.mp4'
#     with open(file_name, 'wb') as f:
#         for line in video.iter_content():
#             f.write(line)
