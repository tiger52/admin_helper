#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
#me = "testpython@digitalscreens.com.ua"
#me = "testpython@owndomain.bsv"
me = "testpython@bet-invest.co.uk"
#you = "s.babik@digitalscreens.com.ua"
you = "s.babik@betinvest.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
    </p>
  </body>
</html>
<CR><LF>.<CR><LF>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
#s = smtplib.SMTP('localhost')
#s = smtplib.SMTP('172.30.104.140')
#s = smtplib.SMTP('mx.inside.digitalscreens.com.ua')
s = smtplib.SMTP('mail.dev.ves')
#s = smtplib.SMTP('aspmx4.googlemail.com')
# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.set_debuglevel(1)
s.sendmail(me, you, msg.as_string())
s.quit()

