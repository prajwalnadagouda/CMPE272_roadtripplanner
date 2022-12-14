import time, threading
import database
import getevents
import getamusementparks 
import getmuseums
import getparks
import getrestaurants
import getfuelstations
from flask import Flask, render_template, request, jsonify
from fuelstations import fetch_fuelstations
from parks import fetch_parks
from amusementparks import fetch_amusement_parks
from flask_cors import CORS
from museums import fetch_museums
from restaurants import fetch_restaurants
from recommendations import fetch_recommendations

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'This Compose/Flask demo has been viewed time(s)'

# @app.route('/updatedatabase')
def update_database():
    print("i am here")
    database.database.update_database()
    threading.Timer(3600, database.database.update_database).start()


@app.route('/getevents',methods=['GET'])
def get_events():
    if request.method == 'GET':
        l1 = request.args.get('l1')
        l2 = request.args.get('l2')
        l3 = request.args.get('l3')
        l4 = request.args.get('l4')
        jdate = request.args.get('date')
        return getevents.display(l1,l2,l3,l4,jdate)

@app.route('/getamusementparks',methods=['GET'])
def rgetamusementparks():
    if request.method == 'GET':
        l1 = request.args.get('l1')
        l2 = request.args.get('l2')
        l3 = request.args.get('l3')
        l4 = request.args.get('l4')
        return getamusementparks.display(l1,l2,l3,l4)

@app.route('/getmuseums',methods=['GET'])
def rgetmuseums():
    if request.method == 'GET':
        l1 = request.args.get('l1')
        l2 = request.args.get('l2')
        l3 = request.args.get('l3')
        l4 = request.args.get('l4')
        return getmuseums.display(l1,l2,l3,l4)

@app.route('/getfuelstations',methods=['GET'])
def rgetfuelstations():
    if request.method == 'GET':
        l1 = request.args.get('l1')
        l2 = request.args.get('l2')
        l3 = request.args.get('l3')
        l4 = request.args.get('l4')
        return getfuelstations.display(l1,l2,l3,l4)

@app.route('/getrestaurants',methods=['GET'])
def rgetrestaurants():
    if request.method == 'GET':
        l1 = request.args.get('l1')
        l2 = request.args.get('l2')
        l3 = request.args.get('l3')
        l4 = request.args.get('l4')
        return getrestaurants.display(l1,l2,l3,l4)

@app.route('/getparks',methods=['GET'])
def rgetparks():
    if request.method == 'GET':
        l1 = request.args.get('l1')
        l2 = request.args.get('l2')
        l3 = request.args.get('l3')
        l4 = request.args.get('l4')
        return getparks.display(l1,l2,l3,l4)


# @app.route('/fuelstations')
# def fetch_fuelstation():
#     return fetch_fuelstations(self='')

# @app.route('/parks')
# def get_parks():
#     return fetch_parks()


# @app.route('/amusementparks')
# def get_amusement_parks():
#     return fetch_amusement_parks()

# @app.route('/museums')
# def get_museums():
#     return fetch_museums()

# @app.route('/restaurants')
# def get_restaurants():
#     return fetch_restaurants()

@app.route('/categories')
def get_categories():
    return jsonify(["Amusement Park", "National Park", "Concert", "Food", "Museum"])


@app.route('/recommendations')
def get_recommendations():
    return fetch_recommendations()



if __name__ == "__main__":
    update_database()
    fetch_fuelstations(self='')
    fetch_parks()
    fetch_amusement_parks()
    fetch_museums()
    fetch_restaurants()
    app.run(host="0.0.0.0", debug=True)
