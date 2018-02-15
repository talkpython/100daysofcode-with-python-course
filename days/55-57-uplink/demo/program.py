from blog_client import BlogClient


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
    svc = BlogClient()
    response = svc.all_entries()

    posts = response.json()
    print()
    for idx, p in enumerate(posts, 1):
        print(" {}. [{:,} views] {}".format(
            idx, p.get('view_count'), p.get('title')
        ))
    print()
    selected = int(input('Which number to view? '))

    selected_id = posts[selected - 1].get('id')

    response = svc.entry_by_id(selected_id)

    selected_post = response.json()
    print("Details for selected_post: {}".format(selected_post.get('id')))
    print("Title: " + selected_post.get('title'))
    print("Written: " + selected_post.get('published'))
    print("Content: " + selected_post.get('content'))
    print()
    print()


def write_post():
    svc = BlogClient()

    title = input("Title: ")
    content = input("Body contents: ")
    view_count = int(input("view count (int): "))

    resp = svc.create_new_entry(title, content, view_count)

    print()
    print("Created new post successfully: {}".format(resp.json().get('id')))
    print()


if __name__ == '__main__':
    main()
