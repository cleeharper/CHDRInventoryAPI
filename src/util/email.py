from typing import Optional
from flask_mail import Mail, Message
from util.config import secrets
import smtplib
from email.mime.text import MIMEText

class Emailer:
    _mail = Mail()

    @staticmethod
    def init(app):
        Emailer._mail.init_app(app)

    @staticmethod
    def send_email(
        recipient: str,
        subject: str,
        body: str,
        attachment: Optional[str] = None,
        cc: Optional[str] = None,
    ):
        """
        Sends an email to the specified recipient.
        Throws SMTPException on failure
        message = Message(
            recipients=[recipient],
            subject=subject,
            body=body,
            sender=secrets["EMAIL_USERNAME"],
            cc=[cc],
        )

        # Can only add a single attachment
        # Attachment is formatted as a string representing the filepath
        if attachment:
            with open(attachment) as fp:
                message.attach(attachment, "calendar/ics", fp.read())

        Emailer._mail.send(message)
        """
        msg = MIMEText(body)
        msg['Subject'] = subject 
        msg['From'] = secrets["EMAIL_USERNAME"]
        msg['To'] = recipient
        s = smtplib.SMTP('localhost')
        s.sendmail(msg['From'], msg['To'], body)
        s.quit()


