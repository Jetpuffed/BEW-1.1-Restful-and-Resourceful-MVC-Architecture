import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Reptimart')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
classifieds = db.classifieds
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/marketplace")
def marketplace():
    return render_template('marketplace.html', classifieds=classifieds.find())


@app.route("/marketplace/new")
def marketplace_new():
    return render_template('marketplace_new.html', listing={})


@app.route("/marketplace", methods=['POST'])
def marketplace_submit():
    listing = {
        'title': request.form.get('title'),
        'price': request.form.get('price'),
        'shipping': request.form.get('shipping'),
        'thumbnail': request.form.get('picture')
    }
    classifieds_id = classifieds.insert_one(listing).inserted_id
    return redirect(url_for('marketplace_view', classifieds_id=classifieds_id))


@app.route("/marketplace/<classifieds_id>")
def marketplace_view(classifieds_id):
    listing = classifieds.find_one({'_id': ObjectId(classifieds_id)})
    return render_template('marketplace_view.html', listing=listing)


@app.route('/marketplace/<classifieds_id>/edit')
def marketplace_edit(classifieds_id):
    listing = classifieds.find_one({'_id': ObjectId(classifieds_id)})
    return render_template('marketplace_new.html', listing=listing)


@app.route("/marketplace/<classifieds_id>/delete", methods=['POST'])
def marketplace_delete(classifieds_id):
    classifieds.delete_one({'_id': ObjectId(classifieds_id)})
    return redirect(url_for('marketplace'))


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/account")
def account():
    return render_template('account.html')
