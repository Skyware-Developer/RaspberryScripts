import time
import board
# Used to define which GPIO pin is connected to the sensor
import adafruit_dht
# DHT library
import psutil
# Library to retrieve info about running processes
import digitalio
# Library used to control I/O pins and set directions

#Check for running libg process, if there's any we kill it
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

# Declaration of the DHT11 on GPIO pin 23
sensor = adafruit_dht.DHT11(board.D23)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        if temp > 25:
            led.value = True
        else:
            led.value = False
        print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)