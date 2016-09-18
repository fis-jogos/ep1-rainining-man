import sys; sys.path.append('.')
from math import sqrt
from world import World
from umbrella import Umbrella

class Boy:
    """
    This class represents the main party of the body in study
    """
    def __init__(self, actor, positionX, positionY,mass, speed, umbrella, gravity=100):
        self.actor = actor
        self.positionX = positionX
        self.positionY = positionY
        self.mass = mass
        self.speed = speed
        self.acceleration = 0
        self.umbrella = umbrella
        self.gravity = gravity
        self.areaBoy = self.actor.width * self.actor.height
        self.areaUmbrella = self.umbrella.actor.width * self.umbrella.actor.height
        self.total_area =  self.areaBoy + self.areaUmbrella
        self.total_mass = self.mass + self.umbrella.mass
        self.k = 1.05

    def update(self, dt):
        drag = self.k * (self.speed ** 2)
        self.acceleration = -(drag - self.mass * self.gravity) / self.total_mass
        self.speed += self.acceleration * dt

        if self.positionY > 20:
            self.positionY -= self.speed * dt
            self.umbrella.positionY = self.positionY + 20
        else:
            self.speed = 0
            self.acceleration = 0
            self.gravity = 0

    def draw(self):
        self.actor.x = self.positionX
        self.actor.y = World.HEIGHT - self.positionY
        self.actor.draw()
