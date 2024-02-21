import paho.mqtt.client as mqtt
import time
import json

#add broker address here in context to compose(service name)
broker_address = "mqttbroker"
mqtt_port = 1883

def on_publish(client,data,result):
    try:
        #print result
        if result>0:
            print(f"Message is published {result} times")
        else:
            print("Failed to send message")
    except Exception as e:
        print("Exception in on publish method",e)

def main_handler(sample_unit):
    #Create MQTT client
    mqtt_client = mqtt.Client()
    #Register callback
    mqtt_client.on_publish= on_publish
    mqtt_client.connect(broker_address,mqtt_port)

    #call the publish

    topic_name = "cdac/diot/temp"
    temp_reading = 11
    humi_reading = 50
    for reading_publish in range(sample_unit):
        sensor_data={
            "temperature":temp_reading+reading_publish,
            "humidity":humi_reading+reading_publish,
        }
        mqtt_client.publish(topic_name,json.dumps(sensor_data))
        print("Info : Published message",sensor_data)
        time.sleep(5)

 
sample_unit=40
main_handler(sample_unit)