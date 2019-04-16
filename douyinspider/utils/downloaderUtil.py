from douyinspider.hot import category,billboard
from douyinspider.download import Downloader,getDownloadPath
from douyinspider.structures import Topic,Video
from douyinspider.person import favorite,post


# 下载分类视频
def downloadCategory():
    current_path = getDownloadPath('category')
    downloader = Downloader(current_path)
    # 设置maxCursor最大请求偏移
    for item in category(maxCursor=50):
        if isinstance(item, Topic):
            videos = item.videos
            for video in videos:
                downloader.download_mp4(video.play_url, video.id)


# 下载广告推广视频
def downloadBillboard():
    current_path = getDownloadPath('billboard')
    downloader = Downloader(current_path)
    for item in billboard():
        if isinstance(item, Video):
            downloader.download_mp4(item.play_url,item.id)



# 下载用户喜欢的视频
def downloadFavorite(user_id, user_name):
    current_path = getDownloadPath('favorite')
    downloader = Downloader(current_path)
    for item in favorite(user_id, user_name):
        if isinstance(item, Video):
            downloader.download_mp4(item.play_url, item.id)


# 下载用户提交的视频
def downloadPost(user_id, user_name):
    current_path = getDownloadPath('post')
    downloader = Downloader(current_path)
    for item in post(user_id, user_name):
        if isinstance(item, Video):
            downloader.download_mp4(item.play_url, item.id)
