
import member_repository
import validation


def get_members():
    return member_repository.get_all_members()


def get_member(member_id):
    return member_repository.get_member_by_id(member_id)


def add_member(data):
    name = data.get("name")
    email = data.get("email")
    member_type = data.get("type")

    if not name:
        return None, "name is required"

    if not validation.is_valid_email(email):
        return None, "invalid email"

    if not validation.is_valid_member_type(member_type):
        return None, "invalid member type"

    try:
        member = member_repository.create_member(
            name, email, member_type
        )
        return member, None
    except Exception:
        return None, "email already exists"
