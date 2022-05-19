def on_button_pressed_a():
    global mode
    mode = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global mode
    mode = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

mode = 0
# Default to light meter
mode = 0

def on_forever():
    # mode=0 is light meter.
    # mode=1 is clapometer
    if mode == 0:
        Kitronik_Move_Motor.write_servo_pin(Kitronik_Move_Motor.ServoSelection.SERVO1,
            input.light_level() / 2)
    else:
        Kitronik_Move_Motor.write_servo_pin(Kitronik_Move_Motor.ServoSelection.SERVO1,
            input.sound_level() / 2)
basic.forever(on_forever)
