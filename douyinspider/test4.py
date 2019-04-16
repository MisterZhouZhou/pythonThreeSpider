import time
import requests
def main():
    '''
    入口函数
    :return:
    '''
    ts = str(time.time())
    # 入口url（热门列表url）
    url = 'https://aweme.snssdk.com/aweme/v1/hot/search/list/?detail_list=0&ts=' + ts + '&js_sdk_version=1.2.2&app_type=normal&manifest_version_code=350&_rticket=1543976807872&ac=wifi&device_id=60155513971&iid=53112482656&os_version=8.0.0&channel=xiaomi&version_code=350&device_type=MI%205&language=zh&resolution=1080*1920&openudid=8aa8e21fca47053b&update_version_code=3502&app_name=aweme&version_name=3.5.0&os_api=26&device_brand=Xiaomi&ssmix=a&device_platform=android&dpi=480&aid=1128&as=a1c56320b7f6ccc7874900&cp=3d63c15f7576037de1_uMy&mas=01258b5acd59f6bccb58178086286fdded0c0c9c2cec1cecc6c6c6'
    # 获取热门列表数据
    res = requests.get(url).content
    print(res)

if __name__ == '__main__' :
    main()