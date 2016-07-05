import sys
from easygui import *
from getNBlinkN2nanpyLCD import taha

msg = "Hi, Please type a positive integer :)"
n = integerbox(msg=msg, default=1, lowerbound=1)
taha(n)

