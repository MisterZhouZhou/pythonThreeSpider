from douyinspider.url.urls import URL
from selenium import webdriver
import requests
import json
import copy
import re
import urllib
import time
import os
from bs4 import BeautifulSoup

# 失败

def getParams(user_id):
    url="https://www.iesdouyin.com/share/user/{}".format(user_id)
    headers={'user-agent': 'Aweme 3.1.0 rv:31006 (iPhone; iOS 12.0; zh_CN) Cronet'}
    # 获得dytk
    reponse = requests.get(url,headers=headers)
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
    userInfo = {}
    # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
    soup = BeautifulSoup(reponse.text, 'html.parser')
    # 获取昵称
    nickname = soup.find('p', class_="nickname").string
    location = soup.find('span', class_="location").string
    # videos = soup.find('li', class_="item goWork").string
    userInfo['nickname'] = nickname
    userInfo['location'] = location
    # userInfo['videos'] = videos
    return headers,params,userInfo


def getParams2(user_id):
    url="https://www.douyinspider.com/share/user/{}".format(user_id)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url)
    nickname = driver.find_element_by_class_name("nickname").text
    location = driver.find_element_by_class_name("location").text
    video_list = driver.find_elements_by_css_selector("li[data-type=\"video\"]")
    videos_info = []
    user_info = {}
    for i in range(len(video_list)):
        video_id = video_list[i].get_attribute('data-id')
        video_url = 'https://www.iesdouyin.com/share/video/{}/?u_code=hjdm8k44&region=CN&mid=6610679524466101005&schema_type=1&object_id=6610679501925911815&utm_campaign=client_scan_share&app=aweme&utm_medium=ios&tt_from=scan_share&iid=45561030398&utm_source=scan_share'.format(video_id)
        videos_info.append(video_url)
    user_info['nickname'] = nickname
    user_info['location'] = location
    user_info['videos'] = videos_info
    return user_info

def download_video(path, url):
    t_url = 'https://www.iesdouyin.com/share/video/6678155284059327747/?u_code=hjdm8k44&region=CN&mid=6610679524466101005&schema_type=1&object_id=6610679501925911815&utm_campaign=client_scan_share&app=aweme&utm_medium=ios&tt_from=scan_share&iid=45561030398&utm_source=scan_share'
    res = requests.get(t_url)
    print(res)
    # try:
    #     print("正在下载：{0}".format(url))
    #     # 通过urllib.request.urlretrieve进行下载歌曲
    #     urllib.request.urlretrieve(url, '{0}/{1}.mp4'.format(path, time.time()))
    #     print("Finish...")
    # except:
    #     print("Failed...")


def get_favor_video(headers, params):
    while True:
        # 请求数据
        furl = "https://www.iesdouyin.com/aweme/v1/aweme/favorite/"
        jsonstr = requests.get(furl, params=params, headers=headers).json()
        # 多次请求会出现正确数据
        #修改全局变量的值
        aweme_list = jsonstr.get('aweme_list')
        print(jsonstr)
        if aweme_list != None and len(aweme_list)!=0:
            break
    for item in aweme_list:
        video_uri = item.get('video').get('play_addr')['uri']
    return aweme_list

if __name__ == '__main__':
    # headers, params,userInfo = getParams(86371592618)
    # get_favor_video(headers, params)
    url='https://www.iesdouyin.com/aweme/v1/aweme/favorite/?user_id=86371592618&count=21&max_cursor=0&aid=1128&_signature=fBZqMxAcIH.WOSqz4s5eTHwWai&dytk=6849c66ff2a629554679fe#e4ad1343a5'
    # 有加载更多
    # furl = 'https://aweme.snssdk.com/aweme/v1/challenge/aweme/?iid=30373511894&device_id=35781128184&os_api=18&app_name=aweme&channel=App%20Store&idfa=811A8841-030F-4AEA-B934-C2A56489C32D&device_platform=iphone&build_number=17805&vid=A4BB3AF4-7981-4805-995B-78419881DC11&openudid=99bf2b608173e21cefd562496d2cf21fa8eba580&device_type=iPhone7,2&app_version=1.7.8&version_code=1.7.8&os_version=11.3&screen_width=750&aid=1128&ac=WIFI&ch_id=1574030716416014&count=21&cursor=0&pull_type=2&query_type=0&type=5&mas=001469ed4a7a3f61de046e21c8c7ae8bcb64a983471da18ec0c8d1&as=a1c5206d9e676a38ee4960&ts=1524500606%E4%BD%9C%E8%80%85%EF%BC%9A%E5%B0%8F%E6%80%AA%E8%81%8A%E8%81%8C%E5%9C%BA%E9%93%BE%E6%8E%A5%EF%BC%9Ahttps://www.jianshu.com/p/a237694e7674%E6%9D%A5%E6%BA%90%EF%BC%9A%E7%AE%80%E4%B9%A6%E7%AE%80%E4%B9%A6%E8%91%97%E4%BD%9C%E6%9D%83%E5%BD%92%E4%BD%9C%E8%80%85%E6%89%80%E6%9C%89%EF%BC%8C%E4%BB%BB%E4%BD%95%E5%BD%A2%E5%BC%8F%E7%9A%84%E8%BD%AC%E8%BD%BD%E9%83%BD%E8%AF%B7%E8%81%94%E7%B3%BB%E4%BD%9C%E8%80%85%E8%8E%B7%E5%BE%97%E6%8E%88%E6%9D%83%E5%B9%B6%E6%B3%A8%E6%98%8E%E5%87%BA%E5%A4%84%E3%80%82'
    while True:
        # 请求数据
        furl = "https://www.iesdouyin.com/aweme/v1/aweme/favorite/"
        headers = {'user-agent': 'Aweme 3.1.0 rv:31006 (iPhone; iOS 12.0; zh_CN) Cronet'}
        jsonstr = requests.get(url, headers=headers).json()
        aweme_list = jsonstr.get('aweme_list')
        print(jsonstr)
        if aweme_list != None and len(aweme_list)!=0:
            break
    print(aweme_list)



    # user_info = getParams2(93515402600)
    # path = os.getcwd() + "/data/{0}".format('video')
    # # 调用os模块判断是否存在
    # if not os.path.exists(path):
    #     os.makedirs(path)

    # # 获取可以播放的地址
    # for video_url in user_info['videos']:
    #    print(video_url)

