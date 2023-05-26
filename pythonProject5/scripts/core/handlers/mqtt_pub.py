from fastapi import FastAPI
from scripts.schemas import Inventory
import json
import paho.mqtt.client as mqtt


# app = FastAPI()
# inventory = Inventory()
#
# mqtt_broker = "localhost"
# mqtt_port = 1883
# mqtt_topic = "item/picks"
#
# # Create an MQTT client
# mqtt_client = mqtt.Client()
# mqtt_client.connect(mqtt_broker, mqtt_port)  # Connect to the MQTT broker
# message = f"Item {inventory.id} count: {inventory.count}"  # Publish the updated count to MQTT
# mqtt_client.publish(mqtt_topic, message)
# mqtt_client.disconnect()

class Publisher:

    def __init__(self, host, port, topic):
        self.host = host
        self.port = port
        self.topic = topic
        self.mqtt_client = mqtt.Client()

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print("Failed to connect, return code: " + str(rc))

    def publish(self, message: str):
        try:
            self.mqtt_client.on_connect = self.on_connect
            self.mqtt_client.connect(self.host, self.port, 60)
            self.mqtt_client.publish(self.topic, message)
            return {"message": "Published message"}
        except Exception as e:
            raise Exception(str(e))
