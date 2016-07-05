import sys
from easygui import *
from getNBlinkN2nanpyLCD import taha

msgbox('salam')
msg = "Hi, Please type a positive integer :)"
n = integerbox(msg=msg, default=1, lowerbound=1)
taha(n)
msgbox(msg='Your number is {}. :)'.format(n))



def pooya_print(msg):
    msgbox(msg=msg)
