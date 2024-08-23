import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

app.secret_key = "smart-condominium"
app.config.from_object("config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .views.views import *
from .views.condominio_views import *
from .views.veiculo_views import *
from .views.morador_views import *
from .models.veiculo_model import Veiculo
from .models.morador_model import Morador
