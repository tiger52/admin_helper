# send mail via telnet
```
openssl s_client -quiet -crlf -starttls smtp -connect gmail-smtp-in.l.google.com:25

telnet 1.2.3.4 25

EHLO mta.sendios.net
MAIL FROM:<bill.gates@example.com>
RCPT TO:<noreply@domain.com>
DATA
From: john cena <bill.gates@example.com>
To: petro pedro <noreply@domain.com>>
Subject: Test Email
Date: Mon, 12 Jun 2024 10:30:00 -0400
Message-ID: <unique.message.id1@example.com>

This is a test email sent via SMTP.
.

QUIT
```
