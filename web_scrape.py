from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
import requests
import pymongo

def init_browser():
    execute_path = {"execute_path": "chromedriver.exe"}
    return Browser ("chrome", **execute_path, headless = False)