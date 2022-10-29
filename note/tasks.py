from django.core.mail import send_mail
from note_django.celery import app


@app.task
def send_some_email(email, message):
    subject = message

    send_mail(
        subject,
        message,
        "admin@note_django.com",
        [email],
        fail_silently=False
    )
