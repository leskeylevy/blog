from flask import Flask
from config import config_options


# initialising the app
def create_app(config_name):
    app = Flask(__name__)
    return app


# from app import views

