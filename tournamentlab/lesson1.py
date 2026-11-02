movies = [
    {"id": "MOV001", "title": "The Last Mission", "year": 2024},
    {"id": "MOV002", "title": "Shadow Strike", "year": 2023},
    {"id": "MOV003", "title": "Final Arena", "year": 2025},
]


def find_movie_by_id(movies, movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie

    return None


def add_movie(movies, movie_id, title, year):
    for movie in movies:
        if movie["id"] == movie_id:
            return False

    movies.append({
        "id": movie_id,
        "title": title,
        "year": year,
    })

    return True


# Find an existing movie.
movie = find_movie_by_id(movies, "MOV002")

if movie is not None:
    print("Found:", movie["title"])
else:
    print("Movie not found")


# Try adding a new movie.
added = add_movie(
    movies,
    "MOV004",
    "Cyber Arena",
    2026,
)

print("Movie added:", added)


# Try adding a duplicate ID.
added = add_movie(
    movies,
    "MOV001",
    "Duplicate Movie",
    2026,
)

print("Duplicate added:", added)


# Display the final collection.
for movie in movies:
    print(movie["id"], movie["title"], movie["year"])