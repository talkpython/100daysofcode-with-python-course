from typing import List

import requests
import collections
import random

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')


def find_movie_by_title(keyword: str) -> List[Movie]:
    if not keyword or not keyword.strip():
        raise ValueError('Must specify a search term.')

    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    results = create_random_errors(results)

    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))

    return movies


def create_random_errors(results):
    # This is a method to occasionally create some more
    # interesting errors other than simply network connectivity errors
    # which are the only "real" errors. This will let us test
    # more types.

    num = random.randint(1, 20)
    if 16 < num <= 18:
        return {}  # Whoops! No data.
    elif 18 < num <= 20:
        raise StopIteration()

    return results  # no errors here.
