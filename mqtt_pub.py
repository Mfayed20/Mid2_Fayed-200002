import paho.mqtt.client as mqtt
import json

broker_address = "10.20.1.95"
client = mqtt.Client()
topic = "se443/midterm2"
x = {
    "StudentID": 200002,
    "Name": "Mohamed",
    "Surname": "Fayed",
    "telephone": "966502578964",
    "Grade": 4
}
y = json.dumps(x)
message = y
if (client.connect(broker_address, 1883, 60) == 0):
    print("Connected succesfully to "+broker_address)
    print("Published in "+topic+", msg = "+message)
client.publish(topic, message)
client.disconnect()
