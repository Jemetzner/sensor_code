from machine import Pin, I2C
import time

# I2C setup
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=100000)  # Set SCL to GPIO22 and SDA to GPIO21

# Qwiic Flex Glove I2C address (the default address is 0x2F)
ADS1015_ADDR = 0x48
CONFIG_REG = 0x01
CONVERSION_REG = 0x00

# Function to configure ADS1015
def configure_ads1015():
    config = bytearray([
        0xC3, 0x83  # Set single-shot mode, AIN0, ±4.096V range, 1600 SPS
    ])
    i2c.writeto_mem(ADS1015_ADDR, CONFIG_REG, config)

# Function to read analog value from A0
def read_ads1015():
    data = i2c.readfrom_mem(ADS1015_ADDR, CONVERSION_REG, 2)  # Read 2 bytes
    raw_value = (data[0] << 8) | data[1]  # Convert to 16-bit integer

    # ADS1015 is a 12-bit ADC, so shift right by 4 bits
    raw_value = raw_value >> 4

    # Convert to signed integer (ADS1015 returns signed values)
    if raw_value > 2047:  # 12-bit max is 2047, values above this are negative
        raw_value -= 4096

    return raw_value

# Configure ADS1015
configure_ads1015()
try:
# Read and print values in a loop
    while True:
        value = read_ads1015()
        print(f"Flex Sensor Value: {value}")
        time.sleep(0.5)  # Adjust delay as needed
except KeyboardInterrupt:
    print("interrupted")
