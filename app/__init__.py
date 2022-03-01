from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(Config)
from werkzeug.security import generate_password_hash

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def __init__(self, first_name, last_name, username, password):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username 
    self.password = generate_password_hash(password, method='pbkdf2:sha256')
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)

from app import views
