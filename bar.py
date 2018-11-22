import time
import random
import px
from neopixel import *
np = Adafruit_NeoPixel(50, 18, 800000, 5, False, 255, 0, ws.WS2811_STRIP_RGB)
np.begin()

marquee = [ px.RED, px.RED, px.GREEN, px.GREEN ]
px.marquee(np, marquee, 250)
