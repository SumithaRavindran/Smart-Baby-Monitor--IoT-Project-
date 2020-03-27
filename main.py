

#******TCSS573 IoT Project by Group 12********** #
# ********Baby Monitor************************** #
# Authors : Sumitha                              #

# This modeule is the main module where are all the other sub-modules get integrated #
# and executed #

from ibmWatson import *
from sensors import *
from activities import *

# function to monitor the baby's activities and fever #
def startMonitoring():
	while (True):
		try:
			babyCry()         # Function to detect baby sounds
			tempHum()         # Function to measure Room temperature and Humidity
			babyMovements()	  # Function to measure baby motion in the cradle
			bodyTemp()		  # Function to measure body temperature
		except KeyboardInterrupt:
			print ("Exiting .....")
			dc()
		except IOError as e:
			print ("Error in IO")
			print (e)
		except TypeError:
			print ("TypeError")
		except IOError as IOe:
			print ("An Error has occured .%" % IOe)
		except Exception as e1:
			print ("Error in exception")
			print (e1)

startMonitoring()


