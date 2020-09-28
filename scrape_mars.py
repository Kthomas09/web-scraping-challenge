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

mars_facts_url = "https://space-facts.com/mars/"
mars_facts = pd.read_html(mars_facts_url)
mars_facts

mars_facts_df = mars_facts[2]
mars_facts_df.columns = ["Description", "Values"]
mars_facts_df

mars_html = mars_facts_df.to_html()
mars_html.replace("\n", " ")
print(mars_html)

usgs_url = "https://astrogeology.usgs.gov"
hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemisphere_url)
hemisphere_html = browser.html
hemisphere_soup = bs(hemisphere_html, "html.parser")

hemisphere_items = hemisphere_soup.find_all("div", class_="item")

image_urls =[]

for i in hemisphere_items:
    title = i.find("h3").text
    img_url_1 = i.find("a", class_="itemLink product-item")["href"]
    browser.visit(usgs_url+img_url_1)
    img_html = browser.html
    img_soup = bs(img_html, "html.parser")
    img_url_2 = usgs_url + img_soup.find("img", class_="wide-image")["src"]
    image_urls.append({"title": title, "img_url":img_url_2})
    
image_urls