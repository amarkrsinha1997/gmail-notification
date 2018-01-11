
import way2python
import imaplib,email,time
from getpass import getpass
print """
	+=================================================================================================================+
	+======================================Gmail Sms Notification Script==============================================+
	+=================================================================================================================+
"""

#Gmail User Id and Password
username= raw_input(" [+] Enter your gmail Id : ")
password=getpass(" [+] Enter your Gmail Password : ")

#Way2sms User Id and Password
number=int(raw_input(' [+] Please Enter Your Way2sms Username : '))
password2=int(getpass(' [+] Please Enter Your Way2sms Password : '))

# Number for the notification alert
mobile = int(raw_input(" [+] Enter a number where you want to send the notification : "))

#AUTHENTICATION TO GMAIL
imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
print imap.login(username, password)

#LOOP FOR SENDING THE CODE AFTER EVERY INTERVAL OF SOME TIME
while True:
	#selects the label
	imap.select('INBOX')

	# Use search(), not status()
	# search for the all unread email
	# Gather the list of all id
	status, response = imap.search(None, '(UNSEEN)')
	id_list = response[0].split()

	# Print the count of all unread messages
	print len(id_list)
	if len(id_list)>0:
		#GETS THE LATEST UNREAD EMAIL
		latest_email_id = int(id_list[-1])
		#FECTHES IT DATA
		typ, data = imap.fetch(latest_email_id, '(RFC822)')
		#Extracts and the send the data useful data to the api
		for response_part in data:
			if isinstance(response_part, tuple):
				msg = email.message_from_string(response_part[1])

				email_subject = msg.get('subject')
				email_from = msg.get('from')

				print '[^] From : ' + email_from + '\n'
				print '[^] Subject : ' + email_subject + '\n'

				#USES THE FILE NAME way2python.py FUNCTION TO SEND THE SMS THROUGH WAY2SMS PORTAL
				way2python.way2sms(mobile, number, password2,'New email received from : \n'+email_from)

	# CODE TO EXTRACT THEBODY PART OF THE EMAIL
				# for part in msg.walk():
				# 	if part.get_content_type()=='text/plain':
				# 		body= part.get_payload(decode=True)
				# 		print body.decode('utf-8')
				# 	else:
				# 		continue

	print """
		*****************************************************************
		************************TIME TO SLEEP****************************
		*****************************************************************\n\n\n
	"""

	time.sleep(300)
