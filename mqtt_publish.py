import paho.mqtt.client as mqtt_diot
import time
import json
import broker_config
import random 
from datetime import datetime

def on_publish(client,userdata,result):
    try:
        if result>0:
            print(f"Message is published {result} times")
        else:
            print("Failed to send message")
        
    except Exception as e:
        print("Exception in 'on publish' method",e)

    

def connectivity_management(broker_address,broker_port):
    try:
        global mqtt_client                                  #Create MQTT client
        mqtt_client = mqtt_diot.Client()                       
        mqtt_client.on_publish = on_publish                 #Register callback
        mqtt_client.connect(broker_address,broker_port)     #Connect with broker

    except Exception as e:
        print(e)

def send_telemetry(sample_unit):
    try:

        temp_reading = 11
        humi_reading = 50
        

        print(broker_config.valid_door_status)
        for reading_publish in range(sample_unit):
            now = datetime.now()
            current_time=now.strftime("%H:%M:%S")
            random.shuffle(broker_config.valid_door_status),
            random.shuffle(broker_config.valid_window_status)
            sensor_data = {
                "temperature": random.randint(broker_config.valid_temperature_sensor[0],broker_config.valid_temperature_sensor[1]),
                "humidity" : random.randint(broker_config.valid_humidity_sensor[0],broker_config.valid_humidity_sensor[1]),
                "door_status" : broker_config.valid_door_status[0],
                "window_status" : broker_config.valid_window_status[0],
                "timestamp" : current_time
            }
            


            mqtt_client.publish(broker_config.publisher_topic_name,json.dumps(sensor_data))
            print("Info:Published message",sensor_data)
            time.sleep(2)
    except Exception as e:
        print(e)






def main_handler(sample_unit):

    connectivity_management(broker_config.broker_address,broker_config.mqtt_port)                   #calling function connectivity_management()
    send_telemetry(sample_unit)                                                                                #calling function send_telemetry()
    

sample_unit = 40
main_handler(sample_unit)