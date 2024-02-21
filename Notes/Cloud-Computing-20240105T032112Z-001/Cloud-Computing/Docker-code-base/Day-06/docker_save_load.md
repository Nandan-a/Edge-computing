https://docs.docker.com/engine/reference/commandline/save/

#docker save

--- command is used to create image archive.

docker save busybox > busybox.tar

docker save <imagename> > <imagename>.tar


BHIoT$ docker run -it alpine
alpine            alpine:diothello  alpine:latest     
BHIoT$ docker run -it alpine:diothello 
BHIoT$ docker run -it alpine:diothello 
Hello From the alpine developed by diot batch
BHIoT$ docker save alpine:diothello > alpine:diothello.tar


----------------------------------------------------------------

To load image in the remote machine

 docker load < busybox.tar.gz
------------------------------------------


 docker load < alpine:diothello.tar.gz


 docker images




