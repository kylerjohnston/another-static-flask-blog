### config.py
#############

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_ROOT = 'content'
    POST_DIR = 'posts'

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
