#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
from time import sleep
import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('pomiary.db')
c = conn.cursor()

CzujnikDeszczuPin = 11 #pin11
CzujnikTempWilgPin = 27 #pin13, ale trzeba podac wprost do DHT
CzujnikWilgGleby = 15 #pin 15, nie wiem czy zadziala

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS pomiary(Czas_pomiaru TEXT, Temperatura_powietrza REAL, Wilgotnosc_powietrza REAL, Wilgotnosc_gleby BOOLEAN, Opady BOOLEAN)')
    conn.commit()
    
def insert(temp_p, wilg_p, wilg_g, opady):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO pomiary(Czas_pomiaru, Temperatura_powietrza, Wilgotnosc_powietrza, Wilgotnosc_gleby, Opady) VALUES(?, ?, ?, ?, ?)", (time, temp_p, wilg_p, wilg_g, opady))
    conn.commit()
    
def select():
    c.execute("SELECT * FROM pomiary")
    data = c.fetchall()
    print(data)

def setup():
    
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(CzujnikDeszczuPin, GPIO.IN)   # Set LedPin's mode is output  GPIO.setmode(GPIO.BOARD)
    GPIO.setup(CzujnikWilgGleby, GPIO.IN)
    
def destroy():
    GPIO.cleanup()
    c.close()
    conn.close()
    
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
        
        wilg = not GPIO.input(CzujnikWilgGleby)
        print("Wilgotnosc gleby: ", wilg)
        
        insert(temperature, humidity, wilg, czyDeszcz)
        
        sleep(5)


if __name__ == '__main__':     # Program start from here
  setup()
  try:
    czytajTemp()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()