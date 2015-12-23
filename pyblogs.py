# FIXME: Use the typing module to assign type information

class Blog:
    """A blog model"""

    url = None
    title = None

    def __init__(self, title, url) -> None:
        self.title = title
        self.url = url

    def __repr__(self):
        return '{}: {}'.format(self.title, self.url)

    @classmethod
    def get_fav_blogs(cls, limit):
        return PYTHON_BLOGS[0:limit]


PYTHON_BLOGS = [
    Blog(title='Talk Python to me', url='http://talkpython.fm'),
    Blog(title='Planet Python', url='http://planetpython.org/'),
    Blog(title='Lucumr', url='http://lucumr.pocoo.org/'),
    Blog(title='Doug Hellmann', url='https://doughellmann.com/blog/'),
    Blog(title='PyDanny', url='http://www.pydanny.com/'),
    Blog(title='Invent with Python', url='http://inventwithpython.com/blog/'),
]
