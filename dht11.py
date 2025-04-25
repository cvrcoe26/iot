import RPi.GPIO as GPIO
import dht11
import time

# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# Read data using pin 21
instance = dht11.DHT11(pin=21)

def read_sensor_with_retry():
    retries = 5
    for i in range(retries):
        result = instance.read()
        if result.is_valid():
            return result
        time.sleep(1)  # Wait for 1s before trying again
    return None  # If all retries fail

while True:
    result = read_sensor_with_retry()
    if result:
        print("Temperature: %.1f C" % result.temperature)
        print("Humidity: %.1f%%" % result.humidity)
    else:
        print("Failed to get valid data from sensor after retries.")
    time.sleep(1)
