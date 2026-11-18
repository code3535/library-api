
def send_notification(email, subject, body):
    """
    Mock notification system.
    Writes notifications to outbox.txt instead of sending emails.
    """

    with open("outbox.txt", "a") as file:
        file.write(
            f"TO: {email} | SUBJECT: {subject} | BODY: {body}\n"
        )

    return True
