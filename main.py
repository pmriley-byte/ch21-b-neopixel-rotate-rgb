"""

RGB (GRB format)

"""
strip = neopixel.create(DigitalPin.P13, 8, NeoPixelMode.RGB)
strip.clear()
strip.set_brightness(20)

def on_forever():
    strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.YELLOW))
    strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.GREEN))
    strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.INDIGO))
    strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.VIOLET))
    strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.PURPLE))
    strip.show()
    basic.pause(1000)
    strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
    strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.ORANGE))
    strip.set_pixel_color(2, neopixel.colors(NeoPixelColors.YELLOW))
    strip.set_pixel_color(3, neopixel.colors(NeoPixelColors.GREEN))
    strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.BLUE))
    strip.set_pixel_color(5, neopixel.colors(NeoPixelColors.INDIGO))
    strip.set_pixel_color(6, neopixel.colors(NeoPixelColors.VIOLET))
    strip.set_pixel_color(7, neopixel.colors(NeoPixelColors.PURPLE))
    strip.show()
    basic.pause(1000)
basic.forever(on_forever)
