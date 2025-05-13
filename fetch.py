from bs4 import BeautifulSoup
import requests
import time

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    time.sleep(random.uniform(0.5, 1.0))
    return soup