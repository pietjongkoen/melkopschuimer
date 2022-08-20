def on_microbit_id_io_p0_pin_evt_rise():
    global P0_Down
    P0_Down = control.millis()
    led.plot_brightness(0, 0, 255)
control.on_event(EventBusSource.MICROBIT_ID_IO_P0,
    EventBusValue.MICROBIT_PIN_EVT_RISE,
    on_microbit_id_io_p0_pin_evt_rise)

def on_microbit_id_io_p0_pin_evt_fall():
    global P0_Up, P0_Time
    P0_Up = control.millis()
    P0_Time = P0_Up - P0_Down
    led.plot_brightness(0, 1, 255)
    if P0_Time < 2000:
        led.plot_brightness(0, 2, 255)
        led.plot_brightness(0, 3, 255)
    else:
        led.plot_brightness(0, 2, 0)
        led.plot_brightness(0, 3, 255)
control.on_event(EventBusSource.MICROBIT_ID_IO_P0,
    EventBusValue.MICROBIT_PIN_EVT_FALL,
    on_microbit_id_io_p0_pin_evt_fall)

P0_Time = 0
P0_Up = 0
P0_Down = 0
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
pins.set_pull(DigitalPin.P3, PinPullMode.PULL_UP)

def on_forever():
    pass
basic.forever(on_forever)
