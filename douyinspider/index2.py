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
    url="https://www.douyinspider.com/share/user/{}".format(user_id)
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
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
    print(soup)
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
    # 请求数据
    furl = "https://www.douyinspider.com/aweme/v1/aweme/favorite/"
    jsonstr = requests.get(furl, params=params, headers=headers).json()
    # 多次请求会出现正确数据
    # aweme_list = jsonstr.get('aweme_list')
    print(jsonstr)
    # if aweme_list != None and len(aweme_list) != 0:
    #     break

if __name__ == '__main__':
    # headers, params, userInfo = getParams(93515402600)
    # print(userInfo)

    user_info = getParams2(93515402600)
    # path = os.getcwd() + "/data/{0}".format('video')
    # # 调用os模块判断是否存在
    # if not os.path.exists(path):
    #     os.makedirs(path)

    # 获取可以播放的地址
    for video_url in user_info['videos']:
       print(video_url)

