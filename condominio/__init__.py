import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

app.secret_key = "smart-condominium"
app.config.from_object("config")

db = SQLAlchemy(app)

from views.views import *
from models.veiculo_model import Veiculo
