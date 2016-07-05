from easygui.boxes.derived_boxes import msgbox
from nanpy import Arduino
from nanpy import Lcd
import time

lcd = Lcd([12, 11, 5, 4, 3, 2], [16, 2])


def phase2():
	av = 0
	cnt = 0
	outputpin = 0
	while True:
		rawvoltage= Arduino.analogRead(outputpin)
		millivolts= float((rawvoltage/1024.0) * 5000.0)
		celsius = (millivolts)/10.0
		tempf = (celsius * 9)/5 + 32
		msgbox('degrees Celsius: {}'.format(celsius))
		msgbox('degrees Fahrenheit: {}'.format(tempf))
		lcd.setCursor(0, 0)
		lcd.printString(celsius)
		lcd.setCursor(0, 1)
		lcd.printString(tempf)
		time.sleep(10)
