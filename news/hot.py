from const import urls
import fetch
import func
import requests
import datetime
import sys

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

def yahoo_more():
    url = "https://tw.news.yahoo.com/_td-news/api/resource?bkt=t3-pc-twnews-article-seamless&crumb=raicEof6JlA&device=desktop&ecma=modern&feature=oathPlayer%2CenableEvPlayer%2CenableGAMAds%2CenableGAMEdgeToEdge%2CvideoDocking&intl=tw&lang=zh-Hant-TW&partner=none&prid=2f5mtulk27reu&region=TW&site=news&tz=Asia%2FTaipei&ver=2.3.3008"

    headers = {
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Origin": "https://tw.news.yahoo.com",
        "Referer": "https://tw.news.yahoo.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "X-Webp": "1",
    }


    payload = {"requests":{"g0":{"resource":"StreamService","operation":"read","params":{"ui":{"comments":True,"editorial_featured_count":1,"image_quality_override":True,"link_out_allowed":True,"ntk_bypassA3c":True,"pubtime_maxage":0,"relative_links":True,"show_comment_count":True,"smart_crop":True,"storyline_count":2,"storyline_min":2,"summary":True,"thumbnail_size":100,"view":"mega","editorial_content_count":0,"finance_upsell_threshold":4},"forceJpg":True,"releasesParams":{"limit":20,"offset":0},"ncpParams":{"query":{"adsSlotsEnabled":True,"namespace":"abu","id":"main-stream","clientId":"abu-web","configId":"popular"},"body":{"gqlVariables":{"main":{"pagination":{"requestedCount":20,"contentOverrides":{},"remainingCount":150,"geminiToken":"{\"adsStartIndex\":\"2\"}","uuids":"b2359b28-e727-38d3-8c5a-72f3144c1bce:STORY,b18e6288-8352-31b7-ba96-5bd1265ef1cb:STORY,d8ff3a2e-61fd-3978-b3d2-21b3ce3ab5c3:STORY,6dbdf88d-c9e9-42bf-89fa-0ff85c086a65:STORY,a93b476e-4d48-4496-9965-cb40a6ae5f9e:STORY,47056943-86c0-388e-9a59-71285b9bb1ea:STORY,2c8ae9b7-efa2-371d-8978-78bb641217f3:STORY,fe2bbe91-2943-33a1-b2a7-380a20220d34:STORY,9b954478-d761-3675-b7b8-a48270286055:STORY,2987f8b0-8e68-310a-b554-77caeb099a19:STORY,689b6730-8665-3e2e-a860-fc220d0730e2:STORY,107bc7ac-6fad-48da-9da6-ed31bd500e00:STORY,e17b700d-1471-3f70-9815-abf18b28bb51:STORY,621be38b-d464-318d-a4c0-b60b14fcc6ce:VIDEO,a86e90df-2791-3826-8ec8-226ca59e9cd2:STORY,f6519d85-04bc-36ea-a958-80dbcd4f6f78:STORY,dfab079c-9637-3512-81e5-a544531e21d4:VIDEO,f5b7ffc9-d435-49b0-b6bc-6977a347a8d7:STORY,8d2307b6-7def-3dc3-8c56-23a6e27f0493:STORY,10eb8a4d-e4df-354a-be92-89053132a48b:STORY,6bc7e649-9941-38fb-81dd-6b673b17a959:STORY,916b6f7a-4615-39aa-b02e-34b726b0b79f:STORY,5b00d264-cadd-360b-8c57-7d7d45281534:STORY,cc9e9e3d-890a-39a6-b9e2-b32cbe31434e:STORY,2569dbdb-12bf-30be-a720-c705aa2a8585:STORY,e2cde595-be12-3650-9388-fcaf02db6de7:STORY,e38638d5-04ea-4975-bc0a-f5a1d577d0b6:STORY,cf11a6ea-176a-3437-932f-2826f22716e9:STORY,18e36bbe-45eb-3948-92b8-7542b8519c8f:STORY,fec0789c-2b4a-43bb-a4a1-50a86790f019:STORY,c476b338-9cbd-39ed-84e8-a06ecb825c0d:STORY,0af5d034-17e3-39e1-9c02-ff764be7d600:STORY,f525abba-acdc-3287-9382-68be781fdbc1:VIDEO,a056ae66-9e6c-3af3-89e7-c9bfad6e5f3a:STORY,379ce7d2-a8a9-3c21-8a61-9864ce32d85f:STORY,61c921ee-bc42-36b2-8f4b-e1180bdc989d:STORY,d036d9d3-0123-37cd-954f-2bb5ab13cccb:STORY,4e267eee-8f3e-3b7c-ad4f-496e5511a9e2:STORY,043c3bee-b871-3061-b2a8-1b5f2e32e88c:STORY,962772c9-eb59-3a87-aeea-703811cdf2c7:STORY,8c2be1e8-fb6d-312e-971c-5b6611721959:STORY,5b41f45a-9625-47ad-98e9-3c34be9544f1:STORY,37b15f4f-ab0a-4a07-a6d2-976128a3ec15:STORY,19627015-ede3-44c3-b9c1-14affff63f6c:STORY,2e4065c3-c501-3058-bce9-cb72995699cb:STORY,72825a1c-32c7-369d-93d2-11400754627e:STORY,70a3eacb-44a6-3de7-bd98-312d1bcf602a:STORY,bd99878a-3ae9-3b0a-84cc-2c3f9f272db3:STORY,e5ab5388-e94a-4c84-8130-16060a62172e:STORY,10109469-56ce-30fc-b280-dac9a5c57a68:STORY,08e8dc25-8ba1-3e7b-b13c-738ab6c1c9d9:STORY,84c5aa26-b1db-3358-a3f9-b9d483602e28:STORY,72ca3b96-00c5-4ac5-858f-126c3e0df012:STORY,a6822f90-9a2b-3207-9052-af55f8688858:STORY,383adedf-bc5a-32f3-891c-f1f9f3e8222b:STORY,1d2e0b25-8aa4-3b51-a8c5-daffb44b0c18:STORY,9ce4f11e-e867-35b7-bfb2-df110a0cebbb:STORY,8c5e9ed0-722d-4fd0-99c3-01804389a644:STORY,5df691ca-b37a-318e-8b51-be0a1ecd0c36:VIDEO,f11c92b1-a692-3187-a300-1353ce9ba8cf:STORY,089b709a-1151-336c-af18-04e69cd7d9f4:STORY,00c91c0d-748f-390e-9ea9-f059a7710ffe:STORY,40d70b50-1ac2-37cb-a1cf-0ec1d4e21c2b:STORY,ab18edaa-18b4-3003-bfdd-c333064ffa32:STORY,af769a2d-93c8-3a70-96d3-bbfa3e07f437:STORY,69282d59-9d70-48d7-8068-eabb217e68e7:STORY,f4ad76f2-e283-376d-8622-96fbe713e576:STORY,09bcc6ff-d8a7-3d9c-8c54-5083274ed97a:STORY,58ca42d5-00b9-4aff-a73c-db515112d2ea:STORY,d97df273-0e1d-3215-adf1-2fa6ea7d0b57:STORY,e687d810-11f7-3821-ad1f-a98c70a2ecac:STORY,f369ea94-88a3-341a-8455-4fca83a4b776:STORY,a85e8e56-1e51-3dd9-8c33-43da1e54eb57:STORY,81d7e1f6-3b7b-3802-b044-0e3239eb4dfd:STORY,6b797e39-d14b-4307-974b-29c81d2b066a:STORY,2b42caae-7375-356e-9401-5f81ef5796ea:VIDEO,ca26332f-00f5-3d9e-a6ef-5a431fca2243:STORY,e37a26c7-bdbe-4773-9aa2-7fd7ee00607b:STORY,76e3950d-5756-3076-8708-d7f42967764e:STORY,0ef92bc8-68cd-38d3-839c-226b9da37526:STORY,7bcd5cae-8d5d-3e5f-9ed3-d9ebc07a3eb3:STORY,e0e777d3-aca9-386f-95ce-a4d5b0c19fd8:STORY,1e3f88bc-9ead-3f93-8f57-fdce48866c6a:STORY,5c208b42-4097-359c-82cc-214c113adc5d:STORY,df3caa05-5054-3ed0-a181-26f461587422:VIDEO,e0e336f3-ff67-3efc-b7d7-2b77e041e3b5:STORY,b2818b2e-17a8-4a19-a7d4-4c0d41511035:STORY,9685935b-3f7f-31eb-979c-c0e20575725a:STORY,37ef15b3-824b-3f05-a78a-e30a548ff1f1:STORY,506b4e3a-38ca-33b2-96df-24f26ef7b059:STORY,0c1c84ea-8bf0-3cff-98dd-319fd156a33d:STORY,d2ce431f-f5d2-32d3-9ede-0e5f7f079004:STORY,51e70c5e-cf9a-38db-ba7d-28b94f431352:STORY,07b9ce40-ff57-4d80-8ca3-d41389f2d753:STORY,ee6077ff-bdcb-39b2-890c-715f7183030e:STORY,c13fae27-4c63-3c03-a48c-b25128e7eb44:STORY,af06ad59-4f72-30f2-98ec-71e6fe91d88e:STORY,7840cbc1-c94e-3836-b653-38e40fcaa180:STORY,1d048a55-33c1-38bb-8fe2-f2cd647aec67:VIDEO,069223e8-4e1c-317f-a8f2-e70370546e81:STORY,c6f294bd-2091-3af0-9c0f-99e1dff05c1b:STORY,f8acda6b-ef02-408b-a3d2-3d58b75137ae:STORY,3cab6608-d187-4fdb-be25-1df8aa82bf6a:STORY,91e93c18-2fd0-34d4-92de-0c70b2f0b968:STORY,d2cf1a89-09ac-3662-b27e-d368646c1cc8:STORY,81aac582-f65e-33c7-81dd-aba2681bcd18:STORY,3bbbf912-006a-32b7-b29d-cf90847f6bb6:STORY,d486dac4-e3fb-3053-8d1d-4efe959b4936:STORY,d77cdd2b-8fea-37e1-95d0-90036568a788:STORY,20e3fcd7-3e89-3fcc-b503-85c1e7b772b4:STORY,ea463cd6-a992-3db8-8ac8-9b16d5d88248:STORY,28653e05-a112-33f5-a512-838d0cd76431:STORY,e4567e15-54ee-3a91-a5f6-3b8499282fd9:STORY,0d201b73-c2ee-3a32-99b9-e423d9ed7883:STORY,eb614502-06e4-3e19-b0e9-cf75c209b253:STORY,ca4e84dd-2c10-3c34-bc93-7a9cba3fe879:STORY,7054b8cc-e200-3b63-882c-1fbeadaf20ce:VIDEO,c9887d68-0044-3666-b9c3-7b293f3e375f:STORY,815e2047-1b42-3ca6-a6fa-55ee70489d1a:STORY,499a83fd-2475-3eb4-b2bb-0d8f488fbb9f:STORY,bf9b961c-108d-3cf9-9bd2-69c45ac657fe:STORY,46fbf57a-b013-336e-840d-df33fec2aa65:STORY,6118260c-9247-362e-b17c-e718cb9edadd:STORY,d71b2bb8-4625-389d-9363-c63499aa803e:STORY,ea94f2c2-81cc-3354-86d3-be4d2ced6507:STORY,1859f656-5042-4664-8413-33750f262f76:STORY,00ffad1d-a389-3b2a-a900-2493a320089e:STORY,534bbfa2-aef3-352a-8d22-fa5f87d0d833:STORY,71dc31f4-1075-37b7-8370-b4ece26cbc4e:STORY,aa2d4f84-5afd-3329-a69c-af7f5a384af2:STORY,b573859d-532e-3fd9-8bb5-efc98e5cd996:STORY,8576ff80-338d-3cd1-b331-0685dc5e5280:STORY,bb071a40-6bcb-33c2-b505-5fdefbc87121:STORY,cc8b04c0-9b3d-3171-a9f8-a1cca5d70a4f:STORY,e19ed54f-383b-38ef-bd14-d2b4e911a304:STORY,b313816c-f478-395b-8c9d-d15947419cb0:STORY,c51db397-7540-39df-b797-9b95253d3bef:STORY,1de9f54f-cc4e-3854-91fc-ca88c1fb22ed:VIDEO,210c1060-52df-3877-a746-92b35f002d62:STORY,e8590cbd-0df1-3ba5-a906-4f807d85b3aa:STORY,b76ed117-40d2-3b72-a410-675e8caf5ef8:STORY,f148f815-4764-328d-81be-1374131eea3f:STORY,9ff0fe9b-d3a1-3e9f-a736-41e46c2ff76d:STORY,df5c6093-a817-3657-a766-f00e68c81559:STORY,1aa76f1c-ae44-47a8-94e5-d89845e9befa:STORY,3aedd3e7-a721-354b-898a-302768fea3ad:STORY,ff6b9526-0fea-3391-9787-5f478cf2240d:STORY,bfba06f9-0ab2-38d3-a5ba-4bb859d16e4f:STORY,dc87c18e-24df-32ec-8640-c7224b17ed1d:VIDEO,965ab0ec-65a8-3712-89a4-88c92bbfbe18:VIDEO"}}}}},"offnet":{"include_lcp":True},"use_content_site":True,"useNCP":True,"ads":{"ad_polices":True,"contentType":"video/mp4,application/x-shockwave-flash","count":25,"frequency":3,"inline_video":True,"pu":"https://tw.news.yahoo.com","se":5419954,"spaceid":2144404979,"start_index":1,"timeout":450,"type":"STRM","useHqImg":True,"useResizedImages":True,"enableTaboolaAds":True,"taboolaConfig":{"mode":"stream-twhk-news-a","placement":"taboola-stream","region":"index","targetType":"mix"}},"batches":{"pagination":True,"size":20,"timeout":1300,"total":170},"enableAuthorBio":True,"max_exclude":0,"min_count":3,"service":{"specRetry":{"enabled":False}},"category":"","pageContext":{"site":"news","section":"most-popular","topic":"default","electionPageType":"default","electionTvType":"default","pageType":"minihome","renderTarget":"default"},"content_type":"subsection"}}},"context":{"feature":"oathPlayer,enableEvPlayer,enableGAMAds,enableGAMEdgeToEdge,videoDocking","bkt":"t3-pc-twnews-article-seamless","crumb":"raicEof6JlA","device":"desktop","intl":"tw","lang":"zh-Hant-TW","partner":"none","prid":"7bkmr0dk27vhg","region":"TW","site":"news","tz":"Asia/Taipei","ver":"2.3.3008","ecma":"modern"}}

    response = requests.post(url, headers=headers, json=payload)

    try:
        result = response.json()
    except:
        return None

    news = result["g0"]["data"]["stream_items"]
    data = []
    for item in news:
        if item["type"] != 'article':
            continue
        title = item['title']
        link = item['url']

        timestamp_ms = item['pubtime']
        dt = datetime.datetime.fromtimestamp(timestamp_ms / 1000)
        time = dt.strftime("%Y/%m/%d %H:%M")

        source = item['publisher']
        entry = {
            "title": title,
            "link": link,
            "time": time,
            "source": source
        }
        data.append(entry)
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
    more_data = yahoo_more()
    if more_data:
        data = data + more_data
    return data


