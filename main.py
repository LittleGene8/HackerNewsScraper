import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('http://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')

def create_custom_hn(links, subtext):
	hn = []

	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href')
		vote = subtext[idx].select('.score')

		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points >= 100:
				hn.append({'title':title, 'link' : href, 'votes': points})

	return sorted(hn, key=lambda k:k['votes'], reverse=True)

results = create_custom_hn(links, subtext)

pprint.pprint(results)
