import yagmail
import getpass

subject = 'My first email with Python with attchement'
body = """
Welcome at ShikhbeShobai https://shikhbeshobai.com/. 
Please check the attached file.
"""
attachment_1 = 'shikhbe_shobai_logo.jpg'

email_password = getpass.getpass(prompt='Password: ', stream=None)
from_gmail_address = 'rafiqnayan@gmail.com'
to_email_address = 'nayan@surecash.net'

yag = yagmail.SMTP(from_gmail_address, email_password)
yag.send(to=to_email_address, subject=subject, contents=body, attachments=attachment_1)
print "Email sent successfully"
