import urllib

# 资源下载类
class Downloader(object):
    # 初始化路径
    def __init__(self, path):
        self.path = path

    def download_mp4(self, url, video_name):
        # 定义url,请求的api
        try:
            print("正在下载：{0}".format(video_name))
            # 设置header为app环境
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent',
                                  'Aweme 3.1.0 rv:31006 (iPhone; iOS 12.0; zh_CN) Cronet')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(url, '{0}/{1}.mp4'.format(self.path, video_name))
            print("Finish...")
        except:
            print("Failed...")
