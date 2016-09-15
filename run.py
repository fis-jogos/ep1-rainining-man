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
HEIGHT = World.HEIGHT = 400

world = World(gravity=100)
boyStartX = World.WIDTH/2
boyStartY = World.HEIGHT
umbrella = Umbrella(Actor('umbrella'),positionX=boyStartX, positionY=boyStartY)
boy = Boy(Actor('1'), positionX=boyStartX,positionY=boyStartY, mass=100,
 speed=30, gravity=world.gravity,umbrella=umbrella)

world.add(umbrella)
world.add(boy)