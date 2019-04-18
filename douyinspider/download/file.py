import os

# 获取下载路径
def getDownloadPath(dir_name):
    current_path = os.getcwd() + "/data/{0}".format(dir_name)
    if not os.path.exists(current_path):
        os.makedirs(current_path)
    return current_path


# 获取下载路径
def getCategoryDownloadPath(dir_name):
    current_path = os.getcwd() + "/data/category/{0}".format(dir_name)
    if not os.path.exists(current_path):
        os.makedirs(current_path)
    return current_path

# 获取下载路径
def getVideoDownloadPath(user_name, dir_name):
    current_path = os.getcwd() + "/data/video/{0}/{1}".format(user_name, dir_name)
    if not os.path.exists(current_path):
        os.makedirs(current_path)
    return current_path

# 获取音乐下载路径
def getMusicDownloadPath(music_collection_name):
    current_path = os.getcwd() + "/data/music/{0}".format(music_collection_name)
    if not os.path.exists(current_path):
        os.makedirs(current_path)
    return current_path