class Umbrella:
    def __init__(self, actor, positionX, positionY, mass=100):
        self.actor = actor
        self.mass = mass
        self.positionX = positionX
        self.positionY = positionY
        self.isOpen = False

    def draw(self):
        self.actor.x = self.positionX
        self.actor.y = 600 - self.positionY
        self.actor.draw()

    def update(self, dt):
        pass
