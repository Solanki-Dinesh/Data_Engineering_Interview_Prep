# SMTP: Simple Mail Transfer Protocol
import yagmail
import pandas as pd
from settings.email_pw import email_pw

sender = "jagami84@gmail.com"

subject = "Test email"
# contents = """
# Hi, this is a test email!
# """
contacts_df = pd.read_csv("contacts.csv")
# print(contacts_df)

yag = yagmail.SMTP(user=sender, password=email_pw)

for index, row in contacts_df.iterrows():
    contents = f"""
    Hi {row['name']}, this is a test email!"""
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email Sent!")
