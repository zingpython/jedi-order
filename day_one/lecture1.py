name = input("Enter your name: ")

name = "Hello " + name

# print(name)

x = 23

y = 3
x = x + 1

x = x - y

x = x * 2

x = x // 2

# print(x)

name = name + " you are " + str(x) + " years old"

print(name)

print(x)

if x==23:
	print("X is 23")
	x = 50

elif x == 22:
	print("X is 22")

else:
	print("X is not 22 or 23")

x = 2

for number in range(11):
	for number2 in range(11):
		print(number*number2)