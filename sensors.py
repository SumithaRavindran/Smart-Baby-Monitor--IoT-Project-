
#**********Project TCS573 - Group 12***************#
#**************Authors*****************************#
#**********Simerpreet Kaur           **************# 
#**********Sumitha Ravindran          *************#
from grovepi import *

# This module consists of information related to the ports to which the sensors are connected #
# It also initializes the sensors to default settings using pinMode option #

import json
import math
import time
import grovepi
from grove_rgb_lcd import *

dhtSensor = 6			# Connected DHT11 to digital port 6 for Room temperature and humidity
lcd = 1 				# Connected LCD RGB Backlight to port I2C 1
primfac = [] 			# to clear LCD display for the next notification
GreenLed = 4 			# Connected Green LED to digital port 4
BlueLed = 5 			# Connected Blue LED to digital port 5
RedLed = 7 				# Connected Red LED to digital port 7
ultrasonic_ranger = 2 	# Connected motion sensor to digital port 2
buzzer = 8 				# Connected buzzer to digital port 8
button = 3 				# Connected butoon to digital port 3
sound_sensor = 2

# defines the OUTPUT mode for actuators #

grovepi.pinMode(GreenLed,"OUTPUT") 
grovepi.pinMode(BlueLed,"OUTPUT") 
grovepi.pinMode(RedLed,"OUTPUT") 
grovepi.pinMode(buzzer,"OUTPUT") 

# defines the INPUT Mode for the sensors #

grovepi.pinMode(button,"INPUT")
pinMode(sound_sensor,"INPUT")
