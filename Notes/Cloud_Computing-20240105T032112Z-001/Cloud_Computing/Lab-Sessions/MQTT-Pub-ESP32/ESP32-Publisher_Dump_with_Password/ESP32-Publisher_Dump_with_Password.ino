/*
 * 
 * ESP32 Sending (Sample Data to Mosquitto Broker)
 * 
 */
#include <WiFi.h>
#include "wifi_cred.h"
#include <PubSubClient.h> 
#include <ArduinoJson.h>    //Arduino JSON Library 
#include <esp_wifi.h>
const char* ssid =   "acts";                          //ssid - service set Identifier (Replace it with your ssid name)
const char* password =  "";                     // replace with ssid paasword
//const char* mqttServer = "192.168.1.8";                  // broker address - replace it with your broker address/cloud broker - test.mosquitto.org
//const int   mqttPort = 1883;                            // broker port number
//const char* clientID = "techemotes";                   // client-id
//const char* channelName1 = "cdac/diot/temperature"; // topic names
//const char* channelName2 =  "teche/patient/humidity";   
char* humidity;
char* temperature;

// Set the custom MAC address in case your ESP32 is not regsitered with the acts network

uint8_t newMACAddress[] = {0xdc, 0x1b, 0xa1, 0x61, 0xed, 0x51};

WiFiClient MQTTclient;
PubSubClient client(MQTTclient);
long lastReconnectAttempt = 0;

DynamicJsonDocument sensor_data(1024);  

boolean reconnect()
{
  if (client.connect(clientID,userName,passWord)) {
    //client.subscribe(channelName); // Subscribe to channel.
    Serial.println("Trying to connect ... !! ");
  }
  return client.connected();
}

void setup() {
  Serial.begin(9600);
  Serial.println("Attempting to connect...");
  WiFi.mode(WIFI_STA);
  esp_wifi_set_mac(WIFI_IF_STA, &newMACAddress[0]);
  WiFi.begin(ssid, password); // Connect to WiFi.
  if (WiFi.waitForConnectResult() != WL_CONNECTED)
  {
    Serial.println("Couldn't connect to WiFi.");
  }
  client.setServer(mqttServer, mqttPort); // Connect to broker
  Serial.println("Connected to MQTT Broker");
  lastReconnectAttempt = 0;
}
void loop() {
   sensor_data["Location"] = "Pune";   
   sensor_data["Temperature"] = 27;
   sensor_data["Humidity"] = 80;
   sensor_data["Pressure"] = 960;
   String json;
   serializeJson(sensor_data, json);
  if (!client.connected())
  {
    long now = millis();
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
    client.loop();
   // client.publish(channelName1, String(t).c_str());  //(topicname, payload)
    client.publish(channelName1, String(json).c_str());  //(topicname, payload)
    //client.publish(channelName1, String(h).c_str()); 
    Serial.println("Message Published");
    Serial.println(json);
    delay(10000);    
  }
}
