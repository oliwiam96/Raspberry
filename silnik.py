#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
from time import sleep


Pompka = 16

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(Pompka, GPIO.OUT)   # Set LedPin's mode is output  GPIO.setmode(GPIO.BOARD)
    

def destroy():
    GPIO.cleanup()
    
def pracaPompki(sygnal):
    while(1):
        if sygnal == True:
            GPIO.output(Pompka, GPIO.HIGH)  # led on
            ##sleep(5)
            ##GPIO.output(Pompka, GPIO.LOW)  # led off
        else:
            sleep(5)
        
if __name__ == '__main__':     # Program start from here
  setup()
  try:
    pracaPompki(True)
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
        
        
        
        


