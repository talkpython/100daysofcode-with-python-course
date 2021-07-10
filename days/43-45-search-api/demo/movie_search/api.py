from typing import List

import requests
import collections

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')


def find_movie_by_title(keyword: str) -> List[Movie]:
    url = f'https://movieservice.talkpython.fm/api/search/{keyword}'

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))

    return movies
