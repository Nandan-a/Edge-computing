https://docs.docker.com/engine/reference/builder/

What is Dockerfile?
-- set of instructions example
FROM
ADD
MAINTAINER
COPY
CMD
RUN
--------------------------------------------------
-- file must be created with name Dockerfile without any extension 

Steps to follow to create container from Dockerfie

Step1:
Create the Dockerfile write the instructions
Step2:
Create the Docker image (Build)

#Command

-t > tag name (referred as image name)
ubuntu (image name)
diothello (tag name)
if tag name is not given by default it will be tagged as latest

docker build -t <imagename:tag> <Dockerfile path (. represent current dir)>

docker build -t ubuntu:diothello .

List the new build image:

docker images | head -3

#Run it as a container
#get the shell
docker run -it --name diothelloc ubuntu:diothello

or

docker run -it --name diothelloc ubuntu:diothello /bin/bash

#only prints stdout and exit

docker run --name myhelloc ubuntu:diothello 

Example:

BHIoT$ docker run --name myhelloc ubuntu:diothello 
Hello from DIoT-2022


#FROM Instruction
#The FROM instruction initializes a new build stage and sets 
#the Base Image for subsequent instructions. 
FROM ubuntu:22.04
RUN apt update -y
RUN apt install net-tools
CMD ["echo", "Hello from DIoT-2022"]
------------------------------------------------------------------------
Working with Alpine os

https://hub.docker.com/_/alpine
https://docs.alpinelinux.org/user-handbook/0.1a/index.html

https://www.cyberciti.biz/faq/10-alpine-linux-apk-command-examples/

#How to check service in alpine
 # apk add openrc
(1/3) Installing ifupdown-ng (0.12.1-r0)
(2/3) Installing openrc (0.44.10-r7)
Executing openrc-0.44.10-r7.post-install
(3/3) Installing mosquitto-openrc (2.0.14-r2)
Executing busybox-1.35.0-r15.trigger
OK: 9 MiB in 22 packages
------------------------------------------------------------------
/ # rc-service status mosquitto
 * rc-service: service `status' does not exist
/ # rc-service mosquitto status
 * You are attempting to run an openrc service on a
 * system which openrc did not boot.
 * You may be inside a chroot or you may have used
 * another initialization system to boot this system.
 * In this situation, you will get unpredictable results!
 * If you really want to do this, issue the following command:
 * touch /run/openrc/softlevel
/ # touch  /run/openrc/softlevel
---------------------------------------------------------------------
https://www.cyberciti.biz/faq/how-to-enable-and-start-services-on-alpine-linux/



