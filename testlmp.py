from nanpy import Arduino
from nanpy import Lcd
import time

lcd = Lcd([12, 11, 5, 4, 3, 2], [16, 2])

av = 0
cnt = 0

outputpin = 0
while True:
	rawvoltage= Arduino.analogRead(outputpin)
	#celsius = rawvoltage * 0.48828125
	#print rawvoltage
	millivolts= float((rawvoltage/1024.0) * 5000.0)
	#print millivolts
	#av = av + millivolts;
	#cnt = cnt + 1
	#print '\n'
	celsius = (millivolts)/10.0
	tempf = (celsius * 9)/5 + 32
	print 'degrees Celsius: ', celsius 
	print 'degrees Fahrenheit: ', tempf
	print '\n'
	#print av
	#print cnt
	print '------------------'
	
	
	lcd.setCursor(0, 0)
	lcd.printString(celsius)
	
	lcd.setCursor(0, 1)
	lcd.printString(tempf)
	time.sleep(3)
	
	
