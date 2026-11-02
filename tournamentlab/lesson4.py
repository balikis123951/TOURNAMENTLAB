books = [
    {"title": "Python Basics", "rating": 4.2},
    {"title": "Learn Go", "rating": 4.8},
    {"title": "Clean Code", "rating": 4.8},
    {"title": "Web Development", "rating": 3.9},
    {"title": "Algorithms", "rating": 4.2},
]


def sort_books(books):
    return sorted(
        books,
        key=lambda book: (
            -book["rating"],
            book["title"].casefold(),
        )
    )


sorted_books = sort_books(books)

for book in sorted_books:
    print(f'{book["title"]}: {book["rating"]}')