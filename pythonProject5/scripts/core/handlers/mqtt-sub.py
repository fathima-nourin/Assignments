import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("pick-count")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect("localhost", 1883)  # Replace with your MQTT broker address and port

mqtt_client.loop_forever()
