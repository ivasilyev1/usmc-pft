from logging.config import fileConfig

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

fileConfig('./log.conf')

app = Flask(__name__)

CORS(app, resources={r"*":{"origins": "http://localhost:*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usmc-pft.db'
db = SQLAlchemy(app)

from usmc_pft import routes
