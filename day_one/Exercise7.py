size = 45

#Find the midpoint
midpoint = (size + 1) // 2


for x in range(size):

	output = ""

	if x+1 > midpoint:
		#After midpoint
		difference = (x+1) - midpoint
		for y in range( midpoint - difference ):
			output = output + "* "
	else:
		#Before the midpoint
		#For 0 to current x add a star to output
		for y in range(x+1):
			output = output + "* "

	print(output)