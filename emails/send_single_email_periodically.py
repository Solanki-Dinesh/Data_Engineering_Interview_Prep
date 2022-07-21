# SMTP: Simple Mail Transfer Protocol
import yagmail
import time
from settings.email_pw import email_pw

sender = "jagoswami84@gmail.com"
receiver = "jagritimi31@gmail.com"

subject = "Test email"
contents = """
Hi, this is a test email!
"""

while True:
    yag = yagmail.SMTP(user=sender, password=email_pw)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    # time.sleep(30)


