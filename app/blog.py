import datetime

class Blog():
    def __init__(self, flatpages):
        self.flatpages = flatpages
        self.posts = [page for page in self.flatpages]
        self.posts.sort(key = lambda i:
                        datetime.datetime.strptime(i['date'], '%d %B %Y'),
                        reverse = True)
        self.pages = self.get_pages()

    def get_pages(self):
        pages = []
        for i in range(5, len(self.posts), 5):
            pages.append(self.posts[i-5: i])
        r = len(self.posts) % 5
        if r > 0:
            pages.append(self.posts[len(self.posts) - r:])
        return pages
