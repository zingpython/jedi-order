
def helloWorld():
	print("hello world")

helloWorld()

def add(number1, number2):
	number_sum = number1 + number2

	return number_sum


try:
	user_input1 = int( input("Enter a number: ") )
except ValueError:
	user_input1 = 5

print( add( user_input1 , 7 ) )


class Car:
	color = str()
	make = str()
	model = str()
	horsepower = int()
	year = str()
	milage = float()

	def __init__(self, color, make, model, year, horsepower):
		self.color = color
		self.make = make
		self.model = model
		self.year = year
		self.horsepower = horsepower
		self.milage = 0.0

	def addMilage(self, miles):
		self.milage = self.milage + miles

	def getColor(self):
		return self.color

	def setColor(self, color):
		self.color = color

	def getModel(self):
		return self.model

	def setModel(self, model):
		new_model = ""
		for letter in model:
			new_model = new_model + letter.upper()
		self.model = new_model


my_car = Car("red","toyota","corolla","2010", 50)

print(my_car.make)

my_car.make = "Toyota"

print(my_car.make)

my_car.addMilage(20)

print(my_car.milage)

my_car.setColor("Yellow")

print( my_car.getColor() )

print( my_car.color )

ken_car = Car("silver","Honda","Acord","2017",45)