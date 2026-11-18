
import db


def get_all_members():
    conn = db.connect()

    members = conn.execute(
        "SELECT * FROM members"
    ).fetchall()

    conn.close()
    return members


def get_member_by_id(member_id):
    conn = db.connect()

    member = conn.execute(
        "SELECT * FROM members WHERE id = ?",
        (member_id,)
    ).fetchone()

    conn.close()
    return member


def create_member(name, email, member_type):
    conn = db.connect()

    cursor = conn.execute(
        """
        INSERT INTO members (name, email, type)
        VALUES (?, ?, ?)
        """,
        (name, email, member_type)
    )

    conn.commit()

    member = conn.execute(
        "SELECT * FROM members WHERE id = ?",
        (cursor.lastrowid,)
    ).fetchone()

    conn.close()
    return member
