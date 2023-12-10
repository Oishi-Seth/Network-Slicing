# Network-Slicing


### Introduction:
The technique to create multiple virtual networks shared over a physical infrastructure is called Network Slicing. Each of these slices are logically isolated and customizable based on the user specific needs or the application. This gives rise to an efficient use of network resources.
One way of network slicing is dividing the network based on the user required service. There are 3 main usage scenarios in 5G. They are:
1. eMBB (enhanced Mobile Broadband) - It aims to improve cellular connectivity with faster data speeds and higher throughput.
2. mMTC (massive Machine Type Communications) - It supports connectivity of a very large number of devices by sending small amounts of data.
3. URLLC (Ultra-Reliable Low Latency Communications) - It supports real-time interactive applications such as virtual/augmented reality.


### Tools used:
The tools required for this project are:
1. Python - For creating user interface
2. Mininet - For emulating virtual network slicing
3. OpenDaylight Controller - For implementing control logic


### Topology Setup:
Separate vitual networks (VNs) were created for each slice type. Created VN called "eMBB", "URLLC" and "mMTC" with 3 separate switches and 2 hosts linked to each switches. These switches are dedicated to their respective services. Based on the functionality of these 3 services, bandwidth and delays were set.


### Working:
1. Run the program with the following command:
```
sudo python3 network_slicing.py
```
2. This will first give the prompt to select the service required by the user. After the user selects the service, based on his selection, bandwidth requirement, maximum tolarable latency and number of devices required to be added is asked.
3. After the user enters the above information, mininet CLI starts. It lists all the controller, switches and hosts added in the topology.
4. ```
   pingall
   ```
   This command in mininet CLI shows that the hosts in different virtual networks fail to communicate with each other whereas the hosts in the same virtual network are able to ping each other.


### Results:
#### Basic Topology:
![Alt text](https://github.com/Oishi-Seth/Network-Slicing/blob/main/images/1.jpeg) </br>
This shows the basic topology of the 3 virtual networks i.e., eMBB, mMTC, URLLC each having 2 hosts connected. 

![Alt text](https://github.com/Oishi-Seth/Network-Slicing/blob/main/images/2.jpeg) </br>
This shows that hosts in the same virtual network are able to ping each other but those in separate VNs are unable to ping.

#### Adding hosts in eMBB VN:
![Alt txt](https://github.com/Oishi-Seth/Network-Slicing/blob/main/images/3.jpeg) </br>
This shows that the user added 3 hosts having a bandwidth of 150Mbps and latency of 15ms.
We can see h7, h8 and h9 are the new hosts added by user over the existing topology. All these hosts are added to s1 which is the OVSswitch for eMBB.

![Alt text](https://github.com/Oishi-Seth/Network-Slicing/blob/main/images/4.jpeg) </br>
h1,h2,h7,h8, and h9 are in eMBB VN and connected to each other.
h3,h4 are in URLLC VN and are connected to each other.
h5, h6 are in mMTC VN and are connected to each other.
None of these hosts across different VN are interconnected.

#### Adding hosts in URLLC VN:
![Alt txt](https://github.com/Oishi-Seth/Network-Slicing/blob/main/images/5.jpeg) </br>
This shows that the user added 7 hosts having a bandwidth of 20Mbps and latency of 0.8ms.
We can the new hosts added by user are added to s2 which is the OVSswitch for URLLC.

![Alt text](https://github.com/Oishi-Seth/Network-Slicing/blob/main/images/6.jpeg) </br>
h1,h2 are in eMBB VN and connected to each other.
h3,h4 and h7 to h13 are in URLLC VN and are connected to each other.
h5, h6 are in mMTC VN and are connected to each other.
None of these hosts across different VN are interconnected.


#### Adding hosts in mMTC VN:
![Alt txt](https://github.com/Oishi-Seth/Network-Slicing/blob/main/images/7.jpeg) </br>
This shows that the user added 14 hosts having a bandwidth of 1Mbps and latency of 10ms.
We can the new hosts added by user are added to s3 which is the OVSswitch for mMTC.

![Alt text](https://github.com/Oishi-Seth/Network-Slicing/blob/main/images/8.jpeg) </br>
h1,h2 are in eMBB VN and connected to each other.
h3,h4 are in URLLC VN and are connected to each other.
h5 to h20 are in mMTC VN and are connected to each other.
None of these hosts across different VN are interconnected.


### References:
1. https://networksimulationtools.com/network-slicing-simulation/
2. https://github.com/jercymat/qualcomm-proj/tree/master
