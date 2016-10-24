from FGAme import *
from math import sqrt
from boy import *

world.add.margin(10, -10)
world.gravity = (0, -10)
player = Boy()
player.body.gravity = world.gravity
gravity_x, gravity_y = player.body.gravity

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
    player.update()

#world.add(player)


run()