def convertToBinary(number):
	binary_string = ""

	while number > 0:
		binary_string = str(number%2) + binary_string

		number = number // 2

	return binary_string

print( convertToBinary(220) )

def convertFromBinary(binary_string):

	binary_string = binary_string[::-1]

	total = 0

	increment = 1

	for digit in binary_string:
		if digit == "1":
			total = total + increment

		increment = increment * 2

	return total

print( convertFromBinary("10110") )