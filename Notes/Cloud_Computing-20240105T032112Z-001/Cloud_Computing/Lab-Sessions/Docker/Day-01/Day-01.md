"""
Getting started with Docker - DIoT Sept 2022
"""
#Installation Steps for Docker

#Link to follow:

https://docs.docker.com/engine/install/

#official web site:
-----------------------
https://docs.docker.com/


https://docs.docker.com/engine/install/ubuntu/

#install using script

https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script


 curl -fsSL https://get.docker.com -o get-docker.sh

 DRY_RUN=1 sudo sh ./get-docker.sh

#To install docker
sudo sh get-docker.sh

BHIoT$ sudo docker -v
Docker version 20.10.22, build 3a2c30b
-----------------------------------------------------------------
sudo docker service status

● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: en>
     Active: active (running) since Sat 2023-01-14 11:58:19 IST; 6min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 2469496 (dockerd)
      Tasks: 45
     Memory: 35.0M
-----------------------------------------------------------------------------------
#If docker service is masked 
systemctl unmask docker
systemctl enable docker



Post installation steps:
-------------------------------
https://docs.docker.com/engine/install/linux-postinstall/

sudo groupadd docker

sudo usermod -aG docker $USER
#Logout or login else run below command
newgrp docker

#Create the account over docker

https://hub.docker.com/signup


BHIoT$ docker login
Authenticating with existing credentials...
WARNING! Your password will be stored unencrypted in /home/bhupendra/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded


docker run hello-world

https://hub.docker.com/_/hello-world


docker pull ubuntu:20.04

#How to run it as a container

docker run -it ubuntu:20.04

#Display running cotainers

BHIoT$ docker container ls 
CONTAINER ID   IMAGE                           COMMAND        CREATED          STATUS             PORTS                                                                                            NAMES
f6fa314f9749   ubuntu:20.04                    "bash"         10 minutes ago   Up 10 minutes                                                                                                       thirsty_mirzakhani

#Execute a command inside container (Must be in running state)

You want a shell of running container

sudo docker exec -it <containerid/conatinernanem> /bin/bash

#create a directory inside the container

BHIoT$ sudo docker exec 6af5fa933455 mkdir test

#attach a container to see STDIO/STDOUT/STDERR

docker attach <containerid/containername>

-----------------------------------------------------------------------------
Docker commands:

# List docker images

docker images
docker image ls

# List running containers
docker container ls
docker ps

# List all containers (Running/Stopped/Exited)
docker container ls -a
docker ps -a


# List all containers with only container id

docker ps -a -q #docker ps -aq       (Only display container IDs) --quiet

#start the container (existed/stopped)
docker start <containerid/containername>
docker container start <containerid/containername>

#Start the container in the interactive mode

docker start -i <containerid/containername>  #will login into the shell of the container

#note down the returned conatiner id
Get the bash shell (If exist)
docker exec -it <containerid/containername> /bin/bash

# list the container with size

docker container ls -s

BHIoT$ docker container ls -s
CONTAINER ID   IMAGE          COMMAND   CREATED          STATUS          PORTS     NAMES                  SIZE
a1d0cf784047   ubuntu:20.04   "bash"    54 minutes ago   Up 54 minutes             xenodochial_bhaskara   0B (virtual 72.8MB)
b878d6b2a448   ubuntu:20.04   "bash"    5 months ago     Up 45 hours               devubuntu2             52B (virtual 72.8MB)
91554c8dd624   ubuntu:20.04   "bash"    5 months ago     Up 45 hours               devubuntu              27B (virtual 72.8MB)

-- OB representes Physical size (Seconday Storage)


#how to create named container

sudo docker run --name diot_v0 -it ubuntu:20.04

BHIoT$ sudo docker container ls
CONTAINER ID   IMAGE                           COMMAND        CREATED              STATUS              PORTS                                                                                            NAMES
bddd93c617ff   ubuntu:20.04                    "bash"         About a minute ago   Up About a minute                                                                                                    diot_v0

# Process to create a Image from a container

1. create a container from some image 
2. add changes (install package/create file etc.)
3. stop the container
4. create a image from container using docker commit

BHIoT$ sudo docker run --name myubntu_20.04 -itd ubuntu:20.04
6385527c7c351af61d3b9db68d8442b9c2574bd0558d6a20b0651d34b91090ca
BHIoT$ sudo docker exec -d mkdir testfolder
Error: No such container: mkdir
BHIoT$ sudo docker exec -d myubntu_20.04 mkdir testfolder
-----------------------------------------------------------------------------------------------------------------------
# How to rename a container

docker rename <cid> <newname>

BHIoT$ docker ps -a | head -2
CONTAINER ID   IMAGE                           COMMAND                  CREATED         STATUS                       PORTS                                                                                                                                                                                            NAMES
72141a57e0da   ubuntu:20.04                    "bash"                   2 hours ago     Exited (0) 2 hours ago                                                                                                                                                                                                        sleepy_taussig
BHIoT$ docker rename 72141a57e0da testdiot23
BHIoT$ docker ps -a | head -2
CONTAINER ID   IMAGE                           COMMAND                  CREATED         STATUS                       PORTS                                                                                                                                                                                            NAMES
72141a57e0da   ubuntu:20.04                    "bash"                   2 hours ago     Exited (0) 2 hours ago                                                                                                                                                                                                        testdiot23
---------------------------------------------------------------------------------------------------------------------------

# Attach local standard input, output, and error streams to a running container

BHIoT$ sudo docker attach myubntu_20.04 
root@6385527c7c35:/# ls
bin   dev  home  lib32  libx32  mnt  proc  run   srv  testfolder  usr
boot  etc  lib   lib64  media   opt  root  sbin  sys  tmp         var
root@6385527c7c35:/# cd testfolder/
root@6385527c7c35:/testfolder# ls
root@6385527c7c35:/testfolder# 

-----------------------------------------------------------------------------
# How to create Image from a container changes 

# Example :

docker commit --author <authorname> <cid/cname> <imagename:tag>


# Some operations for deletion

# Delete a container

docker rm <contanerid/cname>

# for multiple

docker rm <containerid/cname> <containerid/cname> 


# Remove a container forcefully

docker rm --force <containerid/cname> 

docker rm -f <containerid/cname> 


# Remove all containers   (Linux Technique to use $ for getting variable value) (This works will all listing and deletion related cmds)

docker rm $(docker ps -a -q)

# Remove a Docker Image

docker rmi <imagename/imageid>

docker rmi -f <imagename/imageid>
-----------------------------------------------------------------------------------------

Example:

BHIoT$ docker ps
CONTAINER ID   IMAGE          COMMAND   CREATED         STATUS         PORTS     NAMES
656b68615ff8   ubuntu:20.04   "bash"    2 minutes ago   Up 2 minutes             priceless_haibt
b878d6b2a448   ubuntu:20.04   "bash"    5 months ago    Up 2 days                devubuntu2
91554c8dd624   ubuntu:20.04   "bash"    5 months ago    Up 2 days                devubuntu
BHIoT$ docker com
commit   compose  
BHIoT$ docker com
commit   compose  
BHIoT$ docker commit --author diot23 656b68615ff8 mqttifconfig:ubuntu
sha256:25e6bce481102afbc569a8a1839e2154a89a72e1822c80d0e330bd68b41e4d5b
BHIoT$ docker images | head -2
REPOSITORY                  TAG                  IMAGE ID       CREATED         SIZE
mqttifconfig                ubuntu               25e6bce48110   9 seconds ago   101MB



BHIoT$ docker commit apache_server apcheserver:v0
sha256:64c8370a5ec15ed487e3afdf1e5c582862962fb69b02b830fdabe24d936537f3

BHIoT$ docker images | head -3
REPOSITORY                TAG              IMAGE ID       CREATED          SIZE
apcheserver               v0               1b73cdf5f950   10 seconds ago   227MB
<none>                    <none>           64c8370a5ec1   17 seconds ago   227MB

BHIoT$ docker rmi 64c8370a5ec1
Deleted: sha256:64c8370a5ec15ed487e3afdf1e5c582862962fb69b02b830fdabe24d936537f3

BHIoT$ docker images | head -5
REPOSITORY                TAG              IMAGE ID       CREATED          SIZE
apcheserver               v0               1b73cdf5f950   48 seconds ago   227MB
ubuntu                    20.04            d5447fc01ae6   5 weeks ago      72.8MB
ubuntu                    22.04            2dc39ba059dc   4 months ago     77.8MB
application3_publisher    latest           5d999f8b332c   5 months ago     916MB

# Launching a web server (for example Apache)

BHIoT$ docker run -it -p 5600:80 --name apachec apcheserver:v0  
root@6d4168123fd5:/# service apache2 status
 * apache2 is not running
root@6d4168123fd5:/# service apache2 start 
 * Starting Apache httpd web server apache2                                                              AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.17.0.3. Set the 'ServerName' directive globally to suppress this message
 * 
root@6d4168123fd5:/# service apache2 status
 * apache2 is running
root@6d4168123fd5:/# cat /var/www/html/index.html 
 <!DOCTYPE html>
<html>
<head>
<title>container web page</title>
</head>
<body>
<h1>Cloud Computing- Docker Introduction</h1>
<p>Lets map the services that are running inside the container</p>
</body>
</html> 


#Assignment
--------------------
1. Create a container from ubuntu 20.04 named as ubuntu_base
2. Install mosquitto broker
3. create the image from container and name it as ubuntu:mosquitto
4. map the mosquitto broker port (running under container) to host port on 6500
5. publish the message to the broker and subscribe to this
-------------------------------------------------------------------------------------

Publisher with higher QOS and subscriber with lower QOS
------------------------------------------------------------
BHIoT$ mosquitto_pub -t dht22/sensor/temperature --qos 2 -h localhost -p 1883 -l -d
Client null sending CONNECT
Client null received CONNACK (0)
--------
#PUB

BHIoT$ mosquitto_pub -t dht22/sensor/temperature --qos 2 -h localhost -p 1883 -l -d
Client null sending CONNECT
Client null received CONNACK (0)
12c
Client null sending PUBLISH (d0, q2, r0, m1, 'dht22/sensor/temperature', ... (3 bytes))
Client null received PUBREC (Mid: 1)
Client null sending PUBREL (m1)
Client null received PUBCOMP (Mid: 1, RC:0)
-----------------------------------------------
#Sub
BHIoT$ mosquitto_sub -t dht22/sensor/temperature --qos 1 -h localhost -p 1883 -d
Client null sending CONNECT
Client null received CONNACK (0)
Client null sending SUBSCRIBE (Mid: 1, Topic: dht22/sensor/temperature, QoS: 1, Options: 0x00)
Client null received SUBACK
Subscribed (mid: 1): 1
Client null received PUBLISH (d0, q1, r0, m1, 'dht22/sensor/temperature', ... (3 bytes))
Client null sending PUBACK (m1, rc0)
12c

Publisher with lower QOS and subscriber with higher QOS
-----------------------------------------------------------
#PUB
BHIoT$ mosquitto_pub -t dht22/sensor/temperature --qos 1 -h localhost -p 1883 -l -d
Client null sending CONNECT
Client null received CONNACK (0)
45c
Client null sending PUBLISH (d0, q1, r0, m1, 'dht22/sensor/temperature', ... (3 bytes))
Client null received PUBACK (Mid: 1, RC:0)

#SUB
BHIoT$ mosquitto_sub -t dht22/sensor/temperature --qos 2 -h localhost -p 1883 -d
Client null sending CONNECT
Client null received CONNACK (0)
Client null sending SUBSCRIBE (Mid: 1, Topic: dht22/sensor/temperature, QoS: 2, Options: 0x00)
Client null received SUBACK
Subscribed (mid: 1): 2
Client null received PUBLISH (d0, q1, r0, m1, 'dht22/sensor/temperature', ... (3 bytes))
Client null sending PUBACK (m1, rc0)
45c

#Remember:
---------------------------------------------------------------------------------------
- A message published with Higher QOS can be received  by the subscriber with lower QOS (if sub request to)
- A message published with Lower QOS can not be received  by the subscriber with higher QOS (if sub request to)
-------------------------------------------------------------------------------------
