from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from config import config

flatpages = FlatPages()
freezer = Freezer()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    flatpages.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    freezer.init_app(app)
    return app
