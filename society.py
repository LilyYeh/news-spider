from bs4 import BeautifulSoup
import requests

def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

#聯合新聞網
def udn_news():
    #社會
    url = "https://udn.com/news/cate/2/6639"
    soup = get_soup(url)
    news = soup.select("section.thumb-news .story-list__holder .story-list__news")
    for item in news[:6]:
        title = item.find('h3').get_text(strip=True)
        time = item.select_one('.story-list__time').get_text(strip=True)
        href = item.find('a')['href']
        print(title, time, "https://udn.com" + href)

#自由電子報
def itn():
    url = "https://news.ltn.com.tw/list/breakingnews/society"
    soup = get_soup(url)
    news = soup.select(".Listswiper-container .swiper-wrapper a")
    for item in news:
        title = item.find('h3').get_text(strip=True)
        href = item['href']
        print(title, href)

#蘋果新聞網
def apple():
    url = "https://tw.nextapple.com/realtime/local"
    soup = get_soup(url)
    news = soup.select("article.post-style3.postCount")
    for item in news[:8]:
        title = item.find('h3').get_text(strip=True)
        time = item.find('time').get_text(strip=True)
        href = item.find('a')['href']
        print(title,time, href)

#三立新聞網
def setn():
    url = "https://www.setn.com/catalog.aspx?pagegroupid=41"
    soup = get_soup(url)
    news = soup.select(".focus_news #owl-demo .item")
    for item in news:
        title = item.select('.captionText strong')[0].text
        href = item.find('a')['href']
        print(title, 'https://www.setn.com' + href)

print('### 聯合新聞網 ###')
udn_news()

print('### 自由電子報 ###')
itn()

print('### 蘋果新聞網 ###')
apple()

print('### 三立新聞網 ###')
setn()