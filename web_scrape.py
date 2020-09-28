# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
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
news_soup = bs(html, "html.parser")

# creating searches for the html to get the new title and article content.
news_title = news_soup.body.find("div", class_= "bottom_gradient").get_text()
news_content = news_soup.body.find("div", class_= "article_teaser_body").get_text()

print(news_title)
print("---------------------------------------")
print(news_content)

jpl_nasa_url = "https://www.jpl.nasa.gov"
images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(images_url)
html = browser.html
images_soup = bs(html, "html.parser")

relative_image_path = images_soup.find_all('img')[3]["src"]
featured_image_url = jpl_nasa_url + relative_image_path
print(featured_image_url)

mars_weather_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(mars_weather_url)
mars_weather_html = browser.html
weather_soup = bs(mars_weather_html, "html.parser")

mars_weather = weather_soup.find("span", class_= "css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0").get_text()
mars_weather

mars_facts_url = "https://space-facts.com/mars/"
mars_facts = pd.read_html(mars_facts_url)
mars_facts