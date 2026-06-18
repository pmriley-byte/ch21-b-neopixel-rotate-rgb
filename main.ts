led.enable(false)
let strip = neopixel.create(DigitalPin.P13, 8, NeoPixelMode.RGB)
strip.clear()
strip.setBrightness(64)
basic.forever(function () {
    strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
    strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Green))
    strip.setPixelColor(2, neopixel.colors(NeoPixelColors.Blue))
    while (true) {
        strip.rotate(1)
        strip.show()
        basic.pause(500)
    }
    strip.clear()
})
