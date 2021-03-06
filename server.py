from flask import redirect
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_bootstrap_components import themes
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    "El Flow Violento Del Team 79",
    external_stylesheets=[themes.BOOTSTRAP],
    suppress_callback_exceptions=True)

server = app.server
server.config.from_object(Config)

# TODO: implementar algún método de encriptación para asegurar este llave
server.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

login_manager = LoginManager()
login_manager.init_app(server)

db = SQLAlchemy(server)
migrate = Migrate(server, db)
