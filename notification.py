
#**********Project TCS573 - Group 12***************#
#**************Authors*****************************#
#**********Simerpreet Kaur (1970697) **************# 
#**********Sumitha Ravindran (1978232)*************#

# This module is used to send email and sms notifications based on the baby's body #
# temperature and asks the user to take appropriate action #

from twilio.rest import Client
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Credentials for Twilio sms service #
sms_settings = {
	'account_sid': "AC40b382ed0de1c1f09711527417039cfb",
	'auth_token': "f09a42162b02ecdce696b544470c6a0e"
}

# Credentials and settings for Gmail SMTP #
mail_settings = {
	"MAIL_SERVER": 'smtp.gmail.com',
	"MAIL_PORT": 465,
	"MAIL_USE_TLS": False,
	"MAIL_USE_SSL": True,
	"MAIL_USERNAME": '***********@gmail.com',
	"MAIL_PASSWORD": 'Testing@123'
}

# Function to send sms on the user's phone from Twilio account #

def sendSMS(body):
	client = Client(sms_settings['account_sid'], sms_settings['auth_token'])
	client.messages.create(
							from_ = "+**********",
							to = "+**********",
							body = body
						  )
# Function to send email on the user's email address #
def sendEmail(body):
	global MIMEText
	message = MIMEMultipart()
	message["Subject"] = "Baby Monitor: Temperature Details !!"
	message["From"] = mail_settings['MAIL_USERNAME']
	message["To"] = '**************@gmail.com'
	
	html = """<html><body>"""+body+"""</body></html>"""
	htmlBody = MIMEText(html, "html")
	message.attach(htmlBody)
	
	try:
		server = smtplib.SMTP_SSL(mail_settings['MAIL_SERVER'], mail_settings['MAIL_PORT'])
		server.ehlo()
		server.login(mail_settings['MAIL_USERNAME'], mail_settings['MAIL_PASSWORD'])
		server.sendmail(
				mail_settings['MAIL_USERNAME'], 
				'************@gmail.com', 
				message.as_string())
		server.close()

		print 'Email sent!'
	except Exception as e:
		print 'something went wrong'
		print (e)
