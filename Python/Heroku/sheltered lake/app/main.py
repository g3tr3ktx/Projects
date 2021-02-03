import requests
from bs4 import BeautifulSoup
from flask import Flask
import json

app = Flask(__name__)

@app.route("/<query>")
def home(query):
    url = "https://www.google.com/search?q="+query+"pdf"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    samar = soup.find_all('a',href=True)
    data = []
    response = {
        'data' : data
    }
    for link in samar:
     if(link['href'].find('.pdf')!=-1):
      download_link = link['href']
      end = download_link.find('.pdf&sa')
      if(download_link[7:end+4].find('http')!=-1):
       book_link = download_link[7:end+4].replace("%2520","%20")
       data.append(book_link)
      print(download_link[7:end+4])
    print(response)
    return json.dumps(response)