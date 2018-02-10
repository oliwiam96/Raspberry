#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
from time import sleep

CzujnikDeszczuPin = 11 #pin11
CzujnikTempWilgPin = 27 #pin13, ale trzeba podac wprost do DHT

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(CzujnikDeszczuPin, GPIO.IN)   # Set LedPin's mode is output  GPIO.setmode(GPIO.BOARD)
def destroy():
  GPIO.cleanup()
def czytajTemp():
    while True:
        print("Obieg petli")
        humidity, temperature = Adafruit_DHT.read_retry(11, CzujnikTempWilgPin)
        if humidity is not None and temperature is not None:
           #print(temperature, humidity)
           print "Temperatura: %.1f C" % temperature
           print "Wilgotnosc %.1f %%" % humidity
        else:
           print("Failed to get reading. Try again!")
           
        czyDeszcz = not GPIO.input(CzujnikDeszczuPin)
        print("Pada deszcz: ", czyDeszcz)
        
        sleep(1)


if __name__ == '__main__':     # Program start from here
  setup()
  try:
    czytajTemp()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()