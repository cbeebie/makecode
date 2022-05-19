input.onButtonPressed(Button.A, function () {
    mode = 0
})
input.onButtonPressed(Button.B, function () {
    mode = 1
})
let mode = 0
// Default to clapomoter
mode = 1
basic.showIcon(IconNames.Happy)
basic.forever(function () {
    // mode=0 is light meter.
    // mode=1 is clapometer
    if (mode == 0) {
        pins.servoWritePin(AnalogPin.P1, input.lightLevel() / 2)
    } else {
        pins.servoWritePin(AnalogPin.P1, input.soundLevel() / 5)
    }
})
