# import requests
# import json
# from bs4 import BeautifulSoup 
# URL = "https://1lib.in/s/dune/?extension=pdf"
# extensionLink = "https://1lib.in/"
# r = requests.get(URL) 
# soup = BeautifulSoup(r.content, 'html5lib')
# # s = soup.find_all('div', attrs={'class':'checkBookDownloaded itemCoverWrapper'}) 
# # o = soup.find_all('h3', attrs={'itemprop':'name'})
# # print(o)
# # for i in s:
# #     book = {}
# #     book["image"] = s
# # print(extensionLink+s[0].a.text)
# # print(s[0].img['data-src'])

# bookCounter = soup.find_all('div',attrs={'class':'resItemBox resItemBoxBooks exactMatch'}) #list
# bookImage = bookCounter[0].td.img['data-src']
# bookName = bookCounter[0].h3.text
# bookAuthor = bookCounter[0].find('div',attrs={'class':'authors'}).text
# print(bookAuthor)

# # print(bookCounter[0].td.img['data-src'])

# url = "https://1lib.in/papi/book/3558229/formats"
# headers = {'User-Agent': 'Chrome/54.0.2840.71'}
# try:
#  r = requests.get(url,headers=headers)
# except:
#     print(r)
# print(r.text)

import requests

headers = {
    'authority': '1lib.in',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^88^\\^, ^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://1lib.in/book/3558229/9b6b53',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'proxiesNotWorking=; domainsNotWorking=',
}

response = requests.get('https://1lib.in/papi/book/3558229/formats')

print(response.text)
