# url类
class URL(object):
    BaseURL = "https://aweme.snssdk.com/aweme/v1/"

    BaseApiURL = "https://api.amemv.com/aweme/v1/"

    @classmethod
    def favorite_url(cls):
        return cls.BaseURL + "aweme/favorite/"

    # 广告,不支持分页(成功）
    @classmethod
    def billboard(cls):
        return cls.BaseApiURL + "hotsearch/aweme/billboard/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&mas=01e3e5cef0de029bfcdd34f97a802bb868733f3265261a5cdb072e&as=a13500cd74892b29d04593&ts=1540360596"

    # 热门搜索
    @classmethod
    def hot_search(cls):
        return cls.BaseApiURL + "hot/search/list/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&detail_list=0&mas=01b4002e3d345720d85d1983fe6b328535431c67b1f365be1f2f38&as=a1e5000df9532bbfa03287&ts=1540362041"

    # 分类，支持分页(成功)
    @classmethod
    def category_list(cls):
        return cls.BaseApiURL + "category/list/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&count=10&cursor=30&mas=017cf50c73008bad543b552ca0369777473911b0e7c8fbc462a721&as=a195ab9d916dfba5629896&ts=1540535761"

    # 挑战
    @classmethod
    def challenge(cls):
        return cls.BaseApiURL + "challenge/aweme/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&query_type=0&cursor=72&ch_id=1579168686354445&count=18&pull_type=2&type=5&mas=01fa6c53471c45dc2f83db17c2c208d492d353529e1eae812f2728&as=a1656b8d763eabc5a28997&ts=1540535782"


    # 音频
    @classmethod
    def music2video_url(cls):
        return cls.BaseApiURL + "music/aweme/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&cursor=0&music_id=6606196836371794691&pull_type=2&count=18&type=6&mas=0143c9f3d621b358454717211b3d5b91be242eaad18243a010d6a8&as=a1756b5dab96bb15627918&ts=1540535659"


    # 话题
    @classmethod
    def topic2video_url(cls):
        # return cls.BaseApiURL + "challenge/aweme/"
        # url = 'https://api.amemv.com/aweme/v1/challenge/aweme/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&query_type=0&cursor=0&ch_id=1614257803840525&count=18&pull_type=2&type=5&mas=019e89de1c6917f6ff17e5a3fb15e9f4a042dc4b112dd70bc304ee&as=a115357dd5d06b22130853&ts=1540575749'
        # url = 'https://api.amemv.com/aweme/v1/challenge/aweme/?ac=WIFI&iid=49530073634&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=31006&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=3.1.0&js_sdk_version=1.3.0.1&version_code=3.1.0&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&query_type=0&cursor=0&ch_id=1615917132956695&count=18&pull_type=2&type=5&mas=019a446388982299eccaa62c24afeab1fa2c9ae7543ea3cb48af31&as=a16575fd5f15fbfaad0086&ts=1541233247'
        return cls.BaseApiURL + "challenge/aweme/?ac=WIFI&iid=46961748949&device_id=58097798464&os_api=18&app_name=aweme&channel=App%20Store&idfa=B6B7BF1B-AADD-42E6-83AB-D29C93620305&device_platform=iphone&build_number=29101&vid=5A56818A-EC4B-4C9B-843F-881E99603F5A&openudid=825a48a41a70c4182b21cc442993c6bf6f1ed6e6&device_type=iPhone9,2&app_version=2.9.1&version_code=2.9.1&os_version=12.0&screen_width=1242&aid=1128&pass-region=1&query_type=0&cursor=0&ch_id=1614257803840525&count=18&pull_type=2&type=5&mas=019e89de1c6917f6ff17e5a3fb15e9f4a042dc4b112dd70bc304ee&as=a115357dd5d06b22130853&ts=1540575749"

