from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from decouple import config


def send_mail(to_email, subject, content):
    try:
        message = Mail(
            from_email=config("SENDING_EMAIL"),
            to_emails=to_email,
            subject=subject,
            html_content=content,
        )
        sg = SendGridAPIClient(config("SENDGRID_API_KEY"))
        sg.send(message)
        return True
    except Exception as e:
        return False
