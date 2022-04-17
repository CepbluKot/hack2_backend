import smtplib
import atexit
from .getters.read_config import get_post_server_address, get_password, get_email


server = smtplib.SMTP_SSL(get_post_server_address())


def exit_handler():
    server.quit()


def launch_connection():
    # server.set_debuglevel(1)
    server.ehlo(get_email())
    server.login(get_email(), get_password())
    server.auth_plain()

    atexit.register(exit_handler)

launch_connection()

def send_email(to_user_email: str, subject: str, text: str):
    
    email = get_email()
    dest_email = to_user_email
    subject = subject
    email_text = text

    message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email,
                                                        dest_email, 
                                                        subject, 
                                                        email_text)

    server.sendmail(email, dest_email, message)
