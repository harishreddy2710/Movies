import requests
from bs4 import BeautifulSoup
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
import locale

from .models import MovieInfo
from .serializer import MovieSerializer

BASE_URL = 'https://www.imdb.com/'
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
response = {}


@api_view()
def getById(request, slug):
    if request.method == 'GET':
        url = BASE_URL + 'title/' + slug
        print(url)
        source = requests.get(url)
        print(url)
        source.raise_for_status()
        soup = BeautifulSoup(source.text, 'html.parser')
        movie_name = soup.find('h1', attrs={"data-testid": 'hero-title-block__title'}).get_text()
        rating = soup.find('span', class_='sc-7ab21ed2-1 jGRxWM').get_text()
        director = soup.find('a',
                             class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').get_text()
        genre = soup.find('div', class_='ipc-chip-list__scroller').get_text()
        top_cast = soup.find('a', attrs={'data-testid': 'title-cast-item__actor'}).get_text()

        storyline = soup.find('div', class_='ipc-html-content-inner-div').get_text()

        response['movie_name'] = movie_name
        response['rating'] = rating
        response['director'] = director
        response['genre'] = genre
        response['top_cast'] = top_cast
        response['storyline'] = storyline

        dict_data = response
        print(dict_data)
        record = MovieInfo.objects.create(
            movie_name=dict_data.get('movie_name', None),
            rating=dict_data.get('rating', None),
            director=dict_data.get('director', None),
            genre=dict_data.get('genre', None),
            storyline=dict_data.get('storyline', None),
            top_cast = dict_data.get('top_cast', None)

        )
        serializer_data = MovieSerializer(record).data
        print(serializer_data)
        return Response(serializer_data)
