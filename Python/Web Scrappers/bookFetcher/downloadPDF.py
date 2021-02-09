import requests
from bs4 import BeautifulSoup

extensionLink = "https://1lib.in/"

headers = {'User-Agent': 'Chrome/54.0.2840.71'}

url = "https://1lib.in/book/3558229/9b6b53"
r = requests.get(url,headers=headers)

soup = BeautifulSoup(r.content,'html5lib')

downloadLink = soup.find_all('div' , attrs={'class' : 'book-details-button'})[0].a['href']
print(downloadLink)

# https://1lib.in/dl/616568/e7d321
output = "/dl/1323400/29dd9c"