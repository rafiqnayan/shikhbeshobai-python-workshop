import yagmail
import getpass

subject = 'My first email with Python'
body = "Welcome at ShikhbeShobai https://shikhbeshobai.com/"

email_password = getpass.getpass(prompt='Password: ', stream=None)
from_gmail_address = 'rafiqnayan@gmail.com'
to_email_address = 'nayan@surecash.net'

yag = yagmail.SMTP(from_gmail_address, email_password)
yag.send(to=to_email_address, subject=subject, contents=body)
print "Email sent successfully"
