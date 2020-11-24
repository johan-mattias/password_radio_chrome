def on_button_pressed_a():
    radio.send_string("15")
    basic.show_icon(IconNames.CHESSBOARD)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    global count
    count += 1
    if receivedString == password:
        radio.send_string("pass")
        basic.show_icon(IconNames.SQUARE)
    elif receivedString == "pass":
        basic.show_icon(IconNames.TARGET)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    basic.show_number(count)
input.on_button_pressed(Button.B, on_button_pressed_b)

count = 0
password = ""
password = "abcd"
count = 0
radio.set_group(1)