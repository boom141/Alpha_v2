import os
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(APP_PATH, 'webApplication\\templates')
STATIC = os.path.join(APP_PATH, 'webApplication\\static')

def init_app():
    app = Flask(__name__, template_folder= TEMPLATE, static_folder= STATIC)
    app.config['SECRET_KEY'] = 'ybe67i0u'

    CORS(app)
    sio = SocketIO(app, cors_allowed_origin = '*')

    from .scripts.web_routes.views import views
    app.register_blueprint(views, url_prefix= '/')

    from .scripts.networking.sio_namespace import players_lobby
    sio.on_namespace(players_lobby('/lobby'))

    return sio, app