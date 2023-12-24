import logging
import os
import yaml
from flask import Flask

logging.basicConfig(level=logging.DEBUG)

basedir = os.path.abspath(os.path.dirname(__file__))
DEFAULT_CONFIG_FILE = os.path.join(basedir, "config.yaml")

class YamlConfig:

    def __init__(self, config_file):
        # Load config from a yaml file
        with open(config_file) as f:
            config = yaml.safe_load(f)
            if config is not None:
                for key, value in config.items():
                    setattr(self, key.upper(), value)

def create_app():
    # Boilerplate to create  Flask app and load a config.yaml file
    app = Flask(__name__)
    config_file = os.environ.get('FLASK_CONFIG_FILE') or DEFAULT_CONFIG_FILE
    logging.info(f"Base directory: {basedir}")

    app.config.from_object(YamlConfig(config_file))

    # Register blueprints
    from todoink.api import bp
    app.register_blueprint(bp, url_prefix='/api')

    return app
