#!/usr/bin/env python

import os
from app import create_app, freezer
from flask.ext.script import Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def build():
    app = create_app('production')
    if(app.config['SHOW_DRAFTS'] | app.debug | app.testing):
        print('WARNING!! This build will show drafts or is running in debug or testing mode.')
    freezer.init_app(app)
    freezer.freeze()

@manager.command
def test():
    import nose
    import sys
    from config import basedir
    nose.run(
        argv = [sys.argv[0],
                os.path.join(basedir, 'tests')]
    )

if __name__ == '__main__':
    manager.run()
