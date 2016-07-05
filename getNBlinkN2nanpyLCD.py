from nanpy import Arduino
from nanpy import Lcd
import time

lcd = Lcd([12, 11, 5, 4, 3, 2], [16, 2])
lcd.printString('Hello World!')

def taha(N):
	Arduino.pinMode(13, Arduino.OUTPUT)
	while True:
		Arduino.digitalWrite(13, Arduino.HIGH)
		time.sleep(float(N))
		Arduino.digitalWrite(13, Arduino.LOW)
		time.sleep(float(N))
		lcd.setCursor(0, 1)
		lcd.printString(N)
		print N

