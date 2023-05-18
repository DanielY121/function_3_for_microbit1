def on_button_pressed_a():
    global click
    click += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, click
    # you can change it into different kind of words base on variables of alphabet's value
    # also you can remove -1 from the program
    if click == 1:
        a = 1
    elif click == 2:
        b = 1
    elif click == 3:
        c = 1
    elif click == 4:
        d = 1
    elif click == 5:
        e = 1
    elif click == 6:
        f = 1
    elif click == 7:
        g = 1
    elif click == 8:
        h = 1
    elif click == 9:
        i = 1
    elif click == 10:
        j = 1
    elif click == 11:
        k = 1
    elif click == 12:
        l = 1
    elif click == 13:
        m = 1
    elif click == 14:
        n = 1
    elif click == 15:
        o = 1
    elif click == 16:
        p = 1
    elif click == 17:
        q = 1
    elif click == 18:
        r = 1
    elif click == 19:
        s = 1
    elif click == 20:
        t = 1
    elif click == 21:
        u = 1
    elif click == 22:
        v = 1
    elif click == 23:
        w = 1
    elif click == 24:
        x = 1
    elif click == 25:
        y = 1
    elif click == 26:
        z = 1
    elif click == 27:
        a = 0
        click = 1
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        g = 0
        h = 0
        i = 0
        j = 0
        k = 0
        l = 0
        m = 0
        n = 0
        o = 0
        p = 0
        q = 0
        r = 0
        s = 0
        t = 0
        u = 0
        v = 0
        w = 0
        x = 0
        y = 0
        z = 0
    elif click == -1:
        click = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global click
    click += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

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
n = 0
m = 0
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
a = 0
click = 0
click = 0

def on_forever():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
    if a == 1:
        basic.show_string("Alpha")
        basic.pause(1000)
        basic.clear_screen()
        a += -1
    elif b == 1:
        basic.show_string("Bravo")
        basic.pause(1000)
        basic.clear_screen()
        b += -1
    elif c == 1:
        basic.show_string("Charlie")
        basic.pause(1000)
        basic.clear_screen()
        c += -1
    elif d == 1:
        basic.show_string("Delta")
        basic.pause(1000)
        basic.clear_screen()
        d += -1
    elif e == 1:
        basic.show_string("Echo")
        basic.pause(1000)
        basic.clear_screen()
        e += -1
    elif f == 1:
        basic.show_string("Foxtrot")
        basic.pause(1000)
        basic.clear_screen()
        f += -1
    elif g == 1:
        basic.show_string("Golf")
        basic.pause(1000)
        basic.clear_screen()
        g += -1
    elif h == 1:
        basic.show_string("Hotel")
        basic.pause(1000)
        basic.clear_screen()
        h += -1
    elif i == 1:
        basic.show_string("India")
        basic.pause(1000)
        basic.clear_screen()
        i += -1
    elif j == 1:
        basic.show_string("Juliett")
        basic.pause(1000)
        basic.clear_screen()
        j += -1
    elif k == 1:
        basic.show_string("Kilo")
        basic.pause(1000)
        basic.clear_screen()
        k += -1
    elif l == 1:
        basic.show_string("Lima")
        basic.pause(1000)
        basic.clear_screen()
        l += -1
    elif m == 1:
        basic.show_string("Mike")
        basic.pause(1000)
        basic.clear_screen()
        m += -1
    elif n == 1:
        basic.show_string("November")
        basic.pause(1000)
        basic.clear_screen()
        n += -1
    elif o == 1:
        basic.show_string("Oscar")
        basic.pause(1000)
        basic.clear_screen()
        o += -1
    elif p == 1:
        basic.show_string("Papa")
        basic.pause(1000)
        basic.clear_screen()
        p += -1
    elif q == 1:
        basic.show_string("Quebec")
        basic.pause(1000)
        basic.clear_screen()
        q += -1
    elif r == 1:
        basic.show_string("Romeo")
        basic.pause(1000)
        basic.clear_screen()
        r += -1
    elif s == 1:
        basic.show_string("Sierra")
        basic.pause(1000)
        basic.clear_screen()
        s += -1
    elif t == 1:
        basic.show_string("Tango")
        basic.pause(1000)
        basic.clear_screen()
        t += -1
    elif u == 1:
        basic.show_string("Uniform")
        basic.pause(1000)
        basic.clear_screen()
        u += -1
    elif v == 22:
        basic.show_string("Victor")
        basic.pause(1000)
        basic.clear_screen()
        v += -1
    elif w == 23:
        basic.show_string("Whiskey")
        basic.pause(1000)
        basic.clear_screen()
        w += -1
    elif x == 24:
        basic.show_string("Xray")
        basic.pause(1000)
        basic.clear_screen()
        x += -1
    elif y == 25:
        basic.show_string("Yankee")
        basic.pause(1000)
        basic.clear_screen()
        y += -1
    elif z == 26:
        basic.show_string("Zulu")
        basic.pause(1000)
        basic.clear_screen()
        z += -1
    if click == 1:
        basic.show_string("A")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 2:
        basic.show_string("B")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 3:
        basic.show_string("C")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 4:
        basic.show_string("D")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 5:
        basic.show_string("E")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 6:
        basic.show_string("F")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 7:
        basic.show_string("G")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 8:
        basic.show_string("H")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 9:
        basic.show_string("I")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 10:
        basic.show_string("J")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 11:
        basic.show_string("K")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 12:
        basic.show_string("L")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 13:
        basic.show_string("M")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 14:
        basic.show_string("N")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 15:
        basic.show_string("O")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 16:
        basic.show_string("P")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 17:
        basic.show_string("Q")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 18:
        basic.show_string("R")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 19:
        basic.show_string("S")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 20:
        basic.show_string("T")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 21:
        basic.show_string("U")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 22:
        basic.show_string("V")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 23:
        basic.show_string("W")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 24:
        basic.show_string("X")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 25:
        basic.show_string("Y")
        basic.pause(1000)
        basic.clear_screen()
    elif click == 26:
        basic.show_string("Z")
        basic.pause(1000)
        basic.clear_screen()
basic.forever(on_forever)
