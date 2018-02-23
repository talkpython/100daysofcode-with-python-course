import api
import requests.exceptions


def main():
    keyword = input('Keyword of title search: ')
    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not find server. Check your network connection.")
    except ValueError:
        print("ERROR: You must specify a search term.")
    except Exception as x:
        print("Oh that didn't work!: {}".format(x))


if __name__ == '__main__':
    main()
