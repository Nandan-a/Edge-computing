# Note: 

-- By default docker uses bridge networking

#List network types

BHIoT$ docker network ls
NETWORK ID     NAME                     DRIVER    SCOPE
bfd0b6316c95   bridge                   bridge    local

# How to inspect a container

docker inspect <cid/cname>


BHIoT$ docker inspect d35f26610730
[
    {
        "Id": "d35f26610730012780767482baa062aa8845bf8ba26ebe4dd7d7971e4ac933fd",
        "Created": "2023-07-22T22:13:29.906537858Z",
        "Path": "bash",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1109797,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-07-22T22:13:31.214574317Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:25e6bce481102afbc569a8a1839e2154a89a72e1822c80d0e330bd68b41e4d5b",
        "ResolvConfPath": "/var/lib/docker/containers/d35f26610730012780767482baa062aa8845bf8ba26ebe4dd7d7971e4ac933fd/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/d35f26610730012780767482baa062aa8845bf8ba26ebe4dd7d7971e4ac933fd/hostname",
        "HostsPath": "/var/lib/docker/containers/d35f26610730012780767482baa062aa8845bf8ba26ebe4dd7d7971e4ac933fd/hosts",
        "LogPath": "/var/lib/docker/containers/d35f26610730012780767482baa062aa8845bf8ba26ebe4dd7d7971e4ac933fd/d35f26610730012780767482baa062aa8845bf8ba26ebe4dd7d7971e4ac933fd-json.log",
        "Name": "/mqtt",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                23,
                84
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "host",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": false,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/dc9863e37807b9ee8b7c6bb24b7deb7260214344b19e75007369b71bff473a55-init/diff:/var/lib/docker/overlay2/4d17dd9d3fa579c20abb5fc62e8a5793a3a734fed0f7a0ead4e15c547fd9b2cc/diff:/var/lib/docker/overlay2/da021aa8e4967d59b1096cc69e7d7ca43a8b63bd3ca0e487b0e88c54d3e246be/diff",
                "MergedDir": "/var/lib/docker/overlay2/dc9863e37807b9ee8b7c6bb24b7deb7260214344b19e75007369b71bff473a55/merged",
                "UpperDir": "/var/lib/docker/overlay2/dc9863e37807b9ee8b7c6bb24b7deb7260214344b19e75007369b71bff473a55/diff",
                "WorkDir": "/var/lib/docker/overlay2/dc9863e37807b9ee8b7c6bb24b7deb7260214344b19e75007369b71bff473a55/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "d35f26610730",
            "Domainname": "",
            "User": "",
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "bash"
            ],
            "Image": "mqttifconfig:ubuntu",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "b97ce910823381403c2a35689a38b5f2f37026ac35c7f5351467942fb3df8833",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/b97ce9108233",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "9d917c0f1345ccaf3db8d0f57d0a5d5af9242a1f00d9e089e2ccef17778ca412",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.4",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:04",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "bfd0b6316c955ba9083cb60784d2f6bbd5c4cede680d8ad34e739b25752f6a71",
                    "EndpointID": "9d917c0f1345ccaf3db8d0f57d0a5d5af9242a1f00d9e089e2ccef17778ca412",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.4",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:04",
                    "DriverOpts": null
                }
            }
        }
    }
]
