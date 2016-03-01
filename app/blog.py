import datetime

def get_pages(posts):
    """ Groups blog posts into 'pages' of five posts """
    pages = []
    for i in range(4, len(posts), 5):
        pages.append(posts[i-4: i+1])
    r = len(posts) % 5
    if r > 0:
        pages.append(posts[len(posts) - r:])

    return pages

def gen_tags(posts):
    """ Returns a list of dictionaries indicating tag name and tag count
    sorted by tag count. """
    tag_list = {}
    for post in posts:
        for tag in post['tags']:
            if tag in tag_list:
                tag_list[tag] += 1
            else:
                tag_list[tag] = 1
    tags = [{'tag': x, 'count': tag_list[x]} for x in tag_list]
    tags.sort(key = lambda x: x['count'], reverse = True)
    return tags

class Blog():
    def __init__(self, flatpages, post_dir, draft_dir):
        self.flatpages = flatpages
        self.posts = [page for page in self.flatpages
                      if page.path.startswith(post_dir)]
        self.posts.sort(key = lambda i:
                        datetime.datetime.strptime(i['date'], '%d %B %Y'),
                        reverse = True)
        self.drafts = [page for page in self.flatpages
                       if page.path.startswith(draft_dir)]
        self.pages = get_pages(self.posts)
        self.tags = gen_tags(self.posts)
        for post in self.posts:
            post.slug = post.path.split('/')[1]
