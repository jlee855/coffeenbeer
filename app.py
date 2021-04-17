from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("localhost", 27017)
db = client.coffeenbeer


## HOME PAGE
@app.route('/')
def home():
    return render_template('home.html')

## FOR THINSG NOT DEVELOPED YET
@app.route('/under_construction')
def beer_home():
    return render_template('under_construction.html')

## COFFEE HOME PAGE
@app.route('/coffee_home')
def coffee_home():
    return render_template('coffee_home.html')


## COFFEE BRANDS HOME PAGE
@app.route('/coffee_home_brands')
def coffee_home_brands():
    return render_template('coffee_home_brands.html')


## COFFEE FLAVORS HOME PAGE
@app.route('/coffee_home_flavor')
def coffee_home_flavor():
    return render_template('under_construction.html')

## COFFEE COUNTRIES HOME PAGE
@app.route('/coffee_home_countries')
def coffee_home_country():
    return render_template('coffee_home_countries.html')


## COFFEE LISTINGS POST
@app.route('/coffee_listing', methods = ["POST"])
def coffee_listing_post():
    return render_template('coffee_listing.html')

## COFFEE LISTINGS GET (NEED WORK FOR FLAVOR & KINDS)
@app.route('/coffee_listing', methods = ["GET"])
def coffee_listing_get():
    if request.args.get('country') == None:
        brand = request.args.get('brand')
        coffee_info = db.coffee_info.find({'brand': brand})
    elif request.args.get('brand') == None:
        country = request.args.get('country')
        coffee_info = list(db.coffee_info.find({'country': country}))
    if coffee_info == []:
        return render_template('coffee_doesnot_exist.html')
    return render_template('coffee_listing.html', data = coffee_info)

@app.route('/coffee_review', methods = ["GET"])
def coffee_review_get():
    return render_template('coffee_review.html')


@app.route('/coffee_review', methods = ["POST"])
def coffee_review_post():
    review = request.form['review']
    db.coffee_reviews.insert_one({'review': review})
    return jsonify({'result': 'success'})

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)
