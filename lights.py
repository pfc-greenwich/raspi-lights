import time
import random
import px
from neopixel import *
strip = Adafruit_NeoPixel(50, 18, 800000, 5, False, 255, 0, ws.WS2811_STRIP_RGB)
strip.begin()
while(True):
   px.load_solid(strip, px.ORANGE)
   px.fade_in(strip, 5)
   time.sleep(5)
   px.fade_out(strip, 5)
