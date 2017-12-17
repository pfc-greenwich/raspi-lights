import time
import random
import px
from neopixel import *
strip = Adafruit_NeoPixel(50, 18, 800000, 5, False, 255, 0, ws.WS2811_STRIP_RGB)
strip.begin()
while(True):
   px.load_solid(strip, px.WARM_WHITE)
   px.fade_in(strip, 3, cb=40)
   ts = random.randint(60,240)
   time.sleep(ts)
   px.fade_out(strip, 3, cb=40)
   px.alternate(strip, px.BLUE, px.WARM_WHITE, 100)
   px.random_flash(strip, 20)
   px.unalternate(strip, 100)
   time.sleep(2)
   px.from_middle(strip, px.RED, 80)
   px.from_middle(strip, px.WARM_WHITE, 80)
   px.from_middle(strip, px.GREEN, 80)
   px.fade_out(strip, 3)
   px.load_rainbow_cycle(strip)
   px.fade_in(strip, 3)
   px.rainbow_cycle(strip, wait_ms=20, iterations=10)
   px.fade_out(strip, 3)
   px.load_solid(strip, px.WARM_WHITE)
   px.fade_in(strip, 3, cb=40)
   ts = random.randint(60,240)
   time.sleep(ts)
   px.fade_out(strip, 3, cb=40)
   px.load_random_colors()
   px.colors_up(strip, 60)
   px.random_flash(strip, 80)
   px.colors_down(strip, 60)
   time.sleep(2)
   marquee = [ px.RED, px.RED, px.GREEN, px.GREEN ]
   for i in range(40):
      px.marquee(strip, marquee, 250)
   px.fade_out(strip, 3)

