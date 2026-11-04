import json
from pathlib import Path

SAVE_FILE = Path("books.json")


def validate_books(books):
    if not isinstance(books, list):
        raise ValueError("The catalog must be a list.")

    seen_ids = set()

    for book in books:
        if not isinstance(book, dict):
            raise ValueError("Each book must be a dictionary.")

        book_id = book.get("id")
        title = book.get("title")

        if not isinstance(book_id, str) or not book_id.strip():
            raise ValueError("Every book needs a valid ID.")

        if book_id in seen_ids:
            raise ValueError(f"Duplicate book ID: {book_id}")

        if not isinstance(title, str) or not title.strip():
            raise ValueError("Every book needs a title.")

        seen_ids.add(book_id)


def save_books(books):
    validate_books(books)

    temporary_file = SAVE_FILE.with_suffix(".tmp")

    try:
        with temporary_file.open("w", encoding="utf-8") as file:
            json.dump(books, file, indent=4)

        # Replace the old save only after writing succeeds.
        temporary_file.replace(SAVE_FILE)

    finally:
        # Remove an incomplete temporary file if one remains.
        if temporary_file.exists():
            temporary_file.unlink()


def load_books():
    with SAVE_FILE.open("r", encoding="utf-8") as file:
        books = json.load(file)

    validate_books(books)
    return books


if __name__ == "__main__":
    catalog = [
        {"id": "B001", "title": "Python Basics"},
        {"id": "B002", "title": "Learning Go"},
    ]

    save_books(catalog)
    print("Catalog saved.")

    restored_catalog = load_books()

    print("Restored catalog:")
    for book in restored_catalog:
        print(book)

    # Demonstrate duplicate-ID rejection.
    invalid_catalog = [
        {"id": "B001", "title": "Python Basics"},
        {"id": "B001", "title": "Learning Go"},
    ]

    try:
        save_books(invalid_catalog)
    except ValueError as error:
        print(f"Rejected invalid catalog: {error}")