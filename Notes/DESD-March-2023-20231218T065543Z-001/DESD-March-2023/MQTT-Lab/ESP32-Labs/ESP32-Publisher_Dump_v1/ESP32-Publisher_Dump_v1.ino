/*
 * 
 * This is sample code written for PG-DIoT students of ACTS Batch to work with MQTT protocol
 * 
 */
#include <WiFi.h>
#include <PubSubClient.h>    
#include <esp_wifi.h>
#include<DHT.h>
#include<ArduinoJson.h>
#define DHTPIN 4


DynamicJsonDocument doc(1024);

DHT dht(DHTPIN, DHT22);
//set custom MAC Address just in case your esp32 is not registered with the current network
//uint8_t newMACAddress[]={0xc8,0xb2,0x9b,0x70,0x7b,0xf/a};

const char* ssid =   "acts";                          //ssid - service set Identifier (Replace it with your ssid name)
const char* password =  "";                     // replace with ssid paasword
const char* mqttBroker = "192.168.44.125";                  // broker address - replace it with your broker address/cloud broker - test.mosquitto.org
//const char* mqttBrokerv1 = "192.168.43.189";  
const int   mqttPort = 1883;                            // broker port number
const char* clientID = "tech123";                   // client-id
const char* clientIDv1 = "techemotes1";   
const char* mqtt_topic1 = "cdac/room/temperature"; // topic names
const char* mqtt_topic2 = "cdac/room/humidity";
WiFiClient MQTTclient;
//WiFiClient MQTTclientv1/;
PubSubClient client(MQTTclient);
//PubSubClient clientv1(MQTT/clientv1);
long lastReconnectAttempt = 0;
boolean reconnect()
{
  if (client.connect(clientID)) {
    //client.subscribe(channelName); // Subscribe to channel.
    //Serial.println("Subscribed");
  }
  return client.connected();
}
//boolean reco/nnect_v1()
//{
//  if (clientv1.connect(clientIDv1)) {
//    //client.subscribe(channelName); // Subscribe to channel.
//    Serial.println("Subscribed");
//  }
//  return clientv1.connected();
//}
void setup() {
  Serial.begin(9600);
  dht.begin();
  Serial.println("Attempting to connect...");
  WiFi.mode(WIFI_STA);
//  esp_wifi_set_mac(WIFI_IF_STA,/&newMACAddress[0]);
  WiFi.begin(ssid, password); // Connect to WiFi.
  if (WiFi.waitForConnectResult() != WL_CONNECTED)
  {
    Serial.println("Couldn't connect to WiFi.");
  }
  client.setServer(mqttBroker, mqttPort); // Connect to broker
  //Serial.println("Connected to Broker");
  lastReconnectAttempt = 0;
}
void loop() {
  
  if (!client.connected())
  {
    long now = millis();    //returns the number of milliseconds passed since the esp32 began running the current program
    if (now - lastReconnectAttempt > 5000) { // Try to reconnect.
      lastReconnectAttempt = now;
      if (reconnect())
      { // Attempt to reconnect.192.168.1.5
        lastReconnectAttempt = 0;
      }
    }
  }

  else 
  { // Connected.
    Serial.println("Connected to broker");
    client.loop();
//    clientv1.loop()/;
    float h = dht.readHumidity();
    float t = dht.readTemperature();
//      float h = random(0,100);
//      float t = random(0,100);
    delay(2000);
    Serial.print("Humidity is ");
    Serial.println(h);
    Serial.print("Temperature is ");  
     Serial.println(t); 
     
     doc["temperature"]=t;
     doc["humidity"]=h;
     char sensor[500];
     serializeJson(doc,sensor);
    client.publish(mqtt_topic1, sensor);  //(topicname, payload)
//    clientv1.publish(channelName2, String(h).c_str()); 
//    /clientv1.publish(mqtt_topic1, String(t).c_str());  //(topicname, payload)
//    client.publish(mqtt_topic2, String/(h).c_str()); 
    Serial.println("Message Published");
    delay(1000);
  }
}
