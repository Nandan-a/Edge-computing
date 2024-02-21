Practice Assignment
-------------------------
Question : 01
1. create a file hello.py with code print('Helloworld') 
2. create a github repo with name hello_data
3. push this code to master/main branch (depending on your default) branch
4. create a new branch on local repo feature/hellonew
5. add a new line in hello.py -> print("Cloud is nothing but it is someone else computer')
6. merge this code to master/main branch
7. Push the updated changes to main/master branch
--------------------------------------------------------------------------------
Question : 02
1. Create a dockerfile with ubuntu:20.04 as base image and ifconfig utility installed
2. while spinning the container with newly created image named as ubuntu:diotv0
   map the host directory say /home/diot to container directory /container/mydata
3. create a new directory c1 under /container/mydata
4. create a new nodejs file say Helloworld.js with content console.log("Helloworld"
5. observe and verify the file created under c1 directory is visible in the host directory

Question : 03
-----------------
1. use the container created in question 02 to create a new image say ubuntu:ifconfig
2. push this image to Docker hub repo

Qustion : 04
--------------------
1. Create a multi container service using docker-compose file
2. service1 named as pub (developed using paho-mqtt) publish the random number with a sample interval of 5 seconds 40 times before the publisher disconnect.
3. Create a service2 as mq broker (Make sure to create MQTT broker via Dockerfile) and map this to host port 4500
4. ensure broker is starting first and publisher is starting second.
5. use the mosquitto_sub utility from the host to verify that published message is received.

Question : 05
-------------------------
1. Create an IAM user diotdev in your AWS root account
2. Create a IAM group devdiot in your AWS root account
3. Give EC2 full access to devdiot group
4. Add another user diotdev-new in the devdiot group
5. Login with both the users to verify that user have only EC2 service access.

Question 06:
1. use python request module to solve the below problem
2. Create a device on Thingsboard as diot_x (x could be anything)
3. Use the Access token mechanism to post the data to thingsboard device
4. create the dashboard on the thingsboard for temp and humi data
5. create a container (python as a run time environment) to send below telemetry
   {
      "temp" : 27,
      "humi" : 87,
      "location" : "Pune/India"
      "Sensor_deatils" : "DHT22"
      "firmware_version" : "2.01"
   }

6. thingsboard - host (demo.thingsboard.io)








