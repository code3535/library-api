
from flask import Blueprint, jsonify, request

import book_service
from errors import error_response

books_bp = Blueprint("books", __name__)


def format_book(book):
    return {
        "id": book["id"],
        "title": book["title"],
        "author": book["author"],
        "isbn": book["isbn"],
        "available": bool(book["available"])
    }


@books_bp.route("/books", methods=["GET"])
def list_books():
    available = request.args.get("available") == "true"
    books = book_service.get_books(available)

    return jsonify([format_book(book) for book in books])


@books_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = book_service.get_book(book_id)

    if book is None:
        return error_response("book not found", 404)

    return jsonify(format_book(book))


@books_bp.route("/books", methods=["POST"])
def create_book():
    data = request.get_json(silent=True) or {}
    book, error = book_service.add_book(data)

    if error:
        return error_response(error, 400)

    return jsonify(format_book(book)), 201


@books_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    success, error = book_service.remove_book(book_id)

    if not success:
        status = 404 if error == "book not found" else 409
        return error_response(error, status)

    return "", 204
