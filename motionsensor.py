import RPi.GPIO as GPIO
import time

motionSensorPin = 18

redPin   = 16
greenPin = 20
bluePin  = 21

file_object = open("motion_log.txt", "a")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionSensorPin, GPIO.IN)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

GPIO.output(bluePin, GPIO.LOW)


try:
    currentTime = time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())

    while True:
        if GPIO.input(18) == 0:
            GPIO.output(greenPin, GPIO.HIGH)
            GPIO.output(redPin,   GPIO.LOW)

            file_object.write(currentTime + " : Motion not detected.\n")

        else:
            GPIO.output(greenPin, GPIO.LOW)
            GPIO.output(redPin,   GPIO.HIGH)

            file_object.write(currentTime + " : Something is moving\n")

        time.sleep(1)

except KeyboardInterrupt:
    GPIO.output(redPin,   GPIO.LOW)
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(bluePin,  GPIO.HIGH)

    file_object.close()

