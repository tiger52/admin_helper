#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
from sys import exit

processname = "TestMonPid"

# variables you must specify !!!
you = "s.babik@digitalscreens.com.ua,p.khilko@digitalscreens.com.ua"
timeCrash = 60*5 # 5min
#pidfile = "somefile.pid"

parser = argparse.ArgumentParser(description="Monitoring about pid file of some process VIA CRON !!!")
parser.add_argument('-f', '--pidfile', help='the pid file of the process')
args = parser.parse_args()
#print args
if args.pidfile is None:
	parser.print_help()
	exit()

hostName = os.uname()[1]
me = "nodejs@{}".format(hostName)
if os.path.exists(args.pidfile):
	timePidFile = os.path.getctime(args.pidfile)
	Alarmtime = time.time() - timePidFile
	if (Alarmtime <= timeCrash):
		# Create message container - the correct MIME type is multipart/alternative.
		msg = MIMEMultipart()
		msg['Subject'] = "{0} restarted on {1}".format(processname,hostName)
		msg['From'] = me
		msg['To'] = you
		# Create the body of the message (a plain-text and an HTML version).
		text = "Hi!\nServer: {0}\nNodeJS has been restarted\nPID file: {1}".format(hostName,args.pidfile)
		# Record the MIME types of both parts - text/plain and text/html.
		part1 = MIMEText(text, 'plain')
		msg.attach(part1)
		# Send the message via local SMTP server.
		s = smtplib.SMTP('localhost')
		s.sendmail(me, you, msg.as_string())
		s.quit()
#		print "message send"
#	else:
#		print "do nothing, time crash is over"
#else: 
#	print "file not exist"

