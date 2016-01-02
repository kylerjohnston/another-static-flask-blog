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
    FLATPAGES_HTML_RENDERER = prerender_jinja
    FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite(linenos=False)']
    
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
