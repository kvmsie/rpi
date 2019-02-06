import RPi.GPIO as GPIO
import time

minusButtonPin = 18
plusButtonPin  = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(minusButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(plusButtonPin,  GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0;

while True:
    minus_input_state = GPIO.input(18)
    plus_input_state  = GPIO.input(23)

    if minus_input_state == False:
        count -= 1

    if plus_input_state == False:
        count += 1
        
    print(count)
    time.sleep(0.5)
