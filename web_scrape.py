# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path)

news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)
html = browser.html
news_soup = BeautifulSoup(html, "html.parser")