# SMTP: Simple Mail Transfer Protocol
import yagmail
import time
from settings.email_pw import email_pw
from datetime import datetime

sender = "jagrii84@gmail.com"
receiver = "jagritigmi31@gmail.com"

subject = "Test email"
contents = """
Hi, this is a test email!
"""

while True:
    now = datetime.now()
    if now.hour == 15 and now.minute == 15:
        yag = yagmail.SMTP(user=sender, password=email_pw)
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email Sent!")
        time.sleep(60)


