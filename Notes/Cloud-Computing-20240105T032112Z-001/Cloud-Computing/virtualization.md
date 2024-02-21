Download the vmware work station pro 17:
https://www.vmware.com/in/products/workstation-pro/workstation-pro-evaluation.html

Download
-------------------------------------
Workstation 17 Pro for Linux

License keys:

https://gist.github.com/PurpleVibe32/30a802c3c8ec902e1487024cdea26251

MC60H-DWHD5-H80U9-6V85M-8280D
4A4RR-813DK-M81A9-4U35H-06KND
NZ4RR-FTK5H-H81C1-Q30QH-1V2LA
JU090-6039P-08409-8J0QH-2YR7F
4Y09U-AJK97-089Z0-A3054-83KLA
4C21U-2KK9Q-M8130-4V2QH-CF810

chmod 700 VMware-Workstation-Full-17.0.0-20800274.x86_64.bundle 

sudo ./Mware-Workstation-Full-17.0.0-20800274.x86_64.bundle 

Networking types in VM:

https://blogs.vmware.com/kb/2013/03/networking-options-in-vmware-workstation-and-fusion.html

Download ubuntu Desktop

https://ubuntu.com/download/desktop

Bridge Network:
If you use bridged networking, your vm is a full participant in the network. It has access to other machines on the network and can be contacted by other machines on the network as if it were a physical computer on the network

-- Your VM (Guest OS) is having a different IP than host machine
   in the same network.
   Host:
   enp4s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.77.206  netmask 255.255.255.0  broadcast 192.168.77.255
        inet6 fe80::4cd:70:684a:a09  prefixlen 64  scopeid 0x20<link>
        ether e8:6a:64:e3:5e:14  txqueuelen 1000  (Ethernet)
        RX packets 360319  bytes 532429249 (532.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 52777  bytes 5556569 (5.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
VM:

Clonning:
-------------------
Cloning a virtual machine creates a virtual machine that is a copy of the original. The new virtual machine is configured with the same virtual hardware, installed software, and other properties that were configured for the original virtual machine. 

https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-1E185A80-0B97-4B46-A32B-3EF8F309BEED.html

- the machine that need to cloned must be in power off state.
- Linked clone ->
    master vm must be available to have existance of cloned machine.
- Full clone -> independent from the master.
        - deleting the master will not impact on the working of
         slave(new cloned vm)
         

