input.onButtonPressed(Button.A, function () {
    click += -1
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    // you can change it into different kind of words base on variables of alphabet's value
    // also you can remove -1 from the program
    if (click == 1) {
        a = 1
    } else if (click == 2) {
        b = 1
    } else if (click == 3) {
        c = 1
    } else if (click == 4) {
        d = 1
    } else if (click == 5) {
        e = 1
    } else if (click == 6) {
        f = 1
    } else if (click == 7) {
        g = 1
    } else if (click == 8) {
        h = 1
    } else if (click == 9) {
        i = 1
    } else if (click == 10) {
        j = 1
    } else if (click == 11) {
        k = 1
    } else if (click == 12) {
        l = 1
    } else if (click == 13) {
        m = 1
    } else if (click == 14) {
        n = 1
    } else if (click == 15) {
        o = 1
    } else if (click == 16) {
        p = 1
    } else if (click == 17) {
        q = 1
    } else if (click == 18) {
        r = 1
    } else if (click == 19) {
        s = 1
    } else if (click == 20) {
        t = 1
    } else if (click == 21) {
        u = 1
    } else if (click == 22) {
        v = 1
    } else if (click == 23) {
        w = 1
    } else if (click == 24) {
        x = 1
    } else if (click == 25) {
        y = 1
    } else if (click == 26) {
        z = 1
    } else if (click == 27) {
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
    } else if (click == -1) {
        click = 1
    }
})
input.onButtonPressed(Button.B, function () {
    click += 1
})
let z = 0
let y = 0
let x = 0
let w = 0
let v = 0
let u = 0
let t = 0
let s = 0
let r = 0
let q = 0
let p = 0
let o = 0
let n = 0
let m = 0
let l = 0
let k = 0
let j = 0
let i = 0
let h = 0
let g = 0
let f = 0
let e = 0
let d = 0
let c = 0
let b = 0
let a = 0
let click = 0
click = 0
basic.forever(function () {
    if (a == 1) {
        basic.showString("Alpha")
        basic.pause(1000)
        basic.clearScreen()
        a += -1
    } else if (b == 1) {
        basic.showString("Bravo")
        basic.pause(1000)
        basic.clearScreen()
        b += -1
    } else if (c == 1) {
        basic.showString("Charlie")
        basic.pause(1000)
        basic.clearScreen()
        c += -1
    } else if (d == 1) {
        basic.showString("Delta")
        basic.pause(1000)
        basic.clearScreen()
        d += -1
    } else if (e == 1) {
        basic.showString("Echo")
        basic.pause(1000)
        basic.clearScreen()
        e += -1
    } else if (f == 1) {
        basic.showString("Foxtrot")
        basic.pause(1000)
        basic.clearScreen()
        f += -1
    } else if (g == 1) {
        basic.showString("Golf")
        basic.pause(1000)
        basic.clearScreen()
        g += -1
    } else if (h == 1) {
        basic.showString("Hotel")
        basic.pause(1000)
        basic.clearScreen()
        h += -1
    } else if (i == 1) {
        basic.showString("India")
        basic.pause(1000)
        basic.clearScreen()
        i += -1
    } else if (j == 1) {
        basic.showString("Juliett")
        basic.pause(1000)
        basic.clearScreen()
        j += -1
    } else if (k == 1) {
        basic.showString("Kilo")
        basic.pause(1000)
        basic.clearScreen()
        k += -1
    } else if (l == 1) {
        basic.showString("Lima")
        basic.pause(1000)
        basic.clearScreen()
        l += -1
    } else if (m == 1) {
        basic.showString("Mike")
        basic.pause(1000)
        basic.clearScreen()
        m += -1
    } else if (n == 1) {
        basic.showString("November")
        basic.pause(1000)
        basic.clearScreen()
        n += -1
    } else if (o == 1) {
        basic.showString("Oscar")
        basic.pause(1000)
        basic.clearScreen()
        o += -1
    } else if (p == 1) {
        basic.showString("Papa")
        basic.pause(1000)
        basic.clearScreen()
        p += -1
    } else if (q == 1) {
        basic.showString("Quebec")
        basic.pause(1000)
        basic.clearScreen()
        q += -1
    } else if (r == 1) {
        basic.showString("Romeo")
        basic.pause(1000)
        basic.clearScreen()
        r += -1
    } else if (s == 1) {
        basic.showString("Sierra")
        basic.pause(1000)
        basic.clearScreen()
        s += -1
    } else if (t == 1) {
        basic.showString("Tango")
        basic.pause(1000)
        basic.clearScreen()
        t += -1
    } else if (u == 1) {
        basic.showString("Uniform")
        basic.pause(1000)
        basic.clearScreen()
        u += -1
    } else if (v == 22) {
        basic.showString("Victor")
        basic.pause(1000)
        basic.clearScreen()
        v += -1
    } else if (w == 23) {
        basic.showString("Whiskey")
        basic.pause(1000)
        basic.clearScreen()
        w += -1
    } else if (x == 24) {
        basic.showString("Xray")
        basic.pause(1000)
        basic.clearScreen()
        x += -1
    } else if (y == 25) {
        basic.showString("Yankee")
        basic.pause(1000)
        basic.clearScreen()
        y += -1
    } else if (z == 26) {
        basic.showString("Zulu")
        basic.pause(1000)
        basic.clearScreen()
        z += -1
    }
    if (click == 1) {
        basic.showString("A")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 2) {
        basic.showString("B")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 3) {
        basic.showString("C")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 4) {
        basic.showString("D")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 5) {
        basic.showString("E")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 6) {
        basic.showString("F")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 7) {
        basic.showString("G")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 8) {
        basic.showString("H")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 9) {
        basic.showString("I")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 10) {
        basic.showString("J")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 11) {
        basic.showString("K")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 12) {
        basic.showString("L")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 13) {
        basic.showString("M")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 14) {
        basic.showString("N")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 15) {
        basic.showString("O")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 16) {
        basic.showString("P")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 17) {
        basic.showString("Q")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 18) {
        basic.showString("R")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 19) {
        basic.showString("S")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 20) {
        basic.showString("T")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 21) {
        basic.showString("U")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 22) {
        basic.showString("V")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 23) {
        basic.showString("W")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 24) {
        basic.showString("X")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 25) {
        basic.showString("Y")
        basic.pause(1000)
        basic.clearScreen()
    } else if (click == 26) {
        basic.showString("Z")
        basic.pause(1000)
        basic.clearScreen()
    }
})
