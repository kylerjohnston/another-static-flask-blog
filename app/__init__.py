from flask import Flask, render_template
from flask_flatpages import FlatPages
from config import config
from flask_frozen import Freezer

flatpages = FlatPages()
freezer = Freezer()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    flatpages.init_app(app)
    freezer.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
