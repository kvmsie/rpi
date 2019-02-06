import time, sys
import RPi.GPIO as GPIO

redPin   = 17
greenPin = 27
bluePin  = 22

turnOnPin  = 18
turnOffPin = 23
switchPin  = 24

selection = 17


GPIO.setmode(GPIO.BCM)
GPIO.setup(turnOnPin,  GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(turnOffPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(switchPin,  GPIO.IN, pull_up_down=GPIO.PUD_UP)

def turnOn(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

def turnOff(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

def changeSelection():
    global selection

    if selection == 17:
        selection = 27

    elif selection == 27:
        selection = 22

    else:
        selection = 17

while True:
    turnOnButtonPressed  = GPIO.input(turnOnPin)
    turnOffButtonPressed = GPIO.input(turnOffPin)
    switchColorPressed   = GPIO.input(switchPin)

    if turnOnButtonPressed == False:
        turnOn(selection)

    elif turnOffButtonPressed == False:
        turnOff(selection)

    elif switchColorPressed == False:
        changeSelection()


    time.sleep(1)
