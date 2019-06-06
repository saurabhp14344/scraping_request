import requests
from bs4 import BeautifulSoup
from random import choice

def req_proxy():
    url = 'https://www.sslproxies.org/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    return {'https': choice(list(map(lambda x : x[0]+':'+x[1], list(zip(map(lambda x:x.text, soup.find_all("td")[::8]), map(lambda x:x.text, soup.find_all("td")[1::8]))))))}

def proxy_info(request_type, url, **kwargs):
    while 1:
        try:
            proxy = req_proxy()
            print("using proxy is {}".format(proxy))
            r = requests.request(request_type, url, proxies=proxy, timeout=5, **kwargs)
            break
        except:
            pass
    return r

r = proxy_info('get', 'https://youtube.com')
print(r.text)
