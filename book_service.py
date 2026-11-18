
import book_repository
import validation


def get_books(available_only=False):
    return book_repository.get_all_books(available_only)


def get_book(book_id):
    return book_repository.get_book_by_id(book_id)


def add_book(data):
    if not data.get("title") or not data.get("author"):
        return None, "title and author are required"

    if not validation.is_valid_isbn(data.get("isbn")):
        return None, "invalid isbn"

    book = book_repository.create_book(
        data["title"],
        data["author"],
        data["isbn"]
    )

    return book, None


def remove_book(book_id):
    book = book_repository.get_book_by_id(book_id)

    if book is None:
        return False, "book not found"

    if book["available"] == 0:
        return False, "book is on loan"

    book_repository.delete_book(book_id)
    return True, None
