import time
import datetime
from influxdb import InfluxDBClient
import random
"""
Configure database credentails
"""
host = "localhost"     
port = 8086
user = "diot"
password = "diot1234"
interval = 10  #update the data at every 10 seconds
dbname = "data-logger"
#Create the InfluxDB client Object
client = InfluxDBClient(host,port,user,password,dbname)
#create Measurement
measurement = "hall-temperature"
#create tag
location = "pune"
try:
    while True:
        #Random Number
        #    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        temperature = random.randint(-10,50)
        humidity = random.randint(60,90)
        iso = time.ctime()
        data= [
            {
            "measurement" : measurement,
            "tags": {
                "location" : location
            },
            "time" : iso,
            "fields":{
                    "temperature" : temperature,
                    "humidity" : humidity
            }
            }
        ]
        #send/write the JSON data to InfluxDB
        client.write_points(data)
        #Add the interval
        time.sleep(interval)

except KeyboardInterrupt:
    pass

