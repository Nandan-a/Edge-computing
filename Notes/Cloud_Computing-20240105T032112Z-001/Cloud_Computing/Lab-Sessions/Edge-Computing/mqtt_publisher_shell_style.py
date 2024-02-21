import os
import threading
import random
import time
while True:

    def temperature_publisher():
        temp = random.randint(0,50)
        os.system(f"mosquitto_pub -t cdac/diot/temperature -u diot -P diot123 -h localhost -p 1883 -m {temp}")
        time.sleep(10)
    def humidity_publisher():
        humidity = random.randint(50,80)
        os.system(f"mosquitto_pub -t cdac/diot/humidity -u diot -P diot123 -h localhost -p 1883 -m {humidity}")
        time.sleep(10)

    t1 = threading.Thread(target=temperature_publisher)
    t2 = threading.Thread(target=humidity_publisher)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

