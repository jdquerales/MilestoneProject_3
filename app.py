import os
from flask import (Flask, flash, render_template, jsonify,
                   request, session, redirect, url_for)
from functools import wraps
from flask_pymongo import PyMongo
from passlib.hash import pbkdf2_sha256
import datetime
import uuid
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# create an instance of MongoDB database
mongo = PyMongo(app)

db = mongo.db


# decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('home'))
    return wrap

# Create User Class to be used in SignIn and SignUp functionalities


class User:
    def start_session(self, user):
        user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        print(request.form)

        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name').lower(),
            "username": request.form.get('username').lower(),
            "email": request.form.get('email').lower(),
            "affiliation": request.form.get('affiliation'),
            "password": request.form.get('password')
        }

# Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        # Check for existing email address
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use"}), 400
        if db.users.insert_one(user):
            return self.start_session(user)
        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect(url_for('home'))

    def login(self):
        user = db.users.find_one({"email": request.form.get('email').lower()})
        if user and pbkdf2_sha256.verify(
                request.form.get('password'),
                user['password']):
            return self.start_session(user)
        return jsonify({"error": "Invalid login credentials"}), 401

    def update(self):
        updated_user = {
            "name": request.form.get('name').lower(),
            "username": request.form.get('username').lower(),
            "email": request.form.get('email').lower(),
            "affiliation": request.form.get('affiliation'),
            "password": session['user']['password']
        }
        mongo.db.users.update({"_id": session['user']['_id']}, updated_user)
        flash("User Updated. Changes will be reflected in your next session!")
        return redirect(url_for('dashboard'))


class CreateNewJC:
    def submission(self):
        journal = {
            "_id": uuid.uuid4().hex,
            "title": request.form.get('title'),
            "field_research": request.form.get('field'),
            "abstract": request.form.get('abstract'),
            "link": request.form.get('link'),
            "location": request.form.get('location'),
            "iso_format": datetime.datetime.now(),
            "added_on": datetime.datetime.now().strftime("%d-%m-%Y"),
            "added_by": session['user']['name']
        }
        return db.add_article.insert_one(journal)


class Subscription:
    def subscriber(self):
        # check if username already exists in db
        existing_user = mongo.db.subscribers.find_one(
            {"email": request.form.get("subscriptionEmail").lower()})

        if existing_user:
            flash("Email already subscribed, try another account!")
        else:
            new_user = {
                "_id": uuid.uuid4().hex,
                "name": request.form['subscriptionName'].lower(),
                "email": request.form['subscriptionEmail'].lower(),
            }
            mongo.db.subscribers.insert_one(new_user)
            flash("Thanks for subscribing ! ")


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/home', methods=['POST', 'GET'])
def subscribe():
    if request.method == 'POST':
        Subscription().subscriber()
    return redirect(url_for('home', _anchor="about"))


@app.route('/events')
def events():
    journals = list(mongo.db.add_article.find().sort([("iso_format", -1)]))
    return render_template('events.html', journals=journals)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/changeinfo')
def changeinfo():
    return render_template('changeinfo.html')


@app.route('/changeinfo', methods=['POST', 'GET'])
def changeInfo():
    if request.method == 'POST':
        return User().update()
    return render_template('dashboard.html')


@app.route('/signin',  methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        return User().login()
    return render_template('signin.html')


@app.route('/signout')
def signout():
    return User().signout()


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        return User().signup()

    return render_template("signup.html")


@app.route("/create")
def create():
    categories = mongo.db.field_research.find().sort("field", 1)
    return render_template('create.html', categories=categories)


@app.route('/create', methods=['POST', 'GET'])
def createJC():
    if request.method == 'POST':
        CreateNewJC().submission()
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
