from flask import Flask, render_template, request
from pymongo import MongoClient
import requests

app = Flask(__name__)
client = MongoClient("localhost", 27017)
db = client.coffenbeer

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/under_construction')
def beer_home():
    return render_template('under_construction.html')

@app.route('/coffee_home')
def coffee_home():
    return render_template('coffee_home.html')

@app.route('/coffee_home_brands')
def coffee_home_brands():
    return render_template('coffee_home_brands.html')

@app.route('/coffee_home_flavor')
def coffee_home_flavor():
    return render_template('coffee_home_flavor.html')

@app.route('/coffee_home_countries')
def coffee_home_country():
    return render_template('coffee_home_countries.html')

@app.route('/coffee_review')
def coffee_review():
    return render_template('coffee_review.html')

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)
