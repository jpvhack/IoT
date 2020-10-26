import serial
import re
import io
import sys
import datetime
import cayenne.client
import time

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME = "5d3f4490-0df8-11eb-8779-7d56e82df461"
MQTT_PASSWORD = "8d670da73d36bf66f3fbe40e54af3028a1e8c526"
MQTT_CLIENT_ID = "e98a13e0-0f9b-11eb-883c-638d8ce4c23d"

# The callback for when a message is received from cayenne.
def on_message(message): print ("Mensaje recibido: " + str(message))

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

client.on_message = on_message

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.5)
regex=re.compile("[0-9]{2}\.[0-9]{2}")

while True:
 
    try:
        client.loop()
        data = ser.readline().decode('utf-8').rstrip()
        print(data)

        if "Temp" in data:
#            client.virtualWrite(1,str(datetime.datetime.now())+';')
            client.virtualWrite(1,regex.findall(str(data))[1]+"\n")
        if "Hum" in data:
#             client.celsiusWrite(2,str(datetime.datetime.now())+';')
             client.celsiusWrite(2,regex.findall(str(data))[0]+"\n")

    except KeyboardInterrupt:
        break

    time.sleep(15)
