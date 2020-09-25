from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import web_scrape

app = Flask (__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskapp"
mongo = PyMongo(app)
