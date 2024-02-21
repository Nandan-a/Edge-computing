# How to send data of a file
- There are two ways
#  -f : send the contents of a file as the message.

# Publisher (Ensure file is in same dir else mention absolute path)

mosquitto_pub -t cdac/sensor/file -h localhost -p 1883 -f sensor_data.json

# Subscriber
BHIoT$ mosquitto_sub -t cdac/sensor/file -h localhost -p 1883
{
    "place" : "Pune",
    "sensor_Details" : 
    {
        "temperature" : "DHT22",
        "humidity"    : "DHT22"
    },
    "sensor_value" : {
        "temperature" : 35,
        "humidity" : 85
    },
    "firmware_version" : 2.02
}

# Second way
#  -s : read message from stdin, sending the entire input as a message.
# Publisher (Ensure file is in same dir else mention absolute path)

mosquitto_pub -t cdac/sensor/file -h localhost -p 1883 -s < sensor_data.json

# Subscriber
BHIoT$ mosquitto_sub -t cdac/sensor/file -h localhost -p 1883
{
    "place" : "Pune",
    "sensor_Details" : 
    {
        "temperature" : "DHT22",
        "humidity"    : "DHT22"
    },
    "sensor_value" : {
        "temperature" : 35,
        "humidity" : 85
    },
    "firmware_version" : 2.02
}


