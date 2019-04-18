from douyinspider.hot import category,billboard
from douyinspider.download import Downloader, getDownloadPath, getMusicDownloadPath, getVideoDownloadPath, getCategoryDownloadPath
from douyinspider.structures import Topic,Video,MusicCollection,Music
from douyinspider.person import favorite,post
from douyinspider.music import music_collection

# 下载分类视频
def downloadCategory():
    downloader = Downloader()
    # 设置maxCursor最大请求偏移
    for item in category(maxCursor=50):
        if isinstance(item, Topic):
            current_path = getCategoryDownloadPath(item.name)
            videos = item.videos(5) #下载前5页的数据
            for video in videos:
                downloader.download_mp4_path(video.play_url, video.id, current_path)


# 下载广告推广视频
def downloadBillboard():
    current_path = getDownloadPath('billboard')
    downloader = Downloader(current_path)
    for item in billboard():
        if isinstance(item, Video):
            downloader.download_mp4(item.play_url,item.id)


# 下载用户喜欢的视频
def downloadFavorite(user_id, user_name):
    current_path = getVideoDownloadPath(user_name, 'favorite')
    downloader = Downloader(current_path)
    print('正在下载', user_name, '喜欢的视频...')
    for item in favorite(user_id, user_name):
        if isinstance(item, Video):
            downloader.download_mp4(item.play_url, item.id)
    print(user_name, '喜欢的视频下载完成')


# 下载用户提交的视频
def downloadPost(user_id, user_name):
    current_path = getVideoDownloadPath(user_name, 'post')
    downloader = Downloader(current_path)
    print('正在下载', user_name, '提交的视频...')
    for item in post(user_id, user_name):
        if isinstance(item, Video):
            downloader.download_mp4(item.play_url, item.id)
    print(user_name, '提交的视频下载完成')

# 下载音乐榜音乐
def downloadMusicCollection():
    downloader = Downloader()
    for musicCollection in music_collection():
        if isinstance(musicCollection, MusicCollection):
            print('正在下载',musicCollection.mc_name,'...')
            music_path = getMusicDownloadPath(musicCollection.mc_name)
            musics = musicCollection.mc_musics if musicCollection.mc_musics else []
            for music in musics:
                if isinstance(music, Music):
                    downloader.download_mp3_path(music.play_url, music.name, music_path)
            print(musicCollection.mc_name, '下载完成')