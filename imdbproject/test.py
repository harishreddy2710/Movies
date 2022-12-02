from bs4 import BeautifulSoup
import requests

try:
    source = requests.get('https://www.imdb.com/title/tt10872600/?ref_=fn_al_tt_2')
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    movie_name = soup.find('h1', attrs={"data-testid": 'hero-title-block__title'}).get_text()
    print(movie_name)
    rating = soup.find('span', class_='sc-7ab21ed2-1 jGRxWM').get_text()
    print(rating)
    director = soup.find('a',
                         class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').get_text()
    print(director)
    genre = soup.find('div', class_='ipc-chip-list__scroller').get_text()
    print(genre)
    storyline = soup.find('div', class_='ipc-html-content-inner-div').get_text()
    print(storyline)
    topcast = soup.find('a', attrs={'data-testid': 'title-cast-item__actor'})
    print(topcast)

except Exception as e:
    print(e)
