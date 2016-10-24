from FGAme import *
from math import sqrt
from boy import *
from shot import Shot

world.add.margin(10, -10)
world.gravity = (0, -10)
player = Boy()
player.body.gravity = world.gravity
gravity_x, gravity_y = player.body.gravity
gambiarra = True

@listen('long-press', 'up')
def increase_drag():
    player.k = 10

@listen('key-up', 'up')
def decrease_drag():
    player.k = 1.05


@listen('key-down', 'x')
def exit_game():
    exit()

def update():
    global gambiarra
    player.update()
    if gambiarra:
    	shot = Shot()
    	world.add(shot)
    	gambiarra = False

#world.add(player)


run()