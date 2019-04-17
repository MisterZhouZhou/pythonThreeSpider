from douyinspider.utils import fetch
from douyinspider.url.urls import URL
from douyinspider.config import common_headers,person_post_headers
from douyinspider.utils.tranform import data_to_video, data_Anoyi_to_user
import requests
from bs4 import BeautifulSoup
import os
import json

def save_txt(filePath, persons):
    with open(filePath, 'w') as f:
        json.dump(persons, f)

# 获取用户提交的视频
def person():
    print("正在拉取抖音用户列表信息...")
    reponse = requests.get(URL.person_list_url(), headers=common_headers, verify=False)
    print("抖音用户列表信息拉取完毕")
    soup = BeautifulSoup(reponse.text, 'html.parser')
    # 获取昵称
    persons = soup.find_all('div', class_="card-body")
    person_path = os.getcwd() + "/doc/抖音用户.txt"
    if os.path.exists(person_path):
        with open(person_path, 'r') as f:
            person_list = json.loads(f.read())
        print(person_list)
    else:
        person_list = []
        for person in persons:
            person_id = person.find('a').get('href')
            person_id = person_id[4:]
            person_name = person.find('a').string
            person_list.append({"id": person_id, "name": person_name})
        print(person_list)
        save_txt(person_path, person_list)
