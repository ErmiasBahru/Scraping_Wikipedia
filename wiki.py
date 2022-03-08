import sys
import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))
res.raise_for_status()

wiki = bs4.BeautifulSoup(res.text,'html.parser')

for i in wiki.select('p'):
    print(i.getText())