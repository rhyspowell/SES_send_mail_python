#!/usr/bin/env python
import sys, smtplib
from email.mime.text import MIMEText as text

def send_email(args):
 
        m = text(args[4])
        m['Subject'] = args[3]
        m['From'] = args[1]
        m['To'] = args[2]
        #print "Message length is " + repr(len(msg))

        #Change according to your settings
        smtp_server = 'email-smtp.us-east-1.amazonaws.com'
        smtp_username = 'amazon ses username'
        smtp_password = 'amazon ses password'
        smtp_port = '587'
        smtp_do_tls = True

        server = smtplib.SMTP(
            host = smtp_server,
            port = smtp_port,
            timeout = 10
        )
        server.set_debuglevel(10)
        server.starttls()
        server.ehlo()
        server.login(smtp_username, smtp_password)
        server.sendmail(args[1], args[2], m.as_string())

        print "email should have gone"

args_length = len(sys.argv)
if args_length != 5:
        print "This module requires 3 arguements 1 fromaddr, 2 toaddr, 3 subject, 4 message eg. send_mail.py \"test@domain.com\" \"test@domain.com\" \"This is the subject\" \"This is the message\""
else:
        send_email(sys.argv)
