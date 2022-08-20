control.onEvent(EventBusSource.MICROBIT_ID_IO_P0, EventBusValue.MICROBIT_PIN_EVT_RISE, function () {
    P0_Down = control.millis()
    led.plotBrightness(0, 0, 255)
})
control.onEvent(EventBusSource.MICROBIT_ID_IO_P0, EventBusValue.MICROBIT_PIN_EVT_FALL, function () {
    P0_Up = control.millis()
    P0_Time = P0_Up - P0_Down
    led.plotBrightness(0, 1, 255)
    if (P0_Time < 2000) {
        led.plotBrightness(0, 2, 255)
        led.plotBrightness(0, 3, 255)
    } else {
        led.plotBrightness(0, 2, 0)
        led.plotBrightness(0, 3, 255)
    }
})
let P0_Time = 0
let P0_Up = 0
let P0_Down = 0
basic.showLeds(`
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
pins.setPull(DigitalPin.P3, PinPullMode.PullUp)
basic.forever(function () {
	
})
