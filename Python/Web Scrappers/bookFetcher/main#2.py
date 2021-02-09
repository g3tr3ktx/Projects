from flask import Flask
import requests
from bs4 import BeautifulSoup
import json


app = Flask(__name__) 

@app.route("/") 
def home_view(): 
     query = "Python Machine Learning"

     URL = "https://1lib.in/s/"+ query +"/?extension=pdf"
     # extensionLink = "https://1lib.in/"
     r = requests.get(URL)
     soup = BeautifulSoup(r.content, 'html5lib')
     # s = soup.find_all('div', attrs={'class':'checkBookDownloaded itemCoverWrapper'}) 
     # o = soup.find_all('h3', attrs={'itemprop':'name'})
     # print(o)
     # for i in s:
     #     book = {}
     #     book["image"] = s
     # print(extensionLink+s[0].a.text)
     # print(s[0].img['data-src'])

     bookCounter = soup.find_all('div',attrs={'class':'resItemBox resItemBoxBooks exactMatch'}) #list
     allBooks = []
     for book in bookCounter:
         currentBook = {}
         currentBook["bookId"] = book['data-book_id']
         currentBook["bookPath"] = book.h3.a['href']
         currentBook["bookImage"] = book.td.img['data-src']
         currentBook["bookName"] = book.h3.text.strip()
         currentBook["bookAuthor"] = book.find('div',attrs={'class':'authors'}).text.strip()
         allBooks.append(currentBook)

     # print(allBooks)
     print(allBooks[0]['bookId'])
     print(allBooks[0]['bookPath'])
     headers = {
    'authority': '1lib.in',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^88^\\^, ^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://1lib.in/'+allBooks[0]['bookPath'],
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'proxiesNotWorking=; domainsNotWorking=',
     }

     response = requests.get('https://1lib.in/papi/book/'+allBooks[0]['bookId']+'/formats',headers=headers)

     print(response.text)
     return response.text


@app.route("/bookname/<bookNameQuery>")
def bookFetch(bookNameQuery):
     url = "https://1lib.in/s/"+ bookNameQuery +"/?extension=pdf"
     r = requests.get(url)
     soup = BeautifulSoup(r.content, 'html5lib')
     bookCounter = soup.find_all('div',attrs={'class':'resItemBox resItemBoxBooks exactMatch'}) #list
     allBooks = []
     for book in bookCounter:
         currentBook = {}
         currentBook["bookId"] = book['data-book_id']
         currentBook["bookPath"] = book.h3.a['href'].replace('/book/'+book['data-book_id']+'/','')
         currentBook["bookImage"] = book.td.img['data-src']
         currentBook["bookName"] = book.h3.text.strip()
         currentBook["bookAuthor"] = book.find('div',attrs={'class':'authors'}).text.strip()
         allBooks.append(currentBook)
     return json.dumps(allBooks)

@app.route("/bookid/<bookId>/bookpath/<bookPath>")
def pdffetch(bookId,bookPath):
     headers = {
     'authority': '1lib.in',
     'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^88^\\^, ^\\^Google',
     'sec-ch-ua-mobile': '?0',
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
     'accept': '*/*',
     'sec-fetch-site': 'same-origin',
     'sec-fetch-mode': 'cors',
     'sec-fetch-dest': 'empty',
     'referer': 'https://1lib.in/book/'+bookId+'/'+ bookPath,
     'accept-language': 'en-US,en;q=0.9',
     'cookie': 'proxiesNotWorking=; domainsNotWorking=',
     }

     response = requests.get('https://1lib.in/papi/book/'+bookId+'/formats',headers=headers)

     print(response.text)
     return response.text