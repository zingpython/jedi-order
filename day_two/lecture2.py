numbers = [7,3,9,"12",7,3]

print(numbers)

numbers[0] = numbers[0] + 1

numbers.append(22)

x = numbers.pop(2)

numbers.insert(0, 10)

print(x)

print(numbers)

#For loop for the values
for number in numbers:
	number = number * 2

print(numbers)

#For loop for the indexes
for number in range( len(numbers) ):
	print(numbers[number])
	numbers[number] = numbers[number] * 2

print(numbers)

#Tuples
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

#Cannot modify tuples after their creation
# days[0] = "Moonsday"

#Dictionary
salary = {"matthew":2, "ken":20, "paul":300}

print( salary["matthew"] )

salary["matthew"] = 10

print(salary)

#Add new key:value pair to dictionary
salary["frank"] = 200

print(salary)

#Delete key:value pair from dictionary
del salary["ken"]

print(salary)

print(salary.keys())

print(salary.values())

for key in salary.keys():
	print(key)
	print(salary[key])

#While loops

y = 0

while y < 20:
	print(y)
	y = y + 1

	break