import requests
path = "c88ef3"
url = "http://127.0.0.1:5000/bookid/5460543/bookpath/"+path
r = requests.get(url)
print(r.text)