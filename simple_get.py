import requests
from lxml import html

page = requests.get('https://docs.python-guide.org/scenarios/scrape/')

data = html.fromstring(page.content)

tree = data.xpath('//div[@id="lxml-and-requests"]/h2/text()')
print(tree)