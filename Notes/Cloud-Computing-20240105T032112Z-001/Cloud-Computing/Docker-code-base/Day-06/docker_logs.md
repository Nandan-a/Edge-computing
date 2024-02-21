Docker maintains each container log on container basis

cd /var/lib/docker/containers

root@iot:/var/lib/docker/containers# 


root@iot:/var/lib/docker/containers/fc93d56b4ffaf12b50c9b02eb7581be0be38b6e98abfbc684a278e49cd7b3c37# ls
checkpoints                                                                hostconfig.json  mounts
config.v2.json                                                             hostname         resolv.conf
fc93d56b4ffaf12b50c9b02eb7581be0be38b6e98abfbc684a278e49cd7b3c37-json.log  hosts            resolv.conf.hash
root@iot:/var/lib/docker/containers/fc93d56b4ffaf12b50c9b02eb7581be0be38b6e98abfbc684a278e49cd7b3c37# cat fc93d56b4ffaf12b50c9b02eb7581be0be38b6e98abfbc684a278e49cd7b3c37-json.log 
{"log":"Hello From PG-DIoT 222\r\n","stream":"stdout","time":"2022-08-13T09:20:27.608657035Z"}
root@iot:/var/lib/docker/containers/fc93d56b4ffaf12b50c9b02eb7581be0be38b6e98abfbc684a278e49cd7b3c37# 


#To check logs of running containers


sudo docker logs -f <containerid/name>

Example:

docker logs -f portainer





