import math

class Circle:
	radius = float()
	area = float()
	circumference = float()

	def __init__(self, radius):
		self.radius = radius
		self.calculateArea()
		self.calculateCircumference()

	def calculateArea(self):
		self.area = math.pi * self.radius ** 2

	def calculateCircumference(self):
		self.circumference = 2 * math.pi * self.radius

my_circle = Circle(8)

print(my_circle.radius)
print(my_circle.area)
print(my_circle.circumference)