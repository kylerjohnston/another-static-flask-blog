### config.py
#############

import os
from flask import render_template_string, Markup
import markdown

basedir = os.path.abspath(os.path.dirname(__file__))

def prerender_jinja(text):
    # This function prerenders Jinja code in flatpages markdown
    prerendered_body = render_template_string(Markup(text))
    return markdown.markdown(prerendered_body, Config.MARKDOWN_EXTENSIONS)

class Config:
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_ROOT = 'content'
    POST_DIR = 'posts'
    DRAFT_DIR = 'drafts'
    FREEZER_RELATIVE_URLS = False
    MARKDOWN_EXTENSIONS = ['footnotes',
                           'smarty',
                           'codehilite(linenums=False)']
    FLATPAGES_AUTO_RELOAD = False
    FLATPAGES_HTML_RENDERER = prerender_jinja
    FREEZER_DESTINATION_IGNORE = ['.gitignore',
                                  '.git/',
                                  'CNAME',
                                  'robots.txt']
    FREEZER_BASE_URL = 'http://kylerjohnston.com/'
    FREEZER_IGNORE_404_NOT_FOUND = True # To generate /404.html

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    SHOW_DRAFTS = False

class DraftingConfig(DevelopmentConfig):
    SHOW_DRAFTS = True

class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    SHOW_DRAFTS = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SHOW_DRAFTS = False

config = {
    'dev': DevelopmentConfig,
    'production': ProductionConfig,
    'drafting': DraftingConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}
