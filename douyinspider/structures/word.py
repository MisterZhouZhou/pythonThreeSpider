from douyinspider.structures import Base
# 热门词
class Word(Base):

    def __init__(self, **kwargs):
        """
        init word object
        :param kwargs:
        """
        super().__init__()
        self.word_covers = kwargs.get('word_covers')
        self.word = kwargs.get('word')
        self.hot_value = kwargs.get('hot_value')
        self.label = kwargs.get('label')
        self.position = kwargs.get('position')

    def __repr__(self):
        """
        video to str
        :return: str
        """
        return '<Word: <%s, %s>>' % (self.position, self.word)


