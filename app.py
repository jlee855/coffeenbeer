from flask import Flask, render_template, request
from pymongo import MongoClient
import requests

app = Flask(__name__)
client = MongoClient("localhost", 27017)
db = client.coffenbeer

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/beer_home')
def beer_home():
    return render_template('beer_home.html')

@app.route('/coffee_home')
def coffee_home():
    return render_template('coffee_home.html')

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)
