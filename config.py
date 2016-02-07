### config.py
#############

import os
from flask import render_template_string, Markup
from flask_flatpages import pygmented_markdown

basedir = os.path.abspath(os.path.dirname(__file__))

def prerender_jinja(text):
    """ This function uses Jinja to prerender flatpages.
    Courtesy of http://stackoverflow.com/questions/21576520/mix-images-with-markdown-in-a-flask-app
    """
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

class Config:
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_ROOT = 'content'
    POST_DIR = 'posts'
    FREEZER_RELATIVE_URLS = True
# FLATPAGES_MARKDOWN_EXTENSIONS won't work because of the prerender_jinja hack.
# I've edited venv/lib/python3.5/site-packages/flask_flatpages/utils.py
# to include the needed markdown extensions instead in the pygmented_markdown
# function. See lines 40-41 in that file. THIS IS A TERRIBLE HACK. I'm going
# to submit an issue on Github to see if I can resolve it a better way. But
# for the time being this will work.
#
#    FLATPAGES_MARKDOWN_EXTENSIONS = ['footnotes',
#                                    'smarty',
#                                    'codehilite']
#
    FLATPAGES_AUTO_RELOAD = True
    FLATPAGES_HTML_RENDERER = prerender_jinja
    FREEZER_DESTINATION_IGNORE = ['.gitignore',
                                  '.git/',
                                  'CNAME']
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    DEBUG = False
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
