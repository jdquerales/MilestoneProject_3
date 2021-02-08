import os
from flask import (Flask, flash, render_template, jsonify,
                   request, session, redirect, url_for)
from functools import wraps
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import uuid
if os.path.exists("env.py"):
    import env

# Create a Flask instance called app
app = Flask(__name__)

# Read env variables to connect to MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# create an instance of MongoDB database
mongo = PyMongo(app)
db = mongo.db


# I will define a decorator that will allow
# to show centain information only if the
# user is logged in
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
# Most of the actions in the app will be define within the
# User class, it will contain all the relevant actions (methods)
# and it enable us to reuse code while keeping it minimal
class User:
    # Start session method
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return redirect(url_for("dashboard"))

    # Signup method
    def signup(self):
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name').lower(),
            "username": request.form.get('username').lower(),
            "email": request.form.get('email').lower(),
            "affiliation": request.form.get('affiliation'),
            "password": generate_password_hash(request.form.get("password"))
        }
# Encrypt the password
        user['password'] = user['password']
        # Check for existing email address
        if db.users.find_one({"email": user['email']}):
            flash("Email address already in use", "danger")
            return redirect(url_for("signup"))
        if db.users.insert_one(user):
            flash("User successfully created", "success")
            return redirect(url_for("signup"))
        return jsonify({"error": "Signup failed"}), 400

    # Signout method
    def signout(self):
        session.clear()
        return redirect(url_for('home'))

    # Login method
    def login(self):
        user = db.users.find_one({"username": request.form.get('username').lower()})
        if user and check_password_hash(
                user['password'], request.form.get('password')):
            return self.start_session(user)
        else:
            flash("Invalid login credentials", "danger")
            return redirect(url_for("signin"))
        return jsonify({"error": "Invalid login credentials"}), 401

# Update user method
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


# Here I define a new Class that manage the creation of a new
# article
class CreateNewJC:
    # Submission method
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

# edition method
    def edition(self, event_id):
        submission = {
            "title": request.form.get('title'),
            "field_research": request.form.get('field'),
            "abstract": request.form.get('abstract'),
            "link": request.form.get('link'),
            "location": request.form.get('location'),
            "iso_format": datetime.datetime.now(),
            "added_on": datetime.datetime.now().strftime("%d-%m-%Y"),
            "added_by": session['user']['name']
        }
        return db.add_article.update({"_id": event_id}, submission)

    # Delete method
    def delete(self, event_id):
        return db.add_article.remove({"_id": event_id})


# Here I define a new Class that manage subscribers
class Subscription:
    def subscriber(self):
        # check if username already exists in db
        existing_user = mongo.db.subscribers.find_one(
            {"email": request.form.get("subscriptionEmail").lower()})

        if existing_user:
            flash("Email already subscribed, try another account!", "danger")
        else:
            new_user = {
                "_id": uuid.uuid4().hex,
                "name": request.form['subscriptionName'].lower(),
                "email": request.form['subscriptionEmail'].lower(),
            }
            mongo.db.subscribers.insert_one(new_user)
            flash("Thanks for subscribing ! ", "success")


# Entry point of app
@app.route("/")
def home():
    journals = list(mongo.db.add_article.find().sort([("iso_format", -1)]))
    return render_template('home.html', journals=journals)


# POST method in home
@app.route('/home', methods=['POST', 'GET'])
def subscribe():
    if request.method == 'POST':
        Subscription().subscriber()
    return redirect(url_for('home', _anchor="about"))


# Route to display events
@app.route('/events')
def events():
    journals = list(mongo.db.add_article.find().sort([("iso_format", -1)]))
    return render_template('events.html', journals=journals)


# Route to display dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    journals = list(mongo.db.add_article.find().sort([("iso_format", -1)]))
    return render_template('dashboard.html', journals=journals)


# Route to change user information
@app.route('/changeinfo')
def changeinfo():
    return render_template('changeinfo.html')


# Build POST method for changing user information
@app.route('/changeinfo', methods=['POST', 'GET'])
def changeInfo():
    if request.method == 'POST':
        return User().update()
    return render_template('dashboard.html')


# Route to Signin
@app.route('/signin',  methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        return User().login()
    return render_template('signin.html')


# Route to signout
@app.route('/signout')
def signout():
    return User().signout()


# Route to signup
@app.route('/signup')
def signup():
    return render_template('signup.html')


# Signup POST and GET methods
@app.route('/signup', methods=['POST', 'GET'])
def signUp():
    if request.method == 'POST':
        return User().signup()
    return redirect(url_for('dashboard'))


# Route to create a new journal article
@app.route("/create")
def create():
    categories = mongo.db.field_research.find().sort("field", 1)
    return render_template('create.html', categories=categories)


# Create article POST and GET methods
@app.route('/create', methods=['POST', 'GET'])
def createJC():
    if request.method == 'POST':
        CreateNewJC().submission()
    return render_template("dashboard.html")


# Route to edit an article with dynamic variable event_id
@app.route("/edit/<event_id>")
def edit(event_id):
    journals = mongo.db.add_article.find_one({"_id": event_id})
    categories = mongo.db.field_research.find().sort("field_research", 1)
    if request.method == "POST":
        CreateNewJC().edition(event_id)
    return render_template("edit.html", journals=journals,
                           categories=categories)


# POST and GET methods for edit article view
@app.route("/edit/<event_id>", methods=["GET", "POST"])
def edit_update(event_id):
    if request.method == "POST":
        CreateNewJC().edition(event_id)
    return redirect(url_for('events'))


# Route to delete an article with dynamic variable event_id
@app.route("/delete/<event_id>")
def delete(event_id):
    CreateNewJC().delete(event_id)
    return redirect(url_for('events'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
