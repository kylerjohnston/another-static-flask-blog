#!/usr/bin/env python

import os
from app import create_app, freezer
from flask.ext.script import Manager
from config import basedir
from itertools import chain
from jinja2 import Template
import datetime

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def build():
    app = create_app('production')
    if(app.config['SHOW_DRAFTS'] | app.debug | app.testing):
        print('WARNING!! This build will show drafts or is running in debug or testing mode.')
    freezer.init_app(app)
    freezer.freeze()
    buildSitemap()

@manager.command
def test():
    import nose
    import sys
    from config import basedir
    nose.run(
        argv = [sys.argv[0],
                os.path.join(basedir, 'tests')]
    )

def buildSitemap():
    template_path = os.path.join(basedir, 'app/templates/sitemap.xml')
    directory = os.path.join(basedir, 'app/build')
    endpoints = findHTML(directory)
    template = ''
    with open(template_path, 'r') as f:
        template = Template(f.read())
    with open(os.path.join(directory, 'sitemap.xml'), 'w') as f:
        f.write(template.render(pages = endpoints))

def findHTML(directory):
    base = os.path.join(basedir, 'app/build')
    endpoints = []
    subdirs = []
    contents = os.listdir(directory)
    for item in contents:
        path = os.path.join(directory, item)
        if item.endswith('.html'):
            url = path.replace(base, 'http://kylerjohnston.com')
            endpoints.append([url, getLastMod(path)])
        if os.path.isdir(path):
            subdirs.append(path)
    
    # Recurse through all subdirectories
    if len(subdirs) > 0:
        for subdir in subdirs:
            ep = findHTML(subdir)
            for e in ep:
                endpoints.append(e)

    return endpoints

def getLastMod(f):
    return datetime.date.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    manager.run()
