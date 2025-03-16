#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "WN-CAAF90";  // Replace with your Wi-Fi SSID
const char* password = "36q89msf5a";  // Replace with your Wi-Fi password
const char* mqtt_server = "192.168.0.22";  // Replace with your MQTT broker IP address

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
  client.setServer(mqtt_server, 1883);
  while (!client.connected()) {
    if (client.connect("ESP32Client")) {
      Serial.println("Connected to MQTT broker");
    } else {
      delay(1000);
      Serial.println("Connecting to MQTT broker...");
    }
  }
  client.publish("home/sensors/temperature", "25");
}

void loop() {
  client.loop();
}
