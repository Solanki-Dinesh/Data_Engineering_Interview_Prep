# SMTP: Simple Mail Transfer Protocol
import yagmail
import pandas as pd
from settings.email_pw import email_pw

sender = "jagmi84@gmail.com"
receiver = "jagri1@gmail.com"

subject = "Test email"

contacts = pd.read_csv('contacts.csv')

yag = yagmail.SMTP(user=sender, password=email_pw)

for index, row in contacts.iterrows():
    contents = [f"""
    Hi, {row['name']} you have to pay {row['amount']}.
    Bill is attached.
    """, row['filepath']]

    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
