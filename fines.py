
from datetime import date


FINE_PER_DAY = 0.50


def money(amount):
    return round(float(amount), 2)


def calculate_fine(due_date):
    due = date.fromisoformat(due_date)
    days_late = (date.today() - due).days

    return money(max(0, days_late) * FINE_PER_DAY)
