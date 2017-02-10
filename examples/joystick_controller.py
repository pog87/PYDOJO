from pydojo import *

# inizializzo
pygame.init()
width = 800
height = 600
SCREEN(width, height)

bianco = [255, 255, 255]

gamepad_control = False
try:
    # creo un oggetto Joystick
    pad = pygame.joystick.Joystick(0)
    # inizializzo il joystick
    pad.init()
    gamepad_control = True
except:
    print("no GamePad found...")

gufo = Actor('library/gufo.png')
gufo.goto(width/2, height/2)

uno = Arduino('COM5')

rightPwm = uno.get_pin('d:10:p')
leftPwm = uno.get_pin('d:5:p')
RF = uno.get_pin('d:9:o')
RB = uno.get_pin('d:8:o')
LF = uno.get_pin('d:7:o')
LB = uno.get_pin('d:6:o')

RF.write(True)
RB.write(False)
LF.write(True)
LB.write(False)

direction = "forward"

def shutdown():
    RF.write(False)
    RB.write(False)
    LF.write(False)
    LB.write(False)
    rightPwm.write(0)
    leftPwm.write(0)

while True:

    # KEYBOARD CONTROL
    if keydown(ESCAPE):
        shutdown()
        quit()

    if keydown(RIGHT):
        if direction == "forward":
            RF.write(True)
            RB.write(False)
        elif direction == "back":
            RF.write(False)
            RB.write(True)
        rightPwm.write(1)
    if keyup(RIGHT):
        rightPwm.write(0)
        RF.write(False)
        RB.write(False)

    if keydown(LEFT):
        if direction == "forward":
            LF.write(True)
            LB.write(False)
        elif direction == "back":
            LF.write(False)
            LB.write(True)
        leftPwm.write(1)
    if keyup(LEFT):
        leftPwm.write(0)
        LF.write(False)
        LB.write(False)

    if keydown(UP):
        direction = "forward"
    if keydown(DOWN):
        direction = "back"


    # GAMEPAD CONTROL
    if gamepad_control:
        horizontal = pad.get_axis(0)

        if horizontal > 0.2:
            rightPwm.write(0.9)
            gufo.x += int(horizontal * 10)
        if horizontal < -0.2:
            leftPwm.write(0.9)
            gufo.x += int(horizontal * 10)

    fill(bianco)
    gufo.draw()
    sleep(0.01)
    UPDATE()
