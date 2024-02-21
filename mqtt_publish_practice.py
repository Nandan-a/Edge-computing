import paho.mqtt.client as mq_client
import json
import broker_details


def connect_to_broker(topic,port):
    global mqtt_client
    mqtt_client = mq_client.Client()
    mqtt_client.on_publish=on_publish
    mqtt_client.connect(topic,port)



def on_publish(client,userdata,count):
    if count>0:
        print(f"Published {count} times")
    else:
        print("Failed to publish data")


def send_data():
    
