#!/usr/bin/env python

import os
from app import create_app, freezer
from flask.ext.script import Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def build():
    app.debug = False
    app.testing = True
    if(app.config['SHOW_DRAFTS']):
        print('Warning: Draft posts will be visible in this build.')
    freezer.freeze()

@manager.command
def test():
    import nose
    nose.main()

if __name__ == '__main__':
    manager.run()
