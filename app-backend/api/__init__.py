from . config import Config
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


# APP Instance
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


# APP Routes
@app.route("/")
def hello_world():
    return jsonify(hello="world")
