
import re
from datetime import date


def is_valid_email(value):
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value or ""))


def is_valid_isbn(value):
    if not value:
        return False

    isbn = value.replace("-", "").replace(" ", "")

    return (
        len(isbn) in (10, 13)
        and isbn.isdigit()
    )


def is_valid_date(value):
    try:
        date.fromisoformat(value)
        return True
    except (ValueError, TypeError):
        return False


def is_valid_member_type(value):
    return value in ("student", "staff")
