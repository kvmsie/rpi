import RPi.GPIO as GPIO
import Adafruit_DHT
import time

'''
GPIO.setwarnings(false)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup

instance = dht11.DHT11(pin = 18)
result = instance.read();

if (result.isValid()):
    printf("Temperatura: " +result.temperature)
'''

sensor = Adafruit_DHT.DHT11
gpio = 18

for i in range(0, 100):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

    if humidity is not None and temperature is not None:
        #print('Temperatura: {0:0.3f} stopni, Wilgotnosc: {1:0.3f}%'.format(temperature, humidity))
        print(temperature)
    else:
        print('Przypal')
    
    time.sleep(2)

