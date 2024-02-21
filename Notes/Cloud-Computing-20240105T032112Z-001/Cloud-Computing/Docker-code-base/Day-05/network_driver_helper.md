BHIoT$ docker network inspect bridge
[
    {
        "Name": "bridge",
        "Id": "fa83f8e759d466dd038bffb6f59dd99c74b8c76a49d85b33dfd4e041be1f8160",
        "Created": "2023-01-21T13:37:28.195869081+05:30",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "3a88faf04d12602f331338a7265662f62637bcc469e83972c79eb18c42039f04": {
                "Name": "portainer",
                "EndpointID": "fde2569d8aa01bf7fb2bcafc97197b9d92d64198f0ad9b7e4ee1b2f7b0c4f0de",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            },
            "afc472dbd88463797d52416134e57565929bf4e6303252537419e289e08291ab": {
                "Name": "c1",
                "EndpointID": "d0fbf03ad928c279125291930053fd12fe7a1051653bf86fb29f24224bbec366",
                "MacAddress": "02:42:ac:11:00:03",
                "IPv4Address": "172.17.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }
]
----------------------------------------------------------------------------
BHIoT$ docker network inspect mqtt-network
[
    {
        "Name": "mqtt-network",
        "Id": "f0055edd80e8e0f6158da037e6164770c896cce7311e64d1e2e9e3e81dc2e435",
        "Created": "2023-01-21T14:24:53.461929223+05:30",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.21.0.0/16",
                    "Gateway": "172.21.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "9f0751d5a4ece88a36c3986d843782913864e2fccd230d08966b828390bce33c": {
                "Name": "c2",
                "EndpointID": "8bfe52f31308e995344e9c27ff589cca9b27de0822834791cb345bfa992e72c7",
                "MacAddress": "02:42:ac:15:00:02",
                "IPv4Address": "172.21.0.2/16",
                "IPv6Address": ""
            },
            "c310de36ddeafbaac828660c40c771cbd845a29eaeb4aa82e0f628125f0c9cf5": {
                "Name": "c3",
                "EndpointID": "39cd2736b3acb0d5c71ef972a96a3958a4ab29eff186c159158d5877e28a2a7a",
                "MacAddress": "02:42:ac:15:00:03",
                "IPv4Address": "172.21.0.3/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]

--------------------------------------
After connecting c2 and c3 into bridge

BHIoT$ docker network inspect bridge
[
    {
        "Name": "bridge",
        "Id": "fa83f8e759d466dd038bffb6f59dd99c74b8c76a49d85b33dfd4e041be1f8160",
        "Created": "2023-01-21T13:37:28.195869081+05:30",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {
            "3a88faf04d12602f331338a7265662f62637bcc469e83972c79eb18c42039f04": {
                "Name": "portainer",
                "EndpointID": "fde2569d8aa01bf7fb2bcafc97197b9d92d64198f0ad9b7e4ee1b2f7b0c4f0de",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            },
            "9f0751d5a4ece88a36c3986d843782913864e2fccd230d08966b828390bce33c": {
                "Name": "c2",
                "EndpointID": "4a626bd33af74c3112a41f9a0df99734b453d150a5782abc8876680dea265d88",
                "MacAddress": "02:42:ac:11:00:04",
                "IPv4Address": "172.17.0.4/16",
                "IPv6Address": ""
            },
            "afc472dbd88463797d52416134e57565929bf4e6303252537419e289e08291ab": {
                "Name": "c1",
                "EndpointID": "d0fbf03ad928c279125291930053fd12fe7a1051653bf86fb29f24224bbec366",
                "MacAddress": "02:42:ac:11:00:03",
                "IPv4Address": "172.17.0.3/16",
                "IPv6Address": ""
            },
            "c310de36ddeafbaac828660c40c771cbd845a29eaeb4aa82e0f628125f0c9cf5": {
                "Name": "c3",
                "EndpointID": "289085ebdd42501dde7e7cd80e9d06eee68ab6f6f36f8c0cd5ed7882166ae821",
                "MacAddress": "02:42:ac:11:00:05",
                "IPv4Address": "172.17.0.5/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {}
    }

BHIoT$ docker ps
CONTAINER ID   IMAGE                           COMMAND        CREATED          STATUS             PORTS                                                                                            NAMES
c310de36ddea   ubuntu:20.04                    "bash"         18 minutes ago   Up 18 minutes                                                                                                       c3
9f0751d5a4ec   ubuntu:20.04                    "bash"         19 minutes ago   Up 19 minutes                                                                                                       c2
afc472dbd884   ubuntu:20.04                    "bash"         22 minutes ago   Up 22 minutes                                                                                                       c1
3a88faf04d12   portainer/portainer-ce:latest   "/portainer"   5 months ago     Up About an hour   9000/tcp, 0.0.0.0:6701->8000/tcp, :::6701->8000/tcp, 0.0.0.0:6702->9443/tcp, :::6702->9443/tcp   portainer

