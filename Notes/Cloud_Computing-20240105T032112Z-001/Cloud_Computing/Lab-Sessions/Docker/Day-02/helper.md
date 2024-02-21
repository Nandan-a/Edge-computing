BHIoT$ ls
Dockerfile

HIoT$ docker build -t ubuntu:diothello .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM ubuntu:22.04
 ---> 2dc39ba059dc
Step 2/4 : RUN apt update -y
 ---> Running in 50e4719ff07b

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
Get:3 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [720 kB]
Get:4 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [114 kB]
Get:5 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [786 kB]
Get:6 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [659 kB]
Get:7 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [99.8 kB]
Get:8 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [4732 B]
Get:9 http://archive.ubuntu.com/ubuntu jammy/main amd64 Packages [1792 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [266 kB]
Get:11 http://archive.ubuntu.com/ubuntu jammy/restricted amd64 Packages [164 kB]
Get:12 http://archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [17.5 MB]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [1035 kB]
Get:14 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [708 kB]
Get:15 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [990 kB]
Get:16 http://archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [8978 B]
Get:17 http://archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [7286 B]
Get:18 http://archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [3520 B]
Fetched 25.2 MB in 5s (4911 kB/s)
Reading package lists...
Building dependency tree...
Reading state information...
14 packages can be upgraded. Run 'apt list --upgradable' to see them.
Removing intermediate container 50e4719ff07b
 ---> ed0c3e35d60a
Step 3/4 : RUN apt install net-tools
 ---> Running in da1d3ed936e3

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

Reading package lists...
Building dependency tree...
Reading state information...
The following NEW packages will be installed:
  net-tools
0 upgraded, 1 newly installed, 0 to remove and 14 not upgraded.
Need to get 204 kB of archives.
After this operation, 819 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/main amd64 net-tools amd64 1.60+git20181103.0eebece-1ubuntu5 [204 kB]
debconf: delaying package configuration, since apt-utils is not installed
Fetched 204 kB in 1s (266 kB/s)
Selecting previously unselected package net-tools.
(Reading database ... 4395 files and directories currently installed.)
Preparing to unpack .../net-tools_1.60+git20181103.0eebece-1ubuntu5_amd64.deb ...
Unpacking net-tools (1.60+git20181103.0eebece-1ubuntu5) ...
Setting up net-tools (1.60+git20181103.0eebece-1ubuntu5) ...
Removing intermediate container da1d3ed936e3
 ---> d067299f112a
Step 4/4 : RUN echo "Hello from DIoT-2022"
 ---> Running in a8bb82978bac
Hello from DIoT-2022
Removing intermediate container a8bb82978bac
 ---> 76159e5c8f11
Successfully built 76159e5c8f11
Successfully tagged ubuntu:diothello

BHIoT$ docker images | head -3
REPOSITORY                TAG              IMAGE ID       CREATED          SIZE
ubuntu                    diothello        76159e5c8f11   45 seconds ago   120MB
apcheserver               v0               1b73cdf5f950   41 hours ago     227MB

BHIoT$ docker run -it --name diothelloc ubuntu:diothello
root@f0126d67ee26:/# 
root@f0126d67ee26:/# 
root@f0126d67ee26:/# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.3  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:ac:11:00:03  txqueuelen 0  (Ethernet)
        RX packets 17  bytes 2182 (2.1 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

BHIoT$ docker run --name myhelloc ubuntu:diothello 
Hello from DIoT-2022

---------------------------------------------------------------------------
App-02
BHIoT$ docker build -t alpine:diothello .
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM alpine
 ---> d7d3d98c851f
Step 2/4 : LABEL developer="bhupendra.jmd@gmail.com"
 ---> Running in 4f5708512bc0
Removing intermediate container 4f5708512bc0
 ---> b558d468a614
Step 3/4 : RUN apk update
 ---> Running in e290a0741d5e
fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/main/x86_64/APKINDEX.tar.gz
fetch https://dl-cdn.alpinelinux.org/alpine/v3.16/community/x86_64/APKINDEX.tar.gz
v3.16.3-115-g69a7883db6 [https://dl-cdn.alpinelinux.org/alpine/v3.16/main]
v3.16.3-111-g13c6c3d6c5 [https://dl-cdn.alpinelinux.org/alpine/v3.16/community]
OK: 17047 distinct packages available
Removing intermediate container e290a0741d5e
 ---> 9b783c5c0443
Step 4/4 : CMD ["echo", "Hello From the alpine developed by diot batch"]
 ---> Running in b086c4b9fcd8
Removing intermediate container b086c4b9fcd8
 ---> ddbe4a5d292c
Successfully built ddbe4a5d292c
Successfully tagged alpine:diothello
---------------------------------------------------------------------------------
BHIoT$ docker images | head -3
REPOSITORY                TAG              IMAGE ID       CREATED          SIZE
alpine                    diothello        ddbe4a5d292c   54 seconds ago   7.99MB
ubuntu                    diothello        ffed8de0da82   52 minutes ago   120MB
BHIoT$ docker run --name alpinec alpine:diothello 
Hello From the alpine developed by diot batch
---------------------------------------------------
BHIoT$ docker run -it alpine:diothello /bin/sh
/ # 
/ # echo $HOME
/root
/ # echo $0
/bin/sh
/ # 
