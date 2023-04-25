def on_button_pressed_a():
    global click
    click += -1
    if click == 1:
        basic.show_string("a")
        basic.pause(2000)
        basic.clear_screen()
    elif click == 2:
        basic.show_string("b")
        basic.pause(2000)
        basic.clear_screen()
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global a
    if click == 1:
        a += 1
    elif click == 2:
        pass
    elif click == 3:
        pass
    elif click == 4:
        pass
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
z = 0
y = 0
x = 0
w = 0
v = 0
u = 0
t = 0
s = 0
r = 0
q = 0
p = 0
o = 0
l = 0
k = 0
j = 0
i = 0
h = 0
g = 0
f = 0
e = 0
d = 0
c = 0
b = 0
m = 0
n = 0
click = 0

def on_forever():
    global a
    if a == 1:
        basic.show_string("Apple")
        basic.pause(1000)
        basic.clear_screen()
        a += -1
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    elif False:
        pass
    else:
        pass
basic.forever(on_forever)
