from typing import List

import requests
import collections

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')


def find_movie_by_keyword(keyword: str) -> List[Movie]:
    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'
    return __get_results(url)


def find_movie_by_director(director_name: str) -> List[Movie]:
    url = f'http://movie_service.talkpython.fm/api/director/{director_name}'
    return __get_results(url)


def find_movie_by_imdb_code(imdb_code: str) -> List[Movie]:
    url = f'http://movie_service.talkpython.fm/api/movie/{imdb_code}'
    resp = requests.get(url)
    resp.raise_for_status()
    result = resp.json()
    if not result.get('imdb_code'):
        return []

    return [Movie(**result)]


def __get_results(url):
    resp = requests.get(url)
    resp.raise_for_status()
    results = resp.json()
    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))
    return movies
