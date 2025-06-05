from const import urls
import fetch
import func
import sys
from playwright.sync_api import sync_playwright
import time

type = 'hot'

#聯合新聞網
def udn():
    soup = fetch.get_soup(urls.udn['hot'])
    news = soup.select("section.thumb-news .story-list__holder .story-list__news")
    data = []
    for item in news:
        title = item.find('h2').get_text(strip=True)
        time = item.select_one('.story-list__time').get_text(strip=True)
        link = item.select_one('h2 a')['href']
        label = item.select_one('.story-list__info > a')
        tag = {
            'text': label.get_text(strip=True),
            'link': label['href']
        }
        entry = {
            "title": title,
            "time": func.time_format(time),
            "link": link,
            "tag": tag
        }
        data.append(entry)
    return data

#自由電子報
def itn():
    soup = fetch.get_soup(urls.itn['hot'])
    news1 = soup.select(".Listswiper-container .swiper-wrapper a")
    data = []
    for item in news1:
        title = item.find('h3').get_text(strip=True)
        link = item['href']
        entry = {
            "title": title,
            "time": None,
            "link": link
        }
        data.append(entry)

    news2 = soup.select('.whitecon ul.list li')
    for item in news2:
        title = item.find('h3').get_text(strip=True)
        time = item.select_one('.time').get_text(strip=True)
        link = item.find('a')['href']
        entry = {
            "title": title,
            "time": func.time_format(time),
            "link": link
        }
        data.append(entry)
    return data

#蘋果新聞網
def apple():
    soup = fetch.get_soup(urls.apple['hot'])
    news = soup.select("article.post-style3.postCount")
    data = []
    for item in news:
        title = item.find('h3').get_text(strip=True)
        time = item.find('time').get_text(strip=True)
        link = item.select_one('h3 a')['href']
        label = item.select_one('.post-meta .category')
        tag = {
            'text': label.get_text(strip=True),
            'link': None
        }
        entry = {
            "title": title,
            "time": func.time_format(time),
            "link": link,
            "tag": tag
        }
        data.append(entry)
    return data

#三立新聞網
def setn():
    soup = fetch.get_soup(urls.setn['hot'])
    news = soup.select("#NewsList .newsItems")
    data = []
    for item in news[:20]:
        title = item.find('h3').get_text(strip=True)
        time = item.find('time').get_text(strip=True)
        link = item.select_one('h3 a')['href']
        label = item.select_one('.newslabel-tab a')
        label_text = label.get_text(strip=True)
        if label_text == '娛樂':
            label_link = "https://star.setn.com"
        else:
            label_link = "https://www.setn.com/ViewAll.aspx" + label["href"]
        tag = {
            "text": label_text,
            "link": label_link
        }
        entry = {
            "title": title,
            "time": func.time_format(time),
            "link": "https://www.setn.com" + link,
            "tag": tag
        }
        data.append(entry)
    return data

#TVBS
def tvbs():
    soup = fetch.get_soup(urls.tvbs['hot'])
    news = soup.select("li")
    data = []
    cnt = 0
    for item in news:
        h2 = item.select_one('a h2')
        if not h2:
            continue
        title = h2.get_text(strip=True)
        link = item.find('a')['href']
        tag = {
            "text": item.select('a')[1].text,
            "link": urls.tvbs['top'] + item.select('a')[1]["href"]
        }
        entry = {
            "title": title,
            "time": None,
            "link": urls.tvbs['top'] + link,
            "tag": tag
        }
        data.append(entry)

        cnt+=1
        if cnt == 20:
            break
    return data

def yahoo():
    soup = fetch.get_soup(urls.yahoo['hot'])
    news = soup.select("#YDC-Stream .js-stream-content")
    data = []
    for item in news:
        title = item.find('h3').get_text(strip=True)
        link = item.select_one('h3 a')['href']
        target = item.select_one('.Cf > div:nth-child(1) > div img')
        if target:
            target = item.select_one('.Cf > div:nth-child(2) > div')
        else:
            target = item.select_one('.Cf > div:nth-child(1) > div')
        source = target.get_text(strip=True) if target else None
        entry = {
            "title": title,
            "link": urls.yahoo['top'] + link,
            "source": source
        }
        data.append(entry)
    return data

def yahoo_more():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # 設定 True 就是無頭模式
        page = browser.new_page()
        page.goto('https://tw.news.yahoo.com/most-popular', wait_until="domcontentloaded")

        # 滾動觸發載入更多
        page.mouse.wheel(0, 3000)
        time.sleep(1)  # 等待新資料出現

        # 抓 news
        news = page.query_selector_all("li.js-stream-content")

        # 抓第 1～25 個
        data = []
        for idx, item in enumerate(news[:25], start=1):
            h3 = item.query_selector("h3")
            if h3 is None:
                continue

            title = h3.inner_text()

            a_tag = h3.query_selector("a")
            link = None
            if a_tag:
                link = a_tag.get_attribute("href")

            target = item.query_selector('.Cf > div:nth-child(1) > div img')
            if target:
                target = item.query_selector('.Cf > div:nth-child(2) > div')
            else:
                target = item.query_selector('.Cf > div:nth-child(1) > div')
            source = target.inner_text().replace("•", " • ") if target else None

            entry = {
                "title": title,
                "link": urls.yahoo['top'] + link,
                "source": source
            }
            data.append(entry)
        browser.close()
    return data

#ETtoday
def ettoday():
    soup = fetch.get_soup(urls.ettoday[type])
    news = soup.select(".part_pictxt_3 .piece")
    data = []
    for item in news[:8]:
        title = item.find('h3').get_text(strip=True)
        link = item.find('a')['href']
        time = item.select_one('.date').get_text(strip=True)
        entry = {
            "title": title,
            "time": func.time_format(time),
            "link": link
        }
        data.append(entry)

    return data

