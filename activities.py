

#**********Project TCS573 - Group 12***************#
#**********Sumitha Ravindran          *************#
#**********Simerpreet Kaur            *************#

# This file contains the definitions of the activities #
# that are being carried out by the Monitor - i.e. Checking #
# for room temperature and humidity,baby's body temperature, #
# baby sounds and movements and also notifies the caregiver #
# to take action in case baby is sick #


from sensors import *			 # contains port details of the sensors attacted to Rpi #
from ibmWatson import * 		 # to publish data on IBM watson dashboard #
from dbConnect import * 		 # to establish connection with MySql #
from notification import *       # to send email and sms notifications #

import json 
import math
import time

import random # to simulate body temperature values in Farenheit #

status = {
 'babyMoving' : "Baby is moving in the cradle",
 'sleeping': "Baby is sleeping",
 'medgiv':"Medicine Given",
 'babyCry': 'Baby is CRYING',
 'babyGood': 'Baby is CALM',
 
 'SMS': {
	'tempNormal': "Baby is ok",
	'tempHigh': "Take baby to doctor",
	'tempMedicine': "Give medicine to the baby"
 },
 'Email': {
	'tempNormal': "Baby is ok, you can relax",
	'tempHigh': "Take baby to the doctor immediately",
	'tempMedicine': "Give medicine to the baby, he is having fever"
 }
}

previousTime=0
TEMP_COUNT =0

# This function will display Room Temperature and Humidity on the LCD#
def tempHum():
	[temp, hum] = dht(dhtSensor, 0)
	if ((math.isnan(temp) == False) and (math.isnan(hum) == False) and (hum >= 0)):
		print("Room Temp :" + str(temp))
		print("Room Hum :" + str(hum))
		setText("Temp" + str(temp) + "Humidity" + str(hum))
		publishToWatson({'Temperature':temp,'Humidity':hum})
		setRGB(0,128,64)

#This function will displays messages based on the data received from the Sound Sensor
def babyCry():
#using sound sensor
	sensor_value = grovepi.analogRead(sound_sensor)
	threshold_value = 300
	sensorMessage = ''
	if sensor_value > threshold_value:
		sensorMessage = status['babyCry']
	else:
		sensorMessage = status['babyGood']
		
	print(sensorMessage)
	publishToWatson({'sound_sensor':sensorMessage})

#This function will displays messages based on the data received from the Ultrasonic Ranger
def babyMovements():
#using ultrasonic ranger
	range = (grovepi.ultrasonicRead(ultrasonic_ranger))
	ultrasonicMessage = ''
	if (range < 10):
		ultrasonicMessage = status['babyMoving']
	else:
		ultrasonicMessage = status['sleeping']
	
	print(ultrasonicMessage)	
	publishToWatson({'ultrasonic_range': ultrasonicMessage})
	setRGB(64,0,128)
	setText(ultrasonicMessage)

# This function will display baby's body temperature and turn on LEDs based on the temperature level
def bodyTemp():
	global previousTime
	global TEMP_COUNT
	
	currentTempTime=time.time()
	elapsedTime=currentTempTime-previousTime
	statusSMS=''
	statusEmail=''
	giveMedicine=False
	if (TEMP_COUNT == 0):
		deleteData(mail_settings['MAIL_USERNAME'])
	
	if (elapsedTime > 10):
		val = round(random.uniform(103, 95), 1)
		print("Baby Temp:" + str(val))
		publishToWatson({'bTemperature':val})
		setRGB(64,0,128)
		previousTime = currentTempTime
		TEMP_COUNT = TEMP_COUNT +1

		if (val <= 98.6):
			del primfac[:]
			setRGB(64,0,128)
			setText("Baby's Temperature is normal "+ str(val))
			statusSMS = status['SMS']['tempNormal']
			statusEmail = status['Email']['tempNormal']
			digitalWrite(GreenLed,1)     # Send HIGH to switch on LED
			print ("Green LED ON!")
			time.sleep(0.1)

			digitalWrite(GreenLed,0)     # Send LOW to switch off LED
			print ("Green LED OFF!")
			time.sleep(0.1)

		elif (val > 98.6) and (val < 100.4):
			del primfac[:]
			setText("Baby has fever, please give medicine")
			statusSMS = status['SMS']['tempMedicine']
			statusEmail = status['Email']['tempMedicine']
			digitalWrite(BlueLed,1)     # Send HIGH to switch on LED
			print ("Blue LED ON!")
			time.sleep(0.1)

			digitalWrite(BlueLed,0)     # Send LOW to switch off LED
			print ("Blue LED OFF!")
			time.sleep(0.1)
			#giveMedicine = True

		elif (val >= 100.4):
			del primfac[:]
			setText("Baby's Temperature has exceeded the normal range, please take him immediately to the doctor")
			statusSMS = status['SMS']['tempHigh']
			statusEmail = status['Email']['tempHigh']
			# Continous buzzing
			digitalWrite(buzzer,1)
			print ('Buzzer-start')

			digitalWrite(RedLed,1)     # Send HIGH to switch on LED
			print ("Red LED ON!")
			time.sleep(0.1)

			digitalWrite(RedLed,0)     # Send LOW to switch off LED
			print ("Red LED OFF!")
			time.sleep(0.1)
			#giveMedicine = True

		publishToWatson({'textStatus':statusEmail})
		print (statusSMS)
		print (statusEmail)
		sendSMS(statusSMS + ' ' +  str(val))
		sendEmail(statusEmail + ' ' +  str(val))
		saveData(mail_settings['MAIL_USERNAME'], val, statusEmail)
		if(TEMP_COUNT%12 == 0):
			savedTempDetails = getData(mail_settings['MAIL_USERNAME'])
			print (savedTempDetails)
			sendEmail(savedTempDetails)
		if(giveMedicine == True):
			medGiven()

#This function will get input from caregiver once the medicine is given
def medGiven():
	valButton = grovepi.digitalRead(button)
	if (valButton == False):
		print ("Baby needs medicine")
		grovepi.digitalWrite(buzzer,1)
		#print ('start')
		time.sleep(1)

		# Stop buzzing for 1 second and repeat
		grovepi.digitalWrite(buzzer,0)
		#print ('stop')
		time.sleep(1)
		medGiven()

	elif (valButton == True):
		print(status['medgiv'])
		setText(status['medgiv'])
		grovepi.digitalWrite(buzzer,0)
		return
