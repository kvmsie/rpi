import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if (adcnum > 7) or (adcnum <0):
        return -1

    GPIO.output(cspin, True)

    GPIO.output(clockpin, False)
    GPIO.output(cspin, False)

    commandout =  adcnum
    #print("commandout: %d" %commandout)

    commandout |= 0x18
    #print("commandout: %d" %commandout)

    commandout <<= 3
    #print("commandout: %d" %commandout)


    for i in range(5):
        #print("for commandout: %d" %commandout)

        if (commandout & 0x80):
            GPIO.output(mosipin, True)
            #print("tak %d" %i)

        else:
            GPIO.output(mosipin, False)
            #print("nie %d" %i)


        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0

    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1

        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)

    adcout >>= 1
    return adcout


clkPin  = 11
misoPin = 9
mosiPin = 10
csPin   = 8

GPIO.setup(clkPin,  GPIO.OUT)
GPIO.setup(misoPin, GPIO.IN)
GPIO.setup(mosiPin, GPIO.OUT)
GPIO.setup(csPin,   GPIO.OUT)

last_read = 0
tolerance = 5


while True:
    trim_pot_changed = False

    trim_pot = readadc(0, clkPin, mosiPin, misoPin, csPin)
    pot_adjust = abs(trim_pot - last_read)

    if (pot_adjust > tolerance):
        trim_pot_changed = True
        last_read = trim_pot

    if (trim_pot_changed):
        #print("trim_pot_changed", trim_pot_changed)
        print("trim_pot:", int(round(trim_pot / 10.05)), "%")
        #print("pot_adjust:", pot_adjust)
        #print("last_read", last_read)

    time.sleep(0.5)
