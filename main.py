def on_button_pressed_a():
    global click
    click += -1
    if click == 1:
        basic.show_string("a")
        basic.pause(1000)
        basic.clear_screen()
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global a
    if click == 0:
        a += 1
    else:
        pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global click
    click += 1
    if click == 1:
        basic.show_string("a")
        basic.pause(2000)
        basic.clear_screen()
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

a = 0
click = 0
click = 0

def on_forever():
    global a
    if a == 1:
        basic.show_string("Apple")
        basic.pause(1000)
        basic.clear_screen()
        a += -1
    else:
        pass
basic.forever(on_forever)
