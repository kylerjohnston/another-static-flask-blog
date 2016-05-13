from flask import render_template, request
from flask_flatpages import pygments_style_defs
from . import main
from .. import flatpages, freezer
from ..blog import Blog
from manage import app
from werkzeug.contrib.atom import AtomFeed
import datetime

content = Blog(flatpages, app.config['POST_DIR'], app.config['DRAFT_DIR'])

@freezer.register_generator
def error_handlers():
    yield '/404.html'

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

@main.route('/blog')
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

@main.route('/about')
def about():
    return render_template('static.html',
                           description = 'Kyle Johnston is a coder, teacher, writer, and a researcher of 19th-century British literature at the University of Illinois at Urbana-Champaign.',
                           post = flatpages.get_or_404('about'))

@main.route('/tags/<tag>')
def view_tag(tag):
    tagged_posts = [post for post in content.posts if tag in post['tags']]
    return render_template('tag_results.html',
                           posts = tagged_posts,
                           tag = tag)

@main.route('/tags')
def view_tags():
    two_col_tags = []
    for x in range(0, len(content.tags), 2):
        try:
            two_col_tags.append({'one': content.tags[x]['tag'],
                                 'two': content.tags[x+1]['tag']})
        except:
            two_col_tags.append({'one': content.tags[x]['tag'],
                                 'two': ''})
    return render_template('tags.html',
                           two_col_tags = two_col_tags,
                           tags = content.tags)

@main.route('/archive')
def archive():
    return render_template('archive.html',
                           posts = content.posts)

@main.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}

@main.route('/recent.atom')
def atom_feed():
    feed = AtomFeed('Recent Posts',
                    feed_url=request.url, url=request.url_root)
    for post in content.posts:
        postdate = datetime.datetime.strptime(post['date'], '%d %B %Y')
        feed.add(post['title'], post.html,
                 content_type='html',
                 author='Kyle Johnston',
                 url='http://kylerjohnston.com/posts/{}/'.format(post.slug),
                 updated=postdate,
                 published=postdate)
    return feed.get_response()

@main.route('/')
def portfolio():
    return render_template('portfolio.html')

@main.route('/resume')
def resume():
    return render_template('resume.html')

if app.config['SHOW_DRAFTS']:
    @main.route('/drafts')
    def drafts():
        return render_template('blog.html',
                               posts = [post for post in content.drafts],
                               newer_pages = False,
                               older_pages = False,
                               page_num = 1)
