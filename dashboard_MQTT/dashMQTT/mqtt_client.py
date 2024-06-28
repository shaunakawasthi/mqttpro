import paho.mqtt.client as mqtt

# Global variable to store the latest MQTT message
latest_message = "No Message received yet."

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("esp32/Load")  # Replace with your actual MQTT topic

def on_message(client, userdata, msg):
    global latest_message
    latest_message = msg.payload.decode()
    print(f"Received message: {latest_message}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)  # Replace with your MQTT broker details
client.loop_start()