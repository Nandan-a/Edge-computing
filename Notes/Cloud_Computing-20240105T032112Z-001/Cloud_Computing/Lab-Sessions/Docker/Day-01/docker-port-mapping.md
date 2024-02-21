# connect container from host 

BHIoT$ mosquitto_pub -t cdac/acts -h 172.17.0.4 -p 1883 -d -l
Client null sending CONNECT
Client null received CONNACK (0)
^C

# Challenge Dynamic nature of container IP(S)

-- Map the port numbers

host:port

# Official Apache web server image

ubuntu/apache2

# Spin the container

docker run -d --name apache2-container -e TZ=UTC -p 8080:80 ubuntu/apache2

# Here 8080 is host port number
# and 80 is port number
-------------------------------------------------------------------------------------
# What can be customized

-- host port number

# For example expose the container on host machine at port number 6502

docker run -d --name apache2-container -e TZ=UTC -p 6502:80 ubuntu/apache2


# To get the shell

docker exec -it apache2-container /bin/bash






