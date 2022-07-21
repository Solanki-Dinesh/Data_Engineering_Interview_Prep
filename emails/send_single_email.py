# SMTP: Simple Mail Transfer Protocol
import yagmail
from settings.email_pw import email_pw

sender = "swami84@gmail.com"
receiver = "jwami31@gmail.com"

subject = "Test email"
contents = """
Hi, this is a test email!
"""

yag = yagmail.SMTP(user=sender, password=email_pw)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")
