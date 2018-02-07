import api
from gooey import GooeyParser, Gooey


@Gooey(program_name='Movie Search App',
       program_description="Search Talk Python's demo data for movies")
def main():
    print("--------------------------------------")
    print("    MOVIE SEARCH APP (GUI EDITION)")
    print("--------------------------------------")
    print()
    mode, value = get_params()

    if mode == 'Director':
        results = api.find_movie_by_director(value)
    elif mode == 'IMDB Code':
        results = api.find_movie_by_imdb_code(value)
    else:  # mode == 'Keyword'
        results = api.find_movie_by_keyword(value)

    print(f'There are {len(results)} movies found.')
    for r in results:
        print(f"{r.title} with code {r.imdb_code} and director {r.director} has score {r.imdb_score}")


def get_params():
    parser = GooeyParser()
    parser.add_argument('search_term', help="The search term")
    parser.add_argument(
        dest='mode',
        widget='Dropdown',
        choices=['Director', 'IMDB Code', 'Keyword']
    )
    args = parser.parse_args()
    return args.mode, args.search_term


if __name__ == '__main__':
    main()
