from bs4 import BeautifulSoup
import requests
import time
import random

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    #time.sleep(random.uniform(0.5, 1.0))
    return soup

def get_soup_with_header(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "zh-TW,zh;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://www.chinatimes.com/",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache"
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup