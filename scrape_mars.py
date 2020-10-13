# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pymongo
import time
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import time

def init_browser():
    # launching chromedriver to automate the webscrape
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path)

def scrape():
# visiting the url and parsing the HTML
    browser = init_browser()
    mars_dict ={}
    
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    time.sleep(5)
    html = browser.html
    news_soup = bs(html, "html.parser")

    # creating searches for the html to get the new title and article content.
    news_title = news_soup.body.find("div", class_= "bottom_gradient").get_text()
    news_content = news_soup.body.find("div", class_= "article_teaser_body").get_text()

    # scraping the featured image of the Martian surface
    jpl_nasa_url = "https://www.jpl.nasa.gov"
    images_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(images_url)
    html = browser.html
    images_soup = bs(html, "html.parser")
    relative_image_path = images_soup.find_all('img')[3]["src"]
    featured_image_url = jpl_nasa_url + relative_image_path

    # scraping the martian facts
    mars_facts_url = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(mars_facts_url)
    mars_facts_df = mars_facts[2]
    mars_facts_df.columns = ["Description", "Values"]
    mars_html = mars_facts_df.to_html()
    mars_html.replace("\n", " ")

# Mars Hemispheres
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)
    time.sleep(2)
    links = browser.find_by_css("a.product-item h3")
# Retreive all items that contain Mars hemispheres information
    image_urls = []
    for i in range(len(links)):
        hemisphere = {}
        browser.find_by_css("a.product-item h3")[i].click()
        hemisphere["img_url"] = browser.find_by_text("Sample")["href"]
        hemisphere["title"] = browser.find_by_css("h2.title").text
        image_urls.append(hemisphere)
        browser.back()

    # creating a dictionary to store all the scraped data
    mars_dict = {
        "News_Title": news_title,
        "News_Article": news_content,
        "Featured_Image": featured_image_url,
        "Mars_Facts": str(mars_html),
        "Mars_Hemispheres": image_urls
    }

    browser.quit()
    
    return mars_dict

    
        
