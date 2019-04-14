class URL:
    BaseURL = "https://aweme.snssdk.com/aweme/v1/"

    @classmethod
    def favorite_url(cls):
        return cls.BaseURL + "aweme/favorite/"