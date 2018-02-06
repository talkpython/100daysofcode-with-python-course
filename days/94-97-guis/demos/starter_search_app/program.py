import api


def main():
    print("--------------------------------------")
    print("    MOVIE SEARCH APP (CLI EDITION)")
    print("--------------------------------------")
    print()
    print('How do you want to search?')
    mode = input("By [d]irector, [i]mdb code, or [k]eyword? ").strip().lower()

    if mode == 'd':
        director = input("Enter the director's name: ")
        results = api.find_movie_by_director(director)
    elif mode == 'i':
        code = input('Enter the IMDB code: ')
        results = api.find_movie_by_imdb_code(code)
    else:  # mode == 'k'
        keyword = input('Enter your (single) keyword: ')
        results = api.find_movie_by_keyword(keyword)

    print(f'There are {len(results)} movies found.')
    for r in results:
        print(f"{r.title} with code {r.imdb_code} and director {r.director} has score {r.imdb_score}")


if __name__ == '__main__':
    main()
