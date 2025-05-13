from const import urls
import fetch
import func

#聯合新聞網
def udn():
    soup = fetch.get_soup(urls.udn['lifestyle'])
    news = soup.select("section.thumb-news .story-list__holder .story-list__news")
    data = []
    for item in news[:6]:
        title = item.find('h3').get_text(strip=True)
        time = item.select_one('.story-list__time').get_text(strip=True)
        link = item.find('a')['href']
        entry = {
            "title": title,
            "time": func.time_format(time),
            "link": "https://udn.com" + link
        }
        data.append(entry)
    return data

#自由電子報
def itn():
    soup = fetch.get_soup(urls.itn['lifestyle'])
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
def apple():
    soup = fetch.get_soup(urls.apple['lifestyle'])
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
def setn():
    soup = fetch.get_soup(urls.setn['lifestyle'])
    news = soup.select(".focus_news #owl-demo .item .captionText a")
    data = []
    for item in news:
        title = item.find('strong').get_text(strip=True)
        link = item['href']
        entry = {
            "title": title,
            "time": None,
            "link": "https://www.setn.com" + link
        }
        data.append(entry)
    return data