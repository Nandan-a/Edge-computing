#sample https://github.com/aschiffler/python-mqtt
#https://github.com/eclipse/paho.mqtt.python
# The callback for when the client receives a CONNACK response from the server.
"""
Developed for PG-DESD, ACTS Student (2023 Batch)
@maintainer : bhupendra.jmd@gmail.com
MQTT subscriber client
pip3 install paho-mqtt
"""
import paho.mqtt.client as mqtt
import uuid
import time
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
"""
Server configuration Details
"""
sql_server_hostname = os.getenv("SQL_SERVER_ADDRESS")
database_user_name = os.getenv("DATABASE_USER_NAME")
database_password = os.getenv("DATABASE_PASSWORD")
mysql_database_name = os.getenv("DATABASE_NAME")
temperature = None
humidity = None
try: 
    sensor_data_db = mysql.connector.connect(
    host=sql_server_hostname,
    user=database_user_name,
    password=database_password,
    database=mysql_database_name
  )
except Exception as e:
    print(e)
 
  
def on_connect(client, userdata, flags, rc):
    try:
        print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
        #subscribe(topic, qos=0)
        client.subscribe("cdac/diot/temperature")
        client.subscribe("cdac/diot/humidity")
    except Exception as e:
        print("Exception in Subscriber block",e)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    try:
        print("Msg received on topic " + msg.topic+ " "+str(msg.payload.decode()))
        if msg.topic == "cdac/diot/temperature":
            global temperature
            temperature = msg.payload.decode();
        elif(msg.topic == "cdac/diot/humidity"):
            global humidity
            humidity = msg.payload.decode()
        else:
            pass
        # creating payload for data insertion
        localtime = time.asctime( time.localtime(time.time()) )
        data_payload = {
                    "temperature_data": temperature,
                    "humidity_data" : humidity,
                    "timestamp" : localtime
                }
        #get the cursor
        mycursor = sensor_data_db.cursor()

        add_data = ("INSERT INTO diotclassroom "
                "(Temperature,Humidity,TIMESTAMP) "
                "VALUES (%s, %s,%s)")
        payload = (data_payload['temperature_data'],data_payload["humidity_data"],data_payload["timestamp"])
        mycursor.execute(add_data, payload)
        #commit the record
        mycursor = sensor_data_db.commit()
    except Exception as e:
        print("Exception in on message block",e)
try:
    mqtt_client_id=uuid.uuid4().hex
    """
    Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
    """
    client = mqtt.Client(client_id=mqtt_client_id)
    #set username and password based authentication with broker
    client.username_pw_set(username="diot",password="diot123")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
    client.loop_forever()
except Exception as e:
    print("Excption in main",e)