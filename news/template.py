import sys

from const import urls
import fetch
import func
import requests

#聯合新聞網
def udn(type):
    soup = fetch.get_soup(urls.udn[type])
    news1 = soup.select("section.thumb-news .story-list__holder .story-list__news")
    data = []
    for item in news1[:6]:
        title = item.find('h3').get_text(strip=True)
        time = item.select_one('.story-list__time').get_text(strip=True)
        link = item.find('a')['href']
        entry = {
            "title": title,
            "time": func.time_format(time),
            "link": "https://udn.com" + link
        }
        data.append(entry)

    r = requests.get(urls.udn[type + '_api'])
    news2 = r.json().get("lists", [])
    for item in news2[:2]:
        entry = {
            "title": item.get('title'),
            "time": func.time_format(item.get("time", {}).get("date", "")),
            "link": "https://udn.com" + item.get("titleLink", "")
        }
        data.append(entry)
    return data

#自由電子報
def itn(type):
    soup = fetch.get_soup(urls.itn[type])
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
def apple(type):
    soup = fetch.get_soup(urls.apple[type])
    news = soup.select("article.post-style3.postCount")
    data = []
    for item in news[:8]:
        title = item.find('h3').get_text(strip=True)
        time = item.find('time').get_text(strip=True)
        link = item.find('a')['href']
        entry = {
            "title": title,
            "time": func.time_format(time),
            "link": link
        }
        data.append(entry)
    return data

#三立新聞網
def setn(type):
    soup = fetch.get_soup(urls.setn[type])
    news = soup.select(".focus_news #owl-demo .item .captionText a")
    data = []
    for item in news:
        title = item.find('strong').get_text(strip=True)
        link = item['href']
        entry = {
            "title": title,
            "time": None,
            "link": urls.setn['top'] + link
        }
        data.append(entry)
    return data

#ETtoday
def ettoday(type):
    soup = fetch.get_soup(urls.ettoday[type])
    news = soup.select(".part_area_1 .part_pictxt_7 .piece")
    data = []
    for item in news:
        title = item.find('h3').get_text(strip=True)
        link = item.find('a')['href']
        time = item.select_one('.date').get_text(strip=True)
        entry = {
            "title": title,
            "time": time,
            "link": link
        }
        data.append(entry)

    news = soup.select(".part_area_1 .part_list_3 h3")
    for item in news:
        if item.find('a') is None:
            continue
        title = item.find('a')['title']
        link = item.find('a')['href']

        time = None
        if item.select_one('.date') is not None:
            time = item.select_one('.date').get_text(strip=True)
        entry = {
            "title": title,
            "time": time,
            "link": link
        }
        data.append(entry)

    news = soup.select(".part_pictxt_3 .piece")
    for item in news[:4]:
        title = item.find('h3').get_text(strip=True)
        link = item.find('a')['href']
        time = item.select_one('.date').get_text(strip=True)
        entry = {
            "title": title,
            "time": time,
            "link": link
        }
        data.append(entry)

    return data