Reference Documentation

https://docs.docker.com/engine/reference/commandline/push/

Push Image to Docker Repo:

docker tag local-image:tagname new-repo:tagname

docker push new-repo:tagname
---------------------------------------------------------------
docker push bhupendrajmd/sept2022:tagname

docker tag local-image:tagname new-repo:tagname

BHIoT$ docker images | head -10
REPOSITORY                TAG                 IMAGE ID       CREATED         SIZE
edgesub                   mqtt                102149fcbe48   5 hours ago     924MB

docker tag edgesub:mqtt bhupendrajmd/sept2022:mqttedgesubscriber

docker push bhupendrajmd/sept2022:mqttedgesubscriber

BHIoT$ docker images | head -2
REPOSITORY                TAG                  IMAGE ID       CREATED         SIZE
bhupendrajmd/sept2022     mqttedgesubscriber   102149fcbe48   5 hours ago     924MB

BHIoT$ docker push bhupendrajmd/sept2022:mqttedgesubscriber
The push refers to repository [docker.io/bhupendrajmd/sept2022]
67cecf02b5f1: Pushed 
66a38d4290a8: Pushed 
cb373edc6104: Pushed 
feabd2dd0e56: Mounted from library/python 
c2ec8127e8c2: Mounted from library/python 
338bbbbdac03: Mounted from library/python 
9e550b4f0ddf: Mounted from library/python 
b9b05a3855c6: Mounted from library/python 
132e6b0c0edd: Mounted from library/python 
d5ce45249ce1: Mounted from library/python 
b7392dc58749: Mounted from library/python 
083aacb889b3: Mounted from library/python 
mqttedgesubscriber: digest: sha256:485a595da7547365bd218acac90b216e2825e5b9503a0b51a9f66f8232e7b77d size: 2844

-----------------------------------------------------------

docker pull bhupendrajmd/sept2022:mqttedgesubscriber


