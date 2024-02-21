import paho.mqtt.client as mqtt_client
import json
import uuid                         #universally unique identifier
import ardino_config
import sql_arduino


def on_connect(client,userdata,flags,rc):
    try:
        print("Connected with result code "+str(rc))            #Subscribing in on_connect means that if we lose the connection and reconnect then subscriptions will be renewed
        client.subscribe(ardino_config.publisher_topic)

    except Exception as e:
        print("Exception in Subscriber block " + e)


def on_message(client,userdata,msg):
    try:
        # print(msg.payload.decode())
        data_cleaning= msg.payload.decode()
        data_in_json_format=json.loads(data_cleaning)
        # print(data_in_json_format["temperature"])
        temperature_t = data_in_json_format["temperature"]
        humidity_t = data_in_json_format["humidity"]
        # print(temperature_t)
        values = (temperature_t,humidity_t)
        sql_arduino.insert_data_table(values)


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
        client.connect(ardino_config.broker_address,ardino_config.mqtt_port,ardino_config.keep_alive)

        client.loop_forever()


    except Exception as e:
        print("Exception in main",e)

main_handler()