from douyinspider.structures import Base
from douyinspider.utils.fetch import fetch
from douyinspider.url.urls import URL
from douyinspider.config import common_headers,person_post_headers


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
        # self.videos = kwargs.get('videos')
    
    def __repr__(self):
        """
        music to str
        :return:
        """
        return '<Topic: <%s, %s>>' % (self.id, self.name)
    
    def videos(self, max=None):
        """
        get videos of topic
        :return:
        """

        from douyinspider.utils.tranform import data_to_video
        if max and not isinstance(max, int):
            raise RuntimeError('`max` param must be int')
        import subprocess
        query = {
            'ch_id': self.id,
            'count': '9',
            'cursor': '0',
            'aid': '1128'
        }
        offset, count = 0, 0
        videos = []
        sign_code = "" + query['ch_id'] + query['count'] + str(offset)
        signature = subprocess.getoutput('node signature.js %s' % sign_code)

        while True:
            # define cursor, 这里有个问题就是生成了正确的签名也不一定可以拿到数据，以此还要做循环请求
            if query['cursor'] != str(offset) and offset != 0:
                signature = subprocess.getoutput('node signature.js %s' % sign_code)
            query['cursor'] = str(offset)
            query['_signature'] = signature
            result = fetch(URL.category_list_videos(), params=query, headers=common_headers, verify=False)
            aweme_list = result.get('aweme_list', [])
            if aweme_list != None and len(aweme_list) >= 1:
                for item in aweme_list:
                    video = data_to_video(item)
                    count += 1
                    videos.append(video)
                if count >= max:
                    break
                # next page
                if result.get('has_more') != 1:
                    break
                else:
                    offset = result.get('cursor')
        return videos