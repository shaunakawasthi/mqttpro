import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "test.mosquitto.org"
broker_port = 1883

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Define the topic to publish to
topic = "esp32/Load"

# Define the message to publish
message = "Hello, MQTT!, I Hope You are Doing Fine"

# Publish the message
client.publish(topic, message)

print(f"Published message to topic {topic}: {message}")

# Disconnect from the MQTT broker
client.disconnect()