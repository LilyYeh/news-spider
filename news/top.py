from const import urls
import fetch
import re
import demjson3
import json
from playwright.sync_api import sync_playwright
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

#中時新聞網
def chinatimes():
    soup = fetch.get_soup_with_header(urls.chinatimes[type])
    scripts = soup.find_all('script')
    js_code = None
    for script in scripts:
        if 'var data = [' in script.text:
            js_code = script.string or script.text
            break
    pattern = r'data\s*=\s*(\[\s*.*?\s*\]);'
    match = re.search(pattern, js_code, re.DOTALL)
    js_array_str = match.group(1)
    js_array_str = re.sub(r'photoUrl\s*=\s*"', '"', js_array_str)
    js_array_str = re.sub(r'GetUrl_Cn\s*\(\s*"', '"', js_array_str)
    js_array_str = re.sub(r'"\s*\)', '"', js_array_str)
    js_array_str = js_array_str.replace('<br>', '')
    news = json.loads(js_array_str)
    data = []
    for item in news:
        title = item['captionTitle']
        link = item['linkUrl']
        entry = {
            "title": title,
            "link": link
        }
        data.append(entry)
    return data

def chinatimes_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars"
            ]
        )
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800},
            java_script_enabled=True
        )
        page.goto(urls.chinatimes[type], wait_until="domcontentloaded")
        news = page.query_selector_all("#news-pane-1-1 .latest-news > ul > li")
        for idx, item in enumerate(news, start=1):
            h4 = item.query_selector("h4")
            print(h4.inner_text())
        browser.close()