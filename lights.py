import time
import random
import px
from neopixel import *
strip = Adafruit_NeoPixel(50, 18, 800000, 5, False, 255, 0, ws.WS2811_STRIP_RGB)
strip.begin()
while(True):
   px.load_solid(strip, px.WARM_WHITE)
   px.fade_in(strip, 3, cb=40)
   ts = random.randint(300,600)
   time.sleep(ts)
   px.fade_out(strip, 3, cb=40)
   px.load_rainbow_cycle(strip)
   px.fade_in(strip, 3)
   px.rainbow_cycle(strip, wait_ms=50, iterations=20)
   px.fade_out(strip, 3)
   px.load_solid(strip, px.WARM_WHITE)
   px.fade_in(strip, 3, cb=40)
   ts = random.randint(240,540)
   time.sleep(ts)
   px.fade_out(strip, 3, cb=40)
   px.load_random_colors()
   px.colors_up(strip, 60)
   px.random_flash(strip, 80)
   px.colors_down(strip, 60)

