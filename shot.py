from FGAme import *

class Shot(Circle):

	def __init__(self):
		super().__init__(mass=100, vel=(70, 300), radius=10)
