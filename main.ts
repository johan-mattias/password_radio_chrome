input.onButtonPressed(Button.A, function () {
    radio.sendString("15")
    basic.showIcon(IconNames.Chessboard)
    basic.clearScreen()
})
radio.onReceivedString(function (receivedString) {
    count += 1
    if (receivedString == password) {
        radio.sendString("pass")
        basic.showIcon(IconNames.Square)
    } else if (receivedString == "pass") {
        basic.showIcon(IconNames.Target)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(count)
})
let count = 0
let password = ""
password = "zedf"
count = 0
radio.setGroup(1)
