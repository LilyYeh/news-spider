from const import urls
import fetch
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