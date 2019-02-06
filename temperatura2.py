import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    print('Muj super czujnik pokazuje temperaturq: %s' %temperature)
    time.sleep(1)
