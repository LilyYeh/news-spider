from bs4 import BeautifulSoup
import requests

#中時新聞網
def chinatimes():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "zh-TW,zh;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://www.chinatimes.com/",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache"
    }
    url = 'https://www.chinatimes.com/society/?chdtv'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    news = soup.select(".column-left .article-list > ul > li")
    data = []
    for idx, item in enumerate(news, start=1):
        h3 = item.find("h3")
        if h3 is None:
            continue

        title = h3.get_text(strip=True)
        link = h3.find("a")['href']
        time = item.find("time")['datetime']
        entry = {
            "title": title,
            "time": time,
            "link": link
        }
        data.append(entry)
    print(data)
    return data

chinatimes()