import time
import paho.mqtt.client as paho
import json

broker_address = "10.20.1.95"


def on_message(client, userdata, message):
    time.sleep(1)
    #print("received message =",str(message.payload.decode("utf-8")))
    F = json.loads(str(message.payload.decode()))
    print("StudentID: ", F["StudentID"])
    print("Name: ", F["Name"])
    print("Surname: ", F["Surname"])
    print("telephone: ", F["telephone"])
    print("Grade: ", F["Grade"])


client = paho.Client()
client.on_message = on_message
print("connecting to broker ", broker_address)
client.connect(broker_address)
client.loop_start()
print("subscribing ")
client.subscribe("se443/midterm2")
while (True):
    client.on_message = on_message
