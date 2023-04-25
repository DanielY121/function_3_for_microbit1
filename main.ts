input.onButtonPressed(Button.A, function () {
    click += -1
    if (click == 1) {
        basic.showString("a")
        basic.pause(1000)
        basic.clearScreen()
    } else {
    	
    }
})
input.onButtonPressed(Button.AB, function () {
    if (click == 1) {
        a += 1
    } else {
    	
    }
})
input.onButtonPressed(Button.B, function () {
    click += 1
    if (click == 1) {
        basic.showString("a")
        basic.pause(2000)
        basic.clearScreen()
    } else {
    	
    }
})
let click = 0
click = 0
let a = 0
basic.forever(function () {
    if (a == 1) {
        basic.showString("Apple")
        basic.pause(1000)
        basic.clearScreen()
        a += -1
    } else {
    	
    }
})
