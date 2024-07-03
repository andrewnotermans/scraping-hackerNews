import requests
from bs4 import BeautifulSoup
import pprint

def get_soup(url):
    res = requests.get(url)
    return BeautifulSoup(res.text, 'html.parser')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, id, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        numer = int(id[idx].getText().replace('.',''))
        vote = subtext[idx].select('.score')
        if len(vote):
          points = int(vote[0].getText().replace(' points', ''))
          if points > 99:
            hn.append({'id': numer,'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

# Initialisation des listes pour les liens et les sous-textes
mega_links = []
mega_subtext = []
mega_id = []

# Boucle pour parcourir plusieurs pages
for i in range(1, 23):  # Vous pouvez ajuster le nombre de pages ici
    url = f'https://news.ycombinator.com/news?p={i}'
    soup = get_soup(url)
    mega_id.extend(soup.select('.rank'))
    mega_links.extend(soup.select('.titleline > a'))
    mega_subtext.extend(soup.select('.subtext'))




# Affichage des résultats
pprint.pprint(create_custom_hn(mega_links, mega_id, mega_subtext))
