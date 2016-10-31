# Writes an image column by column using WS2801/SPI-like addressable RGB LED lights.
# Author: Markus Rudel
# License: Public Domain
from __future__ import division
import time

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import Image, time, os, sys

class LightWriter:
    # Configure the count of pixels:
    PIXEL_COUNT = 50

    # The WS2801 library makes use of the BCM pin numbering scheme. See the README.md for details.

    # Specify a software SPI connection for Raspberry Pi on the following pins:
    #PIXEL_CLOCK = 26
    #PIXEL_DOUT  = 13
    #pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)

    # Alternatively specify a hardware SPI connection on /dev/spidev0.0:
    SPI_PORT   = 0
    SPI_DEVICE = 0
    pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

    # Configurable values
    filename = "hello.png"

    def displayFile(self, filename, pixels, wait = 0):
        spidev = file("/dev/spidev0.0", "w")
        # load image in RGB format and get dimensions:
        print "Loading file " + filename
        img       = Image.open(filename).convert("RGB")
        width     = img.size[0]
        height    = img.size[1]
        print "%dx%d pixels" % img.size
        # To do: add resize here if image is not desired height

        print "Assigning color information..."
        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                pixels.set_pixel(y, Adafruit_WS2801.RGB_to_color(r, g, b))
                pixels.show()
            if wait > 0:
                time.sleep(wait)

    def main(self):
        try:
            # Clear all the pixels to turn them off.
            pixels.clear()
            pixels.show()  # Make sure to call show() after changing any pixels!
            self.displayFile(filename, pixels, 1)
    
        except KeyboardInterrupt:
            pixels.clear()
            pixels.show()
            sys.exit(0)
    
if  __name__ =='__main__':
    LEDs=LightWriter()
    LEDs.main()