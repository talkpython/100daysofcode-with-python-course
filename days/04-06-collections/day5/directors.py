import csv
from math import nan
from numpy import NaN
import pandas as pd
from collections import defaultdict, namedtuple, Counter

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    csv_url = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'
    data = pd.read_csv(csv_url)

    directors = defaultdict(list)
    for row in data.itertuples():
        if(type(row.director_name) != str):
            continue
        m = Movie(title=row.movie_title.replace('\xa0', ''), year=row.title_year, score=row.imdb_score)
        directors[row.director_name].append(m)
    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    cnt = Counter()

    for director, movies in directors.items():
        cnt[director] += len(movies)
    for element in cnt:
        if cnt[element] < MIN_MOVIES:
            del(directors[element])
        else:
            avg_score = _calc_mean(directors[element])
            directors[element].append(avg_score)
    return directors


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    score = 0.0
    for movie in movies:
        score += movie.score
    return score / len(movies)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter:02}. {director:<52} {avg:.1f}'
    fmt_movie_entry = '{year:.0f}] {title:<50} {score}'
    sep_line = '-' * 60

    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] = movies[-1]
    directors_to_print = cnt.most_common(NUM_TOP_DIRECTORS)

    i = 1
    for dir in directors_to_print:
        print(fmt_director_entry.format(counter=i, director=dir[0], avg=dir[1]))
        for movie in directors[dir[0]]:
            if(type(movie) == float):
                continue
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        print(sep_line)
        i += 1


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()

    directors = get_average_scores(directors)
    print(directors['Christopher Nolan'])
    print_results(directors)


if __name__ == '__main__':
    main()
