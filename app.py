import csv
import json
from bs4 import BeautifulSoup
import time
import requests
from flask import Flask, jsonify, render_template

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    time.sleep(1)
    return soup

#聯合新聞網
def udn_news():
    #社會
    url = "https://udn.com/news/cate/2/6639"
    soup = get_soup(url)
    news = soup.select("section.thumb-news .story-list__holder .story-list__news")
    data = []
    for item in news[:6]:
        title = item.find('h3').get_text(strip=True)
        time = item.select_one('.story-list__time').get_text(strip=True)
        link = item.find('a')['href']
        entry = {
            "title": title,
            "time": time,
            "link": "https://udn.com" + link
        }
        data.append(entry)
    return data

#自由電子報
def itn_news():
    url = "https://news.ltn.com.tw/list/breakingnews/society"
    soup = get_soup(url)
    news = soup.select(".Listswiper-container .swiper-wrapper a")
    data = []
    for item in news:
        title = item.find('h3').get_text(strip=True)
        link = item['href']
        entry = {
            "title": title,
            "time": None,
            "link": link
        }
        data.append(entry)
    return data

#蘋果新聞網
def apple_news():
    url = "https://tw.nextapple.com/realtime/local"
    soup = get_soup(url)
    news = soup.select("article.post-style3.postCount")
    data = []
    for item in news[:8]:
        title = item.find('h3').get_text(strip=True)
        time = item.find('time').get_text(strip=True)
        link = item.find('a')['href']
        entry = {
            "title": title,
            "time": time,
            "link": link
        }
        data.append(entry)
    return data

#三立新聞網
def setn_news():
    url = "https://www.setn.com/catalog.aspx?pagegroupid=41"
    soup = get_soup(url)
    news = soup.select(".focus_news #owl-demo .item")
    data = []
    for item in news:
        title = item.select('.captionText strong')[0].text
        link = item.find('a')['href']
        entry = {
            "title": title,
            "time": None,
            "link": "https://www.setn.com" + link
        }
        data.append(entry)
    return data


app = Flask(__name__)
@app.route("/")
def index():
    udn = udn_news()
    itn = itn_news()
    apple = apple_news()
    setn = setn_news()
    news_data = {
        "society": {
            "udn": udn,
            "itn": itn,
            "apple": apple,
            "setn": setn
        },
        "political": {
            "udn": udn,
            "itn": itn,
            "apple": apple,
            "setn": setn
        },
        "international": {
            "udn": udn,
            "itn": itn,
            "apple": apple,
            "setn": setn
        },
        "lifestyle": {
            "udn": udn,
            "itn": itn,
            "apple": apple,
            "setn": setn
        }

    }

    media_categories = {
        "society": "社會",
        "political": "政治",
        "international": "國際",
        "lifestyle": "生活"
    }
    media_titles = {
        "udn": "聯合新聞網",
        "itn": "自由電子報",
        "apple": "蘋果新聞網",
        "setn": "三立新聞網"
    }
    return render_template("index.html", news=news_data, media_titles=media_titles, media_categories=media_categories)

if __name__ == "__main__":
    app.run(debug=True)