from douyinspider.utils import fetch
from douyinspider.url.urls import URL
from douyinspider.config import common_headers
from douyinspider.utils.tranform import data_to_word
import urllib

# 获取热门关键词
def hotSearchWord():
    result = fetch(URL.hot_search_word(), headers=common_headers, verify=False)
    word_list = result.get('data').get('word_list')
    words = []
    for item in word_list:
        # 热门词
        word = data_to_word(item)
        words.append(word)
    return words

def getVideoOfHotSearchWord(key):
    # 编译关键词
    key = urllib.parse.quote(key)
    # 拼接关键词搜索接口url
    url = 'https://api.amemv.com/aweme/v1/general/search/single/?keyword=' + key + '&offset=0&count=10&is_pull_refresh=0&hot_search=0&latitude=30.725991&longitude=103.968091&ts=1543984658&js_sdk_version=1.2.2&app_type=normal&manifest_version_code=350&_rticket=1543984657736&ac=wifi&device_id=60155513971&iid=53112482656&os_version=8.0.0&channel=xiaomi&version_code=350&device_type=MI%205&language=zh&uuid=862258031596696&resolution=1080*1920&openudid=8aa8e21fca47053b&update_version_code=3502&app_name=aweme&version_name=3.5.0&os_api=26&device_brand=Xiaomi&ssmix=a&device_platform=android&dpi=480&aid=1128&as=a1e5055072614ce6a74033&cp=5813c65d2e7d0769e1[eIi&mas=01327dcd31044d72007555ed00c3de0b5dcccc0c2cec866ca6c62c'
    print(url)
