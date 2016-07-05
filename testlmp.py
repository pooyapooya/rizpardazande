from nanpy import Arduino
from nanpy import Lcd
import time
from test import pooya_print

lcd = Lcd([12, 11, 5, 4, 3, 2], [16, 2])

av = 0
cnt = 0

outputpin = 0
while True:
	rawvoltage= Arduino.analogRead(outputpin)
	millivolts= float((rawvoltage/1024.0) * 5000.0)
	celsius = (millivolts)/10.0
	tempf = (celsius * 9)/5 + 32
	pooya_print('degrees Celsius: {}'.format(celsius))
	pooya_print('degrees Fahrenheit: {}'.format(tempf))
	lcd.setCursor(0, 0)
	lcd.printString(celsius)
	lcd.setCursor(0, 1)
	lcd.printString(tempf)
	time.sleep(10)

