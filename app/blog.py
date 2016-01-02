import datetime

class Blog():
    def __init__(self, flatpages, post_dir):
        self.flatpages = flatpages
        self.posts = [page for page in self.flatpages
                      if post_dir in page.path]
        self.posts.sort(key = lambda i:
                        datetime.datetime.strptime(i['date'], '%d %B %Y'),
                        reverse = True)
        self.pages = self.get_pages()
        self.tags = self.gen_tags()
        for post in self.posts:
            post.slug = post.path.split('/')[1]

    def get_pages(self):
        pages = []
        for i in range(5, len(self.posts), 5):
            pages.append(self.posts[i-5: i])
        r = len(self.posts) % 5
        if r > 0:
            pages.append(self.posts[len(self.posts) - r:])
        return pages

    def gen_tags(self):
        tag_list = {}
        for post in self.posts:
            for tag in post['tags']:
                if tag in tag_list:
                    tag_list[tag] += 1
                else:
                    tag_list[tag] = 1
        tags = [{'tag': x, 'count': tag_list[x]} for x in tag_list]
        tags.sort(key = lambda x: x['count'], reverse = True)
        return tags
