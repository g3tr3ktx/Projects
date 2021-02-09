import requests
from bs4 import BeautifulSoup
URL = "https://1lib.in/s/dune/?extension=pdf"
extensionLink = "https://1lib.in/"
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
    currentBook["bookId"] = extensionLink+book.h3.a['href']
    # currentBook["bookImage"] = book.td.img['data-src']
    # currentBook["bookName"] = book.h3.text.strip()
    # currentBook["bookAuthor"] = book.find('div',attrs={'class':'authors'}).text.strip()
    allBooks.append(currentBook)

print(allBooks)

# print(bookCounter[0].find('div',attrs={'class':'authors'}).text)

# print(bookCounter[0].td.img['data-src'])