import sys; sys.path.append('.')
from world import World
from boy import Boy
from umbrella import Umbrella


def draw():
    world.draw()

def update(dt):
    screen.clear()
    world.update(dt)

# Simulacao
WIDTH = World.WIDTH = 400
HEIGHT = World.HEIGHT = 600

world = World(gravity=50)
boyStartX = World.WIDTH/2
boyStartY = World.HEIGHT
umbrella = Umbrella(Actor('umbrella'),positionX=200, positionY=450)
boy = Boy(
    Actor('1'),
    positionX=boyStartX,
    positionY=boyStartY,
    mass=100,
    speed=0,
    gravity=world.gravity,
    umbrella=umbrella
)

def on_mouse_down():
    boy.k = 10
    boy.actor.image = '2'

def on_mouse_up():
    boy.k = 1.05
    boy.actor.image = '1'

world.add(boy)
