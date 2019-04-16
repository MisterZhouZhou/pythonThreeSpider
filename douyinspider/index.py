import requests
import urllib
import time
import re

# 获取组装参数
# 93515402600 86371592618
def getParams(user_id):
    url="https://www.iesdouyin.com/share/user/{}".format(user_id)
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
        'aid': '1128',
        'dytk': dytk
    }
    return headers,params



def get_favor_video(headers, params):
    while True:
        # 请求数据
        furl = "https://www.iesdouyin.com/aweme/v1/aweme/favorite/"
        jsonstr = requests.get(furl, params=params, headers=headers).json()
        # 多次请求会出现正确数据
        #修改全局变量的值
        aweme_list = jsonstr.get('aweme_list')
        if aweme_list != None and len(aweme_list)!=0:
            break
    return aweme_list


# 拼接视频地址
def getVideoListInfo(aweme_list):
    for item in aweme_list:
        # 读取视频uri
        video_uri=item['video']['play_addr']['uri']
        #拼接视频地址
        video="https://aweme.snssdk.com/aweme/v1/playwm/?video_id="+video_uri
        #下载视频
        #读取视频名称
        title=item['share_info']['share_desc']
        #写入视频
        mp4=requests.get(video,headers=headers,stream=True).content
        print('===',title,'.mp4')

if __name__ == "__main__":
    headers,params = getParams(75984155221)
    # 获取喜欢的视频
    aweme_list = get_favor_video(headers,params)
    print('========\n')
    print(aweme_list)

# def get_url(url):
#     headers = {'user-agent': 'mobile'}
#     req = requests.get(url, headers=headers, verify=False)
#     data = req.json()
#     print(data)
#     for data in data['aweme_list']:
#         name = data['desc'] or data['aweme_id']
#         url = data['video']['play_addr']['url_list'][0]
#         urllib.request.urlretrieve(url, filename=name + '.mp4')
#
#
# if __name__ == "__main__":
#     get_url('https://api.amemv.com/aweme/v1/aweme/post/?max_cursor=0&user_id=98934041906&count=20&retry_type=no_retry&mcc_mnc=46000&iid=58372527161&device_id=56750203474&ac=wifi&channel=huawei&aid=1128&app_name=aweme&version_code=421&version_name=4.2.1&device_platform=android&ssmix=a&device_type=STF-AL10&device_brand=HONOR&language=zh&os_api=26&os_version=8.0.0&uuid=866089034995361&openudid=008c22ca20dd0de5&manifest_version_code=421&resolution=1080*1920&dpi=480&update_version_code=4212&_rticket=1548080824056&ts=1548080822&js_sdk_version=1.6.4&as=a1b51dc4069b2cc6252833&cp=dab7ca5f68594861e1[wIa&mas=014a70c81a9db218501e1433b04c38963ccccc1c4cac4c6cc6c64c')

# video1
# https://www.iesdouyin.com/share/video/6610679501925911815/?u_code=hjdm8k44&region=CN&mid=6610679524466101005&schema_type=1&object_id=6610679501925911815&utm_campaign=client_scan_share&app=aweme&utm_medium=ios&tt_from=scan_share&iid=45561030398&utm_source=scan_share

# http://v6-dy.ixigua.com/ea389b2147bf58c8e9c13e91e79258da/5cb2a8f0/video/m/2202435cd9139274d14a309e5c527d612371161c5ecb00001d6ada3cfc16/?rc=MzY7cXFwdjNkbDMzPGkzM0ApQHRAbzozOTg0ODozNDY7Mzc3PDNAKXUpQGczdylAZmh1eXExZnNoaGRmOzRAc2hnaGIwMmpoXy0tMC0wc3MtbyNvI0M0LTYzLS8tLTAvLi4tLi9pOmItbyM6YDBvI3BiZnJoXitqdDojLy5e&version_code=5.7.0&pass-region=1&pass-route=1&js_sdk_version=1.13.0.0&app_name=aweme&vid=137ED526-308B-484E-B593-B14E61FAFDE1&app_version=5.7.0&device_id=59637246415&channel=App%20Store&mcc_mnc=46000&aid=1128&screen_width=1242&openudid=770220518fd3c5914450ced05b12893b6126ff7e&os_api=18&ac=WIFI&os_version=11.4&device_platform=iphone&build_number=57010&device_type=iPhone8%2C2&iid=68446596697&idfa=CD7CBDBB-ECEB-47BA-8726-CA29C90A6DE5
# http://v6-dy.ixigua.com/6275994ee35e6961c52687ff4da6c3be/5cb2a8ef/video/m/220c353e8bb206d4af6bcafe93f36b8d53d1161c49ce00002c5c2ca30109/?rc=amtxODNnOGxkbDMzN2kzM0ApQHRAbzozOTg0ODozNDY7Mzc3PDNAKXUpQGczdylAZmh1eXExZnNoaGRmOzRAZmpvcS42M2JoXy0tYC0wc3MtbyNvI0M0LTYzLS8tLTAvLi4tLi9pOmItbyM6YDBvI3BiZnJoXitqdDojLy5e&version_code=5.7.0&pass-region=1&pass-route=1&js_sdk_version=1.13.0.0&app_name=aweme&vid=137ED526-308B-484E-B593-B14E61FAFDE1&app_version=5.7.0&device_id=59637246415&channel=App%20Store&mcc_mnc=46000&aid=1128&screen_width=1242&openudid=770220518fd3c5914450ced05b12893b6126ff7e&os_api=18&ac=WIFI&os_version=11.4&device_platform=iphone&build_number=57010&device_type=iPhone8%2C2&iid=68446596697&idfa=CD7CBDBB-ECEB-47BA-8726-CA29C90A6DE5
# http://v6-dy.ixigua.com/e02373242f2ec5970da9d3ae2e8ad888/5cb2a8ed/video/m/220e26dea7de0db41b5857b22639a8573411161c468e000031a9e10581b7/?rc=M3ZoPHV1bXVkbDMzOmkzM0ApQHRAbzozOTg0ODozNDY7Mzc3PDNAKXUpQGczdylAZmh1eXExZnNoaGRmOzRAMHBgX2pjMjVoXy0tYC0vc3MtbyNvI0M0LTYzLS8tLTAvLi4tLi9pOmItbyM6YDBvI3BiZnJoXitqdDojLy5e&version_code=5.7.0&pass-region=1&pass-route=1&js_sdk_version=1.13.0.0&app_name=aweme&vid=137ED526-308B-484E-B593-B14E61FAFDE1&app_version=5.7.0&device_id=59637246415&channel=App%20Store&mcc_mnc=46000&aid=1128&screen_width=1242&openudid=770220518fd3c5914450ced05b12893b6126ff7e&os_api=18&ac=WIFI&os_version=11.4&device_platform=iphone&build_number=57010&device_type=iPhone8%2C2&iid=68446596697&idfa=CD7CBDBB-ECEB-47BA-8726-CA29C90A6DE5
# music
# http://v5-dy.ixigua.com/088c9c0ee27a62ac379440719d9314b1/5cb2a804/video/m/22069539a6a8bb840cca049bf09fbbd5de41161c7d70000035088f3f69cd/?rc=Mzdydzg3aGZ4bDMzOmkzM0ApQHRAb0g6OzozODkzNDU3Mzc3PDNAKXUpQGczdylAZmxkamV6aGhkZjs0QGxwaDRkNDVwaV8tLS8tMHNzLW8jbyNDNTQuLi0vLS0xLy4uLS4vaTpiLW8jOmAvbyNtbCtiK2p0OiMvLl4%3D


# 头像
# http://p1-dy.bytecdn.cn/img/mosaic-legacy/90eb0026e29c3c9b5822~168x168.webp
# music1
# http://v6-dy.ixigua.com/393e01f263b5677d989cf6df3af89ee6/5cb2aa16/video/m/22058c11d67edd84e7bb42302e26bbd5ffe11613d86e0000b27f98dc4fb1/?rc=MzhqbGw7czR5bDMzN2kzM0ApQHRAbzY7OjgzNzozNDo2Mzc3PDNAKXUpQGczdylAZmxkamV6aGhkZjs0QF5ecGQ2cXNpbF8tLTAtMHNzLW8jbyNBMy8uLS0vLS0vMC4uLS4vaTpiLW8jOmAvbyNtbCtiK2p0OiMvLl4%3D
# music2
# http://v6-dy.ixigua.com/88fa68a6d09bb856d149273150e66e8c/5cb2aa13/video/m/22031f0a2d1073d45fd9247d596d6ffcc691161cde450000a0200c4a0aed/?rc=M2xybmp2bDU6bDMzNWkzM0ApQHRAbzNEOTQ0ODszNDw2Mzc3PDNAKXUpQGczdylAZmxkamV6aGhkZjs0QGRzbW1zaTBrbF8tLV8tMHNzLW8jbyNDNDUxNS0vLS0vMC4uLS4vaTpiLW8jOmAvbyNtbCtiK2p0OiMvLl4%3D

# music
# http://v9-dy.ixigua.com/d0d2850e8367f73d455564732e93982d/5cb2ab3b/video/m/22031f0a2d1073d45fd9247d596d6ffcc691161cde450000a0200c4a0aed/?rc=M2xybmp2bDU6bDMzNWkzM0ApQHRAb0RGMzUzNDczNDg7Mzc3PDNAKXUpQGczdylAZmxkamV6aGhkZjs0QGRzbW1zaTBrbF8tLV8tMHNzLW8jbyMxNC0uLS4vLS0vMC4uLS4vaTpiLW8jOmAvbyNtbCtiK2p0OiMvLl4%3D
# http://v3-dy-x.ixigua.com/5041f0f3d9464eccb9f271ca2b8e0b11/5cb2ab39/video/m/22044ea0b4d079749a1a0ad8146907d5c211161c4ca600006d15a3138f40/?rc=am5zNXFpbTM7bDMzO2kzM0ApQHRAbzY1NjgzPDczNDo7Mzc3PDNAKXUpQGczdylAZmxkamV6aGhkZjs0QGNqcy80YjBsbF8tLWMtMHNzLW8jbyMwNTQvNS0vLS0vMC4uLS4vaTpiLW8jOmAvbyNtbCtiK2p0OiMvLl4%3D
# http://v6-dy.ixigua.com/2f37e27aec064d4d3e467c32eba457d6/5cb2ac80/video/m/220e966aef37951465c9930de5f9839da1d1161d62cf000004f1035df09f/?rc=ajR5bmprZjQ4bDMzN2kzM0ApQHRAb0Q6OjgzNzozNDM2Mzc3PDNAKXUpQGczdylAZmxkamV6aGhkZjs0QDBicGRrXzQ2bV8tLTAtMHNzLW8jbyMyLS8uLS0vLS0yMS4uLS4vaTpiLW8jOmAvbyNtbCtiK2p0OiMvLl4%3D


# https://aweme.snssdk.com/aweme/v1/playwm/?video_id=6610679501925911815&line=0

# http://v5-dy.ixigua.com/56722ae2389b47ebf960378639b2213d/5cb30c82/video/m/2208f59a07afe384892bf5fde3063959ea91161cf32d00006f47b50ff73a/?rc=M3Q2PGlndHl1bDMzOmkzM0ApQHRAbzo8OTQzOzgzNDQ2Ojc3PDNAKXUpQGczdylAZmxkamV6aGhkZjs0QGxsYGFsMTZual8tLV4tL3NzLW8jbyMtNDAwLS0vLS0uMC4uLS4vaTpiLW8jOmAvbyNtbCtiK2p0OiMvLl4%3D
# https://www.iesdouyin.com/share/video/6610679501925911815/?u_code=hjdm8k44&region=CN&mid=6610679524466101005&schema_type=1&object_id=6610679501925911815&utm_campaign=client_scan_share&app=aweme&utm_medium=ios&tt_from=scan_share&iid=45561030398&utm_source=scan_share
# 获取喜欢列表
# https://www.iesdouyin.com/aweme/v1/aweme/favorite/?user_id=93515402600&count=21&max_cursor=0&aid=1128&_signature=fBZqMxAcIH.WOSqz4s5eTHwWai&dytk=6849c66ff2a629554679fe#e4ad1343a5