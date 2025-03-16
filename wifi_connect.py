import network
import time

SSID = "WN-CAAF90"  # Replace with your Wi-Fi SSID
PASSWORD = "36q89msf5a"  # Replace with your Wi-Fi password

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print("Connected, IP address:", wlan.ifconfig()[0])

connect()
