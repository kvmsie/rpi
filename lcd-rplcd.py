import RPi.GPIO as GPIO
import time
from RPLCD import CharLCD

GPIO.setwarnings(False)

# For 8-bit pins from D0-D7
lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=18, pin_e=23, pins_data=[4, 17, 27, 22, 28, 29, 30, 31])

# For 4-bit pins from D4-D7
# lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=18, pin_e=23, pins_data=[28, 29, 30, 31])

while True:
    lcd.clear()
    time.sleep(1)

    lcd.cursor_pos = (0, 0)
    lcd.write_string(u'POZDRO')
    lcd.cursor_pos = (1, 11)
    lcd.write_string(u'MORDO')

    time.sleep(1)
