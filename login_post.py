import requests
from bs4 import BeautifulSoup

url = "https://the-internet.herokuapp.com/login"
headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}
login_data = []
login_data.append({
    'username' : 'tomsmith',
    'password' : 'SuperSecretPassword!',
})

r = requests.Session().post(url, data = login_data)
#s = requests.Session().post(url, data=login_data, headers=headers)
print(r)
