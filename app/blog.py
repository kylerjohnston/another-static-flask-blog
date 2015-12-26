# blog.py
# Static blog generator

import sys
from flask import Flask, render_template
from flask.ext.script import Manager
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'
app = Flask(__name__)
manager = Manager(app)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)

@manager.command
def build():
    freezer.freeze()

@app.route('/')
def posts():
    posts = [page for page in flatpages]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('blog.html', posts=posts)

@app.route('/posts/<name>')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    manager.run()

