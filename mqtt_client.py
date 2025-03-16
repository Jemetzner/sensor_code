import network
import time
from umqtt.simple import MQTTClient

# Wi-Fi credentials
SSID = "WN-CAAF90"
PASSWORD = "36q89msf5a"

# MQTT broker settings (Raspberry Pi running Mosquitto)
MQTT_BROKER = "192.168.0.22"  # Replace with your Pi's IP address
MQTT_TOPIC = "esp32/data"

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    print("Connecting to Wi-Fi...")
    time.sleep(1)

print("Connected to Wi-Fi:", wifi.ifconfig())

# Connect to MQTT broker
client = MQTTClient("esp32_client", MQTT_BROKER, port = 1883)
client.connect()
print("Connected to MQTT broker")

# Publish messages in a loop
try:
    while True:
        message = "Hello from ESP32!"
        client.publish(MQTT_TOPIC, message)
        print("Published:", message)
        time.sleep(2)
except KeyboardInterrupt:
    print("script stopped by user")

