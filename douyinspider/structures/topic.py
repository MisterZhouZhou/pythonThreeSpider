from douyinspider.structures import Base
from douyinspider.utils.fetch import fetch
from douyinspider.url.urls import URL
from douyinspider.config import common_headers


class Topic(Base):
    
    def __init__(self, **kwargs):
        """
        init topic object
        :param kwargs:
        """
        super().__init__()
        self.id = kwargs.get('id')
        self.view_count = kwargs.get('view_count')
        self.user_count = kwargs.get('user_count')
        self.name = kwargs.get('name')
        self.desc = kwargs.get('desc')
        self.videos = kwargs.get('videos')
    
    def __repr__(self):
        """
        music to str
        :return:
        """
        return '<Topic: <%s, %s>>' % (self.id, self.name)
    
    # def videos(self, max=None):
    #     """
    #     get videos of topic
    #     :return:
    #     """
    #
    #     from douyinspider.utils.tranform import data_to_video
    #     if max and not isinstance(max, int):
    #         raise RuntimeError('`max` param must be int')
    #     query = {
    #         'device_id': '58097798460',
    #         'ch_id': self.id,
    #         'count': '18',
    #         'aid': '1129'
    #     }
    #     offset, count = 0, 0
    #     videos = []
    #     while True:
    #         # define cursor
    #         query['cursor'] = str(offset)
    #         result = fetch(URL.topic2video_url(), params=query, headers=common_headers, verify=False)
    #         aweme_list = result.get('aweme_list', [])
    #         print(URL.topic2video_url())
    #         print(result)
    #         print('===')
    #         for item in aweme_list:
    #             video = data_to_video(item)
    #             count += 1
    #             videos.append(video)
    #             if max and count >= max:
    #                 return
    #         # next page
    #         if result.get('has_more'):
    #             offset += 18
    #         else:
    #             break
    #     return videos