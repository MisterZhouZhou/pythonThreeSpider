import os

# 获取下载路径
def getDownloadPath(dir_name):
    current_path = os.getcwd() + "/data/{0}".format(dir_name)
    if not os.path.exists(current_path):
        os.makedirs(current_path)
    return  current_path