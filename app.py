import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from passlib.hash import pbkdf2_sha256
import uuid
import pymongo
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

db = mongo.db


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)