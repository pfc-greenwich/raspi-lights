import time
import os
import random
from neopixel import Color

RED = Color(128,0,0)
ORANGE = Color(100,16,0)
YELLOW = Color(128,64,0)
GREEN = Color(0,128,0)
AQUA = Color(0,64,16)
BLUE = Color(0,0,128)
PURPLE = Color(64,0,64)
WARM_WHITE = Color(255,197,143)
WHITE = Color(255,255,255)
BLACK = Color(0,0,0)

default_colors = [
  RED,
  ORANGE,
  YELLOW,
  GREEN,
  AQUA,
  BLUE,
  PURPLE
]

Colors = default_colors

random.seed()

def load_solid(np, c):
    for i in range(0, np.numPixels()):
        np.setPixelColor(i, c)

def solid(np, c):
    for i in range(0, np.numPixels()):
        np.setPixelColor(i, c)
    np.show()

def chase(np, c, d):
    for i in range(c * np.numPixels()):
        for j in range(0, np.numPixels()):
            np.setPixelColor(j, BLACK)
        np.setPixelColor(i % np.numPixels(), Color(255,255,255))
        np.show()
        time.sleep(d / 1000.0)
    np.setPixelColor(np.numPixels() - 1, BLACK)
    np.show()

def load_random_colors():
    global Colors
    Colors = []
    num_colors = len(default_colors)
    t = list(default_colors)
    for i in range(0, num_colors):
        j = random.randint(0, len(t) - 1)
#       print "picked %d from %d %s" % (j, len(t), t[j])
        Colors.append(t[j])
        t.remove(t[j])

def colors_up(np, t):
    time.sleep(1)
    for i in range(0,np.numPixels()):
        np.setPixelColor(i, WHITE)
        if (i > 0):
            np.setPixelColor(i - 1, Colors[(i - 1) % 7])
        np.show()
        time.sleep(t / 1000.0)
    np.setPixelColor(i, Colors[i % 7])
    np.show()

def colors_down(np, t):
    time.sleep(1)
    for i in range((np.numPixels() - 1),0,-1):
        np.setPixelColor(i, WHITE)
        if (i < (np.numPixels() - 1)):
            np.setPixelColor(i + 1, BLACK)
        np.show()
        time.sleep(t / 1000.0)
    solid(np, BLACK)
    np.show()

def colors(np):
    for i in range(0,np.numPixels()):
         np.setPixelColor(i, Colors[i % 7])
    np.show()

def random_flash(np, c):
    count = 0
    while(count < c):
         i = random.randint(0, np.numPixels() - 1)
         old = np.getPixelColor(i)
         np.setPixelColor(i,WHITE)
         np.show()
         time.sleep(80.0 / 1000.0)
         np.setPixelColor(i,old)
         np.show()
         time.sleep(random.randint(300, 900) / 1000.0)
         count += 1

def unalternate(np,t):
    for i in range((np.numPixels() - 1),0,-2):
        np.setPixelColor(i, BLACK)
        np.show()
        time.sleep(t / 1000.0)

    for i in range((np.numPixels() - 2),0,-2):
        np.setPixelColor(i, BLACK)
        np.show()
        time.sleep(t / 1000.0)
    solid(np, BLACK)

def alternate(np,a,b,t):
    solid(np, BLACK)
    for i in range(0,np.numPixels(),2):
        np.setPixelColor(i, a)
        np.show()
        time.sleep(t / 1000.0)
   
    for i in range(1,np.numPixels(),2):
        np.setPixelColor(i, b)
        np.show()
        time.sleep(t / 1000.0)

def blink(np, c, t):
    for i in range(c):
        np.setBrightness(0)
        np.show()
        time.sleep(t / 1000.0)
        np.setBrightness(255)
        np.show()
        time.sleep(t / 1000.0)

def check(np, i):
   if (i < 0):
      return 0
   if (i > (np.numPixels() - 1)):
      return (np.numPixels() - 1)
   return i

def from_middle(np, color, t):
   middle = int(np.numPixels() / 2)
   np.setPixelColor(middle, color)
   np.show()
   time.sleep(t / 1000.0)
   count = 1
   while ((middle + count) <= np.numPixels()):
      np.setPixelColor(check(np,middle + count), color)
      np.setPixelColor(check(np,middle - count), color)
      np.show()
      time.sleep(t / 1000.0)
      count += 1

def fade_out(np, t, cb=255, rs=255):
   d = (t * 1000.0) / cb
   for b in range(cb, 0, -1):
      np.setBrightness(b)
      np.show()
      time.sleep(d / 1000.0)
   np.setBrightness(rs)
   solid(np, BLACK)

def fade_in(np, t, cb=255):
   d = (t * 1000.0) / cb
   for b in range(0, cb):
      np.setBrightness(b)
      np.show()
      time.sleep(d / 1000.0)

def wheel(pos):
   """Generate rainbow colors across 0-255 positions."""
   if pos < 85:
      return Color(pos * 3, 255 - pos * 3, 0)
   elif pos < 170:
      pos -= 85
      return Color(255 - pos * 3, 0, pos * 3)
   else:
      pos -= 170
      return Color(0, pos * 3, 255 - pos * 3)

def rainbow_cycle(strip, wait_ms=20, iterations=5):
   """Draw rainbow that uniformly distributes itself across all pixels."""
   for j in range(256*iterations):
      for i in range(strip.numPixels()):
         strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
      strip.show()
      time.sleep(wait_ms/1000.0)

def load_rainbow_cycle(strip):
   for i in range(strip.numPixels()):
      strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels())) & 255))


