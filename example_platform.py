from pydojo import *

# create game display
screen(1280, 720)

background('example_asset/backgrounds/forest2.png')

framerate(30)

# PYCO INIT
pyco = Actor('example_asset/characters/pyco1.png', 'idle')
pyco.loadfolder('example_asset/characters/pyco_walk/')
# print pyco.costumes
pyco.goto(100, 600)
pyco.speed = 5
# pyco.rotate = False
pyco.rotation = 'flip'
pyco.bullets = []
pyco.jumping = False

# BAT INIT
bat = Actor('example_asset/characters/bat1.png')
bat.load('example_asset/characters/bat2.png')
bat.rotation = 'flip'
bat.point(random.randint(0, 360))
bat.bounce = True
bat.tag = 'enemy'

# PY BULLET INIT
py = Actor('example_asset/characters/python.png')
py.scale(50, 50)
py.hide()

# PLATFORMS INIT
platforms = []
for i in range(6):
    a = Actor('example_asset/characters/platform.png', str(i))
    a.tag = 'support'
    a.scale(200, 50)
    platforms.append(a)
for p in platforms:
    p.gorand()
# print(platforms)

# TERRAIN INIT
terrain = Actor('example_asset/characters/terrain.png')
terrain.goto(CENTER.x, 700)
terrain.scale(1280, 50)
terrain.tag = 'support'

gravity = 10

for a in getactors():
    print a.costume

print(ACTORS)

while True:

    # MOVEMENT
    if key(RIGHT):
        pyco.point(90)
        pyco.forward(pyco.speed)
        pyco.nextcostume(pause=7, costumes=[1, 4])
    if keyup(RIGHT):
        pyco.setcostume('idle')
    if key(LEFT):
        pyco.point(-90)
        pyco.forward(pyco.speed)
        pyco.nextcostume(pause=7, costumes=[1, 4])
    if keyup(LEFT):
        pyco.setcostume('idle')

    # JUMP
    if keydown(UP):
        if pyco.collide('support'):
            pyco.jumping = True
            t = 0
    if pyco.jumping:
        if t < 15:
            pyco.y -= (2 * gravity)
            t = t + 1

    # SHOOT
    if keydown(SPACE):
        bullet = clone(py)
        bullet.tag = 'bullet'
        bullet.point(pyco.direction)
        bullet.goto(pyco)
        bullet.show()
        pyco.bullets.append(bullet)

    if pyco.collide(bat):
        print('preso')
        pyco.hide(2)
    if keydown(P):
        pyco.show()
    if keydown(O):
        pyco.hide()

    for b in pyco.bullets:
        b.forward(10)
        if distance(pyco, b) > 2000:
            pyco.bullets.remove(b)
        b.roll(5)

    if key(DOWN):
        pyco.point(180)
        pyco.forward(pyco.speed)

    if not pyco.collide('support'):
        # print('falling')
        pyco.y += gravity

    if pyco.y > 720:
        pyco.y = 500

    # BAT
    bat.nextcostume()
    bat.forward(10)
    if bat.collide('bullet'):
        print('colpito')
        bat.hide(2)

    update()
