def main():
    val = 'RUN'

    while val:
        print("What would you like to do next?")
        val = input('[w]rite a post or [r]ead them?')

        if val == 'w':
            write_post()
        elif val == 'r':
            read_posts()


def read_posts():
    pass


def write_post():
    pass
