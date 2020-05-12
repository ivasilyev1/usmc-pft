from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, logging

app = Flask(__name__)
CORS(app, resources={r"*":{"origins": "http://localhost:3000"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usmc-pft.db'
db = SQLAlchemy(app)

from usmc_pft import routes