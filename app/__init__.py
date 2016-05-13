from flask import Flask, render_template
from flask_flatpages import FlatPages
from config import config
from flask_frozen import Freezer
from flask.ext.assets import Environment
from . import asset_bundle

flatpages = FlatPages()
freezer = Freezer()
assets = Environment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    flatpages.init_app(app)
    freezer.init_app(app)
    assets.init_app(app)
    assets.register('js_all', asset_bundle.js_all)
    assets.register('css_all', asset_bundle.css)
    assets.register('portfolio_css', asset_bundle.portfolio_css)
    assets.register('resume_css', asset_bundle.resume_css)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
