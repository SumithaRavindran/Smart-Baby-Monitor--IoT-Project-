#**********Project TCS573 - Group 12***************#
#**********Sumitha Ravindran          *************#
#**********Simerpreet Kaur            *************#

# This file assists to connect to IBM Watson Platform #


import paho.mqtt.client as mqtt
import json

# IBM Watson details to establish connection and publish data #
watson_details = {
    'host': 'euag1a.messaging.internetofthings.ibmcloud.com',
    'clientid': 'd:euag1a:Sensors:tempHumSensor',
    'username': 'use-token-auth',
    'password': 'HTxv+Lp)kac&P@LdEN',
    'topic': 'iot-2/evt/temperature/fmt/json'
}

client = mqtt.Client(watson_details['clientid'])
client.username_pw_set(watson_details['username'], watson_details['password'])
client.connect(watson_details['host'], 1883, 60)

def dc():
    client.disconnect()
  
def publishToWatson(data):
    client.publish(
        watson_details['topic'], 
        json.dumps(data)
    )
   




