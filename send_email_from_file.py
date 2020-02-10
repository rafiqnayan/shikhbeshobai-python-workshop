import yagmail
import getpass
from string import Template
import csv

subject = 'Registration Confirmation'
body = """
Dear $name, 
Thank you for registering at ShikhbeShobai. 
Your registration token is $token.
We are eagerly waiting for your presence!
"""
body_template = Template(body)

email_password = getpass.getpass(prompt='Password: ', stream=None)
from_gmail_address = 'rafiqnayan@gmail.com'
yag = yagmail.SMTP(from_gmail_address, email_password)

with open('user_tokens.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            user_name = row[0]
            to_email_address = row[1]
            user_token = row[2]
            line_count += 1
            email_body = body_template.substitute(name=user_name, token=user_token)
            yag.send(to=to_email_address, subject=subject, contents=email_body)

print "Email sent successfully"
