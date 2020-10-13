# Import Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# variable to run Flask
app = Flask (__name__)

# connecting Flask app to Mongodb
app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskapp"
mongo = PyMongo(app)

# home function for app to read into the Mars Dictionary in Data Base
@app.route("/")
def home():
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template("index.html", mars_dict = mars_dict)

# Function to initialize scrape
@app.route("/scrape")
def scrape():
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars.scrape()
    mars_dict.update({}, mars_data, upsert=True)
    return redirect("/", code = 302)

# Run flask app.
if __name__ == "__main__":
    app.run(debug=True)
