from const import urls
import fetch
import re
import json
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