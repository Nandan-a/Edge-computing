Networking with standalone containers
Docker by default uses the bridge network
https://docs.docker.com/network/network-tutorial-standalone/
---------------------------------------------------

BHIoT$ docker network ls
NETWORK ID     NAME                   DRIVER    SCOPE
809621412d68   09-08-2022_default     bridge    local
e4ec6c81118d   application3_default   bridge    local
fa83f8e759d4   bridge                 bridge    local
c75eefcbe8ef   compose-demo_default   bridge    local
2e7d18cfca3e   docker_gwbridge        bridge    local
1ed104b0b19b   host                   host      local
03dcd0e6bf12   none                   null      local
-------------------------------------------------------

BHIoT$ docker container ls -a | head -4
CONTAINER ID   IMAGE                           COMMAND                  CREATED        STATUS                        PORTS                                                                                            NAMES
533b0155e003   edgesub:mqtt                    "python mqtt_subscri…"   2 hours ago    Exited (130) 11 minutes ago                                                                                                    mqttsub

docker inspect 533b0155e003

Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "fa83f8e759d466dd038bffb6f59dd99c74b8c76a49d85b33dfd4e041be1f8160",
                    "EndpointID": "",
                    "Gateway": "",
                    "IPAddress": "",
                    "IPPrefixLen": 0,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "",
                    "DriverOpts": null
                }
            }
        }

------------------------------------------------------
While working with Bridge:
1. two container can ping between each other using container id
2. two container can not ping between each other using container name
3. Container can ping hostmachine using ip address
4. Host machine can ping to containers using container ip
-----------------------------------------------------------------------------

Use Case:

In order to communicate two or more containers via container name

Solution:

Create user defined bridge networks
--------------------------------------------------------------------------------------

docker network create --driver bridge mqtt-network


BHIoT$ docker network create --driver bridge mqtt-network
f0055edd80e8e0f6158da037e6164770c896cce7311e64d1e2e9e3e81dc2e435
--------------------------------------------------------------------------------------------
BHIoT$ docker network ls
NETWORK ID     NAME                   DRIVER    SCOPE
1ed104b0b19b   host                   host      local
f0055edd80e8   mqtt-network           bridge    local
03dcd0e6bf12   none                   null      local
--------------------------------------------------------------------------------------------
1.
Host a conatiner c1 with default bridge

BHIoT$ docker run -it --name c1 ubuntu:20.04
root@afc472dbd884:/# 

2. Host a conatiner c2 with user defined bridge
#--network (used to define network created by user)
docker run -it --name c2 --network mqtt-network ubuntu:20.04

3. Host a conatiner c3 with user defined bridge
#--network (used to define network created by user)
docker run -it --name c3 --network mqtt-network ubuntu:20.04



#run following commands on container c1,c2,c3
apt update
apt install iputils-ping
apt install net-tools

root@c310de36ddea:/# ping c2
PING c2 (172.21.0.2) 56(84) bytes of data.
64 bytes from c2.mqtt-network (172.21.0.2): icmp_seq=1 ttl=64 time=0.435 ms
64 bytes from c2.mqtt-network (172.21.0.2): icmp_seq=2 ttl=64 time=0.164 ms

root@c310de36ddea:/# ping c1
ping: c1: Temporary failure in name resolution


root@c310de36ddea:/# ping c3
PING c3 (172.21.0.3) 56(84) bytes of data.
64 bytes from c310de36ddea (172.21.0.3): icmp_seq=1 ttl=64 time=0.029 ms
64 bytes from c310de36ddea (172.21.0.3): icmp_seq=2 ttl=64 time=0.101 ms

To allow C3/c2 to ping c1 via IP 
Need to connect them into bridge network
BHIoT$ docker network connect bridge c2
BHIoT$ docker network connect bridge c3


Host networking:

https://docs.docker.com/network/host/

If you use the host network mode for a container, that container’s network stack is not isolated from the Docker host (the container shares the host’s networking namespace), and the container does not get its own IP-address allocated.

https://docs.docker.com/network/network-tutorial-host/

--network host {Lauanch conatainer with host networking}

docker run --rm -d --network host --name myapche httpd

BHIoT$ sudo netstat -neltp | grep 80
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      101        38079      1305/systemd-resolv 
tcp        0      0 127.0.0.1:8088          0.0.0.0:*               LISTEN      128        57847      10055/influxd       
tcp        0      0 127.0.0.1:42809         0.0.0.0:*               LISTEN      1000       112873     36501/Code --standa 
tcp6       0      0 :::8086                 :::*                    LISTEN      128        67592      10055/influxd       
BHIoT$ docker run --rm -d --network host --name myapche httpd
0873f459a04047f3f686bff96d52611c312458fdaf401611ca6a1be06d352284
BHIoT$ docker exec -it myapche /bin/bash
root@iot:/usr/local/apache2# 
root@iot:/usr/local/apache2# 
root@iot:/usr/local/apache2# ls
bin  build  cgi-bin  conf  error  htdocs  icons  include  logs	modules
root@iot:/usr/local/apache2# cd htdocs/  
root@iot:/usr/local/apache2/htdocs# ls
index.html
root@iot:/usr/local/apache2/htdocs# cat index.html 
<html><body><h1>It works!</h1></body></html>
root@iot:/usr/local/apache2/htdocs# 
