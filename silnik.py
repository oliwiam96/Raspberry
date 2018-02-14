#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
from time import sleep


Pompka = 16

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(Pompka, GPIO.OUT)   # Set LedPin's mode is output  GPIO.setmode(GPIO.BOARD)
    GPIO.output(Pompka, GPIO.LOW)  # led off
    

def destroy():
    GPIO.cleanup()
    
def pracaPompki(sygnal):
    if sygnal == True:
        GPIO.output(Pompka, GPIO.HIGH)  # led on
    else:
        GPIO.output(Pompka, GPIO.LOW)  # led off
        
        
if __name__ == '__main__':     # Program start from here
  setup()
  try:
    while(1):
        pracaPompki(True)
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
        
        
        
        


