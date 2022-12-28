#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import random


# LED strip configuration:
LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 21      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



                
def limpiarLeds(strip):
    for i in range(150):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()
    
def prender(strip, led, color):
     strip.setPixelColor(led, color)
    
def apagar(strip, led):
    strip.setPixelColor(led, Color(0, 0, 0))
    
    
rojo = Color(255, 0, 0)
verde = Color(0, 255, 0)
class Serpiente:
    def __init__(self, largo, pos, vel, c1=rojo, c2=verde):
        self.largo = largo
        self.pos = pos
        self.vel = vel
        
        self.c1 = c1
        self.c2 = c2
    
    def dibuja(self, tira):
        for i in range(0, self.largo):
            if i % 2 == 0:
                prender(tira, self.pos-4+i, self.c1)
            else:
                prender(tira, self.pos-4+i, self.c2)
    
    def mueve(self):
        self.pos = self.pos + self.vel
        
    

      

# Main program logic follows:
if __name__ == '__main__':
    
    largo = int(input("Largo: "))
    pos = int(input("Posicion: "))
    vel = int(input("Velocidad: "))
    
    
    # Process arguments
    tira = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    tira.begin()
    
    #rojo = Color(255, 0, 0)
    #verde = Color(0, 255, 0)
    tira.show()
    
    #color1 = verde
    #color2 = rojo
    
    rapidez = 0.08
    
    serpientes = []  
    sep1 = Serpiente(largo, pos, vel)
    serpientes.append(sep1)
    
    
    
    
    for i in range(300):
        limpiarLeds(tira)
        
        
        for sep in serpientes:
            sep.dibuja(tira)
            sep.mueve()
        
        
        if i == 20:
            sep2 =  Serpiente(3, 0, 1, c1=Color(94, 57, 153))
            serpientes.append(sep2)
            
        if i == 100:
            sep3 = Serpiente(10, 0, 1, c2=Color(98, 39, 105))
            serpientes.append(sep3)
            
        if i == 135:
            sep4 = Serpiente(8, 0, 3)
            serpientes.append(sep4)
            
        
        
        tira.show()
        time.sleep(rapidez)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #largo = 5
    #pos = 4
    #rapidez = 0.08
    
    
    #for j in range(0, 150):
     #   
      #  for i in range(0, largo):
       #     if i % 2 == 0:
        #        prender(tira, pos-4+i, color1)
         #   else:
         #       prender(tira, pos-4+i, color2)
        #tira.show()
        #time.sleep(rapidez)
         #       
        #pos = pos + 1
        #limpiarLeds(tira)
    
    
    #for i in range(0, largo):
     #   if i % 2 == 0: 
           # prender(tira, i, color1)
     #   else:
      #      prender(tira, i, color2)
       # tira.show()
       # time.sleep(rapidez)
       # 
        #if color1 == rojo:
         #   color1 = verde
        #else:
         #   color1 = rojo
            
       # if color2 == rojo:
        #    color2 = verde
        #else:
         #   color2 = rojo
    
    time.sleep(rapidez)
    
    
    #for i in range(largo, 100):
      #  apagar(tira, i-largo)
      #  tira.show()
      #  time.sleep(0.05)
       # if i % 2 == 0:
       #     prender(tira, i, color1)
       # else:
       #     prender(tira, i, color2)
       # tira.show()
       # time.sleep(rapidez)
        
       # preColor1 = color1
       # color1 = color2
       # color2 = preColor1
    
    #x = 0
    #for i in range(0, 15):
    #    strip.setPixelColor(x+i, Color(0, 0, 0))
    #time.sleep(0.5)
    #
    #x = 1
    #for i in range(0, 5):
    #    strip.setPixelColor(x+i, Color(255, 0, 0))
    #time.sleep(0.5)
        
    #x = 2
    #for i in range(0, 5):
    #    strip.setPixelColor(x+i, Color(255, 0, 0))
    #time.sleep(0.5) 
    
    #strip.show()
        
        
    
    
    
    
    
    