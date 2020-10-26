#!/usr/bin/python
import Adafruit_DHT
import cayenne.client
import time

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME = "5d3f4490-0df8-11eb-8779-7d56e82df461"
MQTT_PASSWORD = "8d670da73d36bf66f3fbe40e54af3028a1e8c526"
MQTT_CLIENT_ID = "9a191e40-0df8-11eb-883c-638d8ce4c23d"

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

# Sensor should be set to Adafruit_DHT.DHT11,
sensor = Adafruit_DHT.DHT11
pin = 18

while True:
 client.loop()
 humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
 if humedad is not None and temperatura is not None:
 	print('temperatura={0:0.1f}*C humedad={1:0.1f}%'.format(temperatura, humedad))
 	client.celsiusWrite(1, temperatura)
 	client.virtualWrite(2, humedad)

 else:
 	print('Fallo en la lectura. Prueba otra vez!')
