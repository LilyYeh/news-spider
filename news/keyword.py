from const import urls
import fetch
import re
import json
from playwright.sync_api import sync_playwright
import sys

#聯合新聞網
def udn():
    soup = fetch.get_soup(urls.udn['top'])
    tags = soup.select("section.navigation-wrapper .navigation--simple")

    if tags is None:
        return None

    data = []
    for tag in tags:
        title = tag.get_text(strip=True)
        link = tag['href']
        entry = {
            "title": title,
            "link": link
        }
        data.append(entry)

    keywords = soup.select("section.keywords a")
    if keywords is None:
        return data
    for keyword in keywords:
        title = keyword.get_text(strip=True)
        link = keyword['href']
        entry = {
            "title": title,
            "link": link if re.match(r'^https', link) else "https://udn.com" + link
        }
        data.append(entry)

    return data

#自由電子報
def itn():
    soup = fetch.get_soup(urls.itn['top'])

    hot_keywords_block = soup.find('div', id='hot_keyword_area')
    scripts = hot_keywords_block.find_all('script')

    keywords = None
    for script in scripts:
        if 'hot_keyword_words' in script.text:
            match = re.search(r'var\s+hot_keyword_words\s*=\s*(\[.*?\]);', script.text, re.DOTALL)
            if match:
                json_text = match.group(1)
                keywords = json.loads(json_text)
                break

    if keywords is None:
        return None

    data = []
    for keyword in keywords:
        title = keyword['text']
        link = keyword['link']['href']
        entry = {
            "title": title,
            "link": link
        }
        data.append(entry)

    return data

#三立新聞網
def setn():
    soup = fetch.get_soup(urls.setn['top'])
    news = soup.select("#mainMenu li")
    data = []
    start = False
    for item in news:
        title = item.find('a').get_text(strip=True)
        if title == '新聞':
            break

        if start == True:
            entry = {
                "title": title,
                "link": item.find('a')['href']
            }
            data.append(entry)

        if title == '即時':
            start = True
    return data

#TVBS
def tvbs():
    soup = fetch.get_soup(urls.tvbs['top'])
    news = soup.select("#pc2 li")
    data = []
    start = False
    for item in news:
        title = item.find('a').get_text(strip=True)
        if title == '即時':
            break

        if start == True:
            entry = {
                "title": title,
                "link": urls.tvbs['top'] + item.find('a')['href']
            }
            data.append(entry)

        if title == '首頁':
            start = True
    return data

#中時新聞網
def chinatimes():
    soup = fetch.get_soup_with_header(urls.chinatimes['top'])
    news_list = soup.select_one("ul.main-nav-item-group")
    news = news_list.select("li.highlight.keyword")
    data = []
    for idx, item in enumerate(news, start=1):
        title = item.get_text(strip=True)
        link = item.find("a")['href']

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
        page.goto(urls.chinatimes['top'], wait_until="domcontentloaded")
        news_list = page.query_selector("ul.main-nav-item-group")
        news = news_list.query_selector_all("li.highlight.keyword")
        data = []
        for idx, item in enumerate(news, start=1):
            title = item.inner_text()
            link = item.query_selector("a").get_attribute("href")

            entry = {
                "title": title,
                "link": link
            }
            data.append(entry)
        browser.close()
    return data