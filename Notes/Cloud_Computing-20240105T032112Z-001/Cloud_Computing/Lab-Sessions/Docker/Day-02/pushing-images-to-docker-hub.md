# Reference

https://docs.docker.com/engine/reference/commandline/push/

# Go to Docker Hub and Create A Repository (Command to be used for pushing images with example)

docker push bhupendrajmd/diot23:tagname

# Tag Docker image 

docker image tag <localimagename:tag> <dockerhubrepousername/repositoryname>

#  Tag Docker image

docker image tag hello-diot:v1 bhupendrajmd/diot23

# Push Docker Image

# docker image push <local tagged image with repo> or docker push

docker image push bhupendrajmd/diot23


BHIoT$ sudo docker image tag hello-diot:v1 bhupendrajmd/diot23:v1


BHIoT$ sudo docker push bhupendrajmd/diot23:v1
The push refers to repository [docker.io/bhupendrajmd/diot23]
762298d60f73: Layer already exists 
4738ac7233a7: Layer already exists 
59c56aee1fb4: Layer already exists 
v1: digest: sha256:bb4fdcf21a63b8ff14ad1cc90d295e979c42650d405c48dd6a32ae3e95b0cf5b size: 951

------------------------------------------------------------------------------------------------------
docker images 
REPOSITORY                       TAG       IMAGE ID       CREATED          SIZE
bhupendrajmd/diot23              latest    58fafd213f87   31 minutes ago   121MB
bhupendrajmd/diot23              v1        58fafd213f87   31 minutes ago   121MB
hello-diot                       v1        58fafd213f87   31 minutes ago   121MB

# ------------- Pulling from Docker Hub------------------------------------------------

BHIoT$ docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
BHIoT$ sudo docker run -it bhupendrajmd/diot23:v1
Unable to find image 'bhupendrajmd/diot23:v1' locally
v1: Pulling from bhupendrajmd/diot23
9d19ee268e0d: Already exists 
f385ec9ce64a: Already exists 
b8f1bebdd728: Already exists 
Digest: sha256:bb4fdcf21a63b8ff14ad1cc90d295e979c42650d405c48dd6a32ae3e95b0cf5b
Status: Downloaded newer image for bhupendrajmd/diot23:v1
Hello from DIoT 2023
