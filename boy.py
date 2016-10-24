from FGAme import *

class Boy:

    def __init__(self):
        self.body = world.add.aabb(shape=(50,80), pos=(400, 560), mass=100)
        self.k = 1.05

    def update(self):
        x, y = self.body.vel
        drag = self.k * (y ** 2)
        a = (self.body.mass * self.body.gravity[1] + drag) / self.body.mass
        speed_x, speed_y = self.body.vel
        speed_y += a * 1/60
        pos_x, pos_y = self.body.pos
        pos_y -= speed_y * 1/60
        self.body.vel = (speed_x, speed_y)

        print (self.body.vel[1])

        if(self.body.pos[1] < 35):
            self.body.vel = (0, 0)
