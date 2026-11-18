
from datetime import date

import fines


def check_borrowing_eligibility(member, loans):
    owed = 0
    open_loans = 0

    for loan in loans:
        if loan["returned"] == 0:
            open_loans += 1
            owed += fines.calculate_fine(loan["due_date"])
        elif loan["fine_paid"] == 0:
            owed += loan["fine"]

    if owed > 0:
        return "member has unpaid fines"

    limit = 5 if member["type"] == "staff" else 3

    if open_loans >= limit:
        return "loan limit reached"

    return None


def check_renewal_eligibility(loan):
    if loan["returned"] == 1:
        return "loan already returned"

    due_date = date.fromisoformat(loan["due_date"])

    if due_date < date.today():
        return "overdue loans cannot be renewed"

    if loan["renewals"] >= 1:
        return "loan was already renewed"

    return None
