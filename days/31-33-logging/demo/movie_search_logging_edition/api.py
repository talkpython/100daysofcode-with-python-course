from typing import List

import logbook
import requests
import collections
import random

import time

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')

api_log = logbook.Logger('API')


def find_movie_by_title(keyword: str) -> List[Movie]:
    t0 = time.time()

    api_log.trace('Starting search for {}'.format(keyword))

    if not keyword or not keyword.strip():
        api_log.warn("No keyword supplied")
        raise ValueError('Must specify a search term.')

    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'

    resp = requests.get(url)
    api_log.trace("Request finished, status code {}.".format(resp.status_code))
    resp.raise_for_status()

    results = resp.json()
    results = create_random_errors(results)

    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))

    t1 = time.time()

    api_log.trace('Finished search for {}, {:,} results in {} ms.'.format(
        keyword, len(movies), int(1000 * (t1 - t0))))

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
