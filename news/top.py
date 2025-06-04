from const import urls
import fetch
import func
import re
import json
import demjson3
import sys

type = 'top'

#聯合新聞網
def udn():
    soup = fetch.get_soup(urls.udn[type])
    scripts = soup.find_all('script')
    js_code = None
    for script in scripts:
        if '__UDN__.newsLists' in script.text:
            js_code = script.string or script.text
            break
    pattern = r'__UDN__\.newsLists\s*=\s*(\[\s*.*?\s*\]);'
    match = re.search(pattern, js_code, re.DOTALL)
    js_array_str = match.group(1)
    news = demjson3.decode(js_array_str)
    data = []
    for item in news:
        if item.get('type') != 'picture':
            continue
        title = item['title']
        link = item['titleLink']
        entry = {
            "title": title,
            "link": link
        }
        data.append(entry)
    return data

#自由電子報
def itn():
    soup = fetch.get_soup(urls.itn[type])
    news = soup.select(".jumbotron .swiper-container .swiper-slide a")
    data = []
    for item in news:
        title = item.find('h2').get_text(strip=True)
        link = item['href']
        entry = {
            "title": title,
            "link": link
        }
        data.append(entry)
    return data

#蘋果新聞網
def apple():
    soup = fetch.get_soup(urls.apple[type])
    news = soup.select("#top-slider .swiper-wrapper .swiper-slide article.post-style1 a")
    data = []
    for item in news[:15]:
        title = item.find('h3').get_text(strip=True)
        link = item['href']
        label = item.select_one('.post-meta .category')
        tag = {
            'text': label.get_text(strip=True),
        }
        entry = {
            "title": title,
            "link": link,
            "tag": tag
        }
        data.append(entry)
    return data

#三立新聞網
def setn():
    soup = fetch.get_soup(urls.setn[type])
    news = soup.select(".focus_news #owl-demo .item .captionText a")
    data = []
    for item in news:
        title = item.find('strong').get_text(strip=True)
        link = item['href']
        entry = {
            "title": title,
            "link": urls.setn['top'] + link
        }
        data.append(entry)
    return data

#ETtoday
def ettoday():
    soup = fetch.get_soup(urls.ettoday[type])
    news = soup.select(".area_1 .piece") + soup.select(".area_2 .piece")

    data = []
    for item in news:
        if (item.find('a') is None):
            continue

        title = item.find('a')['title']
        link = item.find('a')['href']
        tag = None
        if item.select_one('.tag') is not None:
            tag = {
                'text': item.select_one('.tag').get_text(strip=True),
            }
        entry = {
            "title": title,
            "tag": tag,
            "link": link
        }
        data.append(entry)
    return data