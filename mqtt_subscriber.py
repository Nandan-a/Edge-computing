import paho.mqtt.client as mqtt_client
import json
import uuid                         #universally unique identifier
import broker_config
import sql_connect_edge
import mysql.connector

def on_connect(client,userdata,flags,rc):
    try:
        print("Connected with result code "+str(rc))            #Subscribing in on_connect means that if we lose the connection and reconnect then subscriptions will be renewed
        client.subscribe("cdac/diot/temp")
        


    except Exception as e:
        print("Exception in Subscriber block " + e)


def on_message(client,userdata,msg):
    try:
        print(msg.topic+" "+str(msg.payload))
        print("Data received",msg.payload.decode())
        data_cleaning= msg.payload.decode()
        data_in_json_format=json.loads(data_cleaning)
        print(data_in_json_format)
   

        temperature_data = str(data_in_json_format['temperature'])
        humidity_data = str(data_in_json_format['humidity'])
        door_status_data = data_in_json_format['door_status']
        window_status_data = data_in_json_format['window_status']
        # values = (temperature_data,humidity_data,door_status_data,window_status_data)
        # sql_connect_edge.insert_data_table(temperature_data,humidity_data,door_status_data,window_status_data)


    except Exception as e:
        print("Exception occured "+e)





def main_handler():
    try:
        #creating client id using uuid package
        mqtt_client_id=uuid.uuid4().hex
        client = mqtt_client.Client(client_id=mqtt_client_id)



        client.username_pw_set(username="diot",password="diot123")
        client.on_connect=on_connect
        client.on_message = on_message
        client.connect(broker_config.broker_address,broker_config.mqtt_port,broker_config.keep_alive)

        client.loop_forever()

    except Exception as e:
        print("Exception in main",e)

main_handler()