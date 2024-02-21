coap://host/api/v1/$ACCESS_TOKEN/telemetry

coap://demo.thingsboard.io/api/v1/{Acesstoken}/telemetry

{"temp":20, "humidity":87}

cat sensor_data.json | coap post coap://demo.thingsboard.io/api/v1/ABC123/telemetry


https://thingsboard.io/docs/reference/coap-api/

apt update
apt install net-tools
apt install iputils-ping

ping <hostip>   // container is able to ping to host machine

container 1 is able to able to ping container 2 with container ip

but fail to communicate via container name

#you can get details baout a cotainer
docker inspect <containerid> 

#docker network ls
default network - bridge

BHIoT$ mosquitto_pub -t cdac/acts -h 192.168.77.206 -p 1883 -d -l
Client null sending CONNECT
Client null received CONNACK (0)
^C

BHIoT$ mosquitto_pub -i pub -t cdac/acts -h 192.168.77.206 -p 1883 -d -l
Client pub sending CONNECT
Client pub received CONNACK (0)


https://projects.eclipse.org/projects/iot.mosquitto

https://mosquitto.org/man/mosquitto-8.html

Important

In version 1.6.x and earlier, the listener defined by -p (or the default port of 1883) would be bound to all interfaces and so be accessible from any network. It could also be used in combination with -c.

From version 2.0 onwards, the listeners defined with -p are bound to the loopback interface only, and so can only be connected to from the local machine. If both -p is used and a listener is defined in a configuration file, then the -p options are IGNORED.

-----------------------------------------------------------------
Use Case:

1. Install mosquitto-clients utility in container
2. Use Host broker address
3. Subscriber on the host machine env

