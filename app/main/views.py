from flask import render_template
from . import main
from .. import flatpages
from ..blog import Blog

content = Blog(flatpages)

def page_test(page_num):
    if len(content.pages) > page_num:
        newer_pages = True
    else:
        newer_pages = False
    if page_num > 1:
        older_pages = True
    else:
        older_pages = False
    return older_pages, newer_pages

@main.route('/')
def blog():
    older_pages, newer_pages = page_test(1)
    return render_template('blog.html',
                           posts = content.pages[0],
                           newer_pages = newer_pages,
                           older_pages = False,
                           page_num = 1)

@main.route('/pages/<num>')
def pages(num):
    num = int(num)
    older_pages, newer_pages = page_test(num)
    return render_template('blog.html',
                           posts = content.pages[(num - 1)],
                           newer_pages = newer_pages,
                           older_pages = older_pages,
                           page_num = num)

@main.route('/posts/<post_name>')
def post(post_name):
    page = flatpages.get_or_404('posts/' + post_name)
    return render_template('post.html',
                           post = page)
