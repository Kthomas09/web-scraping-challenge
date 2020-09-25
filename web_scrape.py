# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
import time
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# launching chromedriver to automate the webscrape
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path)

# visiting the url and parsing the HTML
news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)
time.sleep(5)
html = browser.html
news_soup = BeautifulSoup(html, "html.parser")

# creating searches for the html to get the new title and article content.
news_title = news_soup.body.find("div", class_= "content_title").get_text()
news_content = news_soup.body.find("div", class_= "article_teaser_body").get_text()