# Smart-Baby-Monitor--IoT-Project
# Smart Baby Monitor with Python,IBM Watson(MQTT) and AWS MySql 

 Smart Baby Monitor consists of Six components: 

     1. activities - contains definitions for all the functions created for Rpi to capture sensor data and take appropriate action.

     2. dbConnect - used to to establish connection with the AWS MySql to upload the data on the AWS cloud 

     3. ibmWatson - used to connect Rpi to IBM Watson to create a dashbaord for baby monitor.

     4. notification - contains the sms and email settings required to be sent according to the sensor data captured and analysed by Rpi

     5. sensors - contains the information regarding all the sensors which is required for sensor deployement in the progam

     6. main - contains function calls already defined in activities to check for baby movements, sounds, body temperature ,and room  temperature & humdidity.

## Pre-requisites

    ### Python Libraries required :
    	1. pymysql - To connect and create database on AWS RDS MySql
    	2. Twilio - To send sms notification to a phone number
    	3. paho mqtt - To send sensor data from Rpi to IBM Watson dashboard
    	4. NodeRed - To display data on local interface

    ### HARDWARE REQUIREMENTS :

    	Rpi and GrovePi plus
			
			### GrovePi Sensors : 

    			1. DHT11 - To capture room temperature and humidity
    			2. Ultrasonic Ranger - To capture motion
    			3  Sound - To capture sound
    			4. BioMedical Sensor - to capture body temperature
    			5. Button - to capture input from the user after an action has been taken

			### GrovePi Actuators :

    			1. Green LED - To represent normal temperature 
    			2. Blue LED - To represent that baby has fever 
    			3. RED LED - To represent that baby has fever and needs to be taken to a doctor
    			4. Buzzer - TO notify user to take action 
    			5. LCD - To display all the relevant notifications

# Demo of Smart Baby MOnitor
    

    1. python main.py - Launch main.py in terminal with rest of the all files imported. Keep all the files in the same folder as main.py

    	Operations Performed:

    	1. tempHum - measures the room temperature and humidity and displayed on LCD, IBM Dashboard and Node-red
    	2. babyCry - measures the sound of the baby and based on the decibel value we can analyse if baby is in stress or not
    	3. babyMovements - measures the motion of the baby and based on the value we can analyse that the baby is awake and moving 
    	4. bodyTemp - measures the body temperature of the sick baby and notifies parents/user
    	5. medGiven - sends notification in case the baby needs attention in terms of administring medicine or consulting a doctor for further treatment.


### 
    
    Data will be displayed on the IBM Watson Dashbaord and also on the node-red interface

    Email and SMS notifications will be sent to the user.

    LCD will also display same messages.

    MySql will send the cumulative data to the user in email recorded for three consecutive days 

