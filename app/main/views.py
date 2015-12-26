from flask import render_template
from . import main
from .. import flatpages

@main.route('/')
def blog():
    posts = [page for page in flatpages]
    posts.sort(key = lambda item:item['date'], reverse = False)
    return render_template('blog.html', posts = posts)
