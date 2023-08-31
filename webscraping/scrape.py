import pprint

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/?p=2')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find('a'))
# print(soup.title)
# print(soup.find(id='score_20514755'))
# print(soup.select('.score'))
# print(soup.select('#score_37221287'))
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

links2= soup.select('.titleline > a')
subtext2= soup.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


# print(votes[0])
# print(votes[3].get('id'))
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(mega_links, mega_subtext):
    hn = []
    for idx, item in enumerate(mega_links):
        title = item.getText()
        href = item.get('href', None)
        vote = mega_subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
