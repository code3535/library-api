
import db


def get_all_loans():
    conn = db.connect()
    loans = conn.execute("SELECT * FROM loans").fetchall()
    conn.close()
    return loans


def get_loan_by_id(loan_id):
    conn = db.connect()
    loan = conn.execute(
        "SELECT * FROM loans WHERE id = ?", (loan_id,)
    ).fetchone()
    conn.close()
    return loan


def get_member_loans(member_id):
    conn = db.connect()
    loans = conn.execute(
        "SELECT * FROM loans WHERE member_id = ?", (member_id,)
    ).fetchall()
    conn.close()
    return loans


def get_book(book_id):
    conn = db.connect()
    book = conn.execute(
        "SELECT * FROM books WHERE id = ?", (book_id,)
    ).fetchone()
    conn.close()
    return book


def get_member(member_id):
    conn = db.connect()
    member = conn.execute(
        "SELECT * FROM members WHERE id = ?", (member_id,)
    ).fetchone()
    conn.close()
    return member


def create_loan(book_id, member_id, due_date, checked_out):
    conn = db.connect()

    cursor = conn.execute(
        """
        INSERT INTO loans (book_id, member_id, due_date, checked_out)
        VALUES (?, ?, ?, ?)
        """,
        (book_id, member_id, due_date, checked_out)
    )

    conn.execute(
        "UPDATE books SET available = 0 WHERE id = ?",
        (book_id,)
    )

    conn.commit()

    loan = conn.execute(
        "SELECT * FROM loans WHERE id = ?",
        (cursor.lastrowid,)
    ).fetchone()

    conn.close()
    return loan


def return_loan(loan_id, book_id, fine):
    conn = db.connect()

    conn.execute(
        "UPDATE loans SET returned = 1, fine = ? WHERE id = ?",
        (fine, loan_id)
    )

    conn.execute(
        "UPDATE books SET available = 1 WHERE id = ?",
        (book_id,)
    )

    conn.commit()

    loan = conn.execute(
        "SELECT * FROM loans WHERE id = ?", (loan_id,)
    ).fetchone()

    conn.close()
    return loan


def renew_loan(loan_id, new_due_date):
    conn = db.connect()

    conn.execute(
        """
        UPDATE loans
        SET due_date = ?, renewals = renewals + 1
        WHERE id = ?
        """,
        (new_due_date, loan_id)
    )

    conn.commit()

    loan = conn.execute(
        "SELECT * FROM loans WHERE id = ?", (loan_id,)
    ).fetchone()

    conn.close()
    return loan


def mark_fine_paid(loan_id):
    conn = db.connect()

    conn.execute(
        "UPDATE loans SET fine_paid = 1 WHERE id = ?",
        (loan_id,)
    )

    conn.commit()

    loan = conn.execute(
        "SELECT * FROM loans WHERE id = ?", (loan_id,)
    ).fetchone()

    conn.close()
    return loan
