
for x in range(1,101):

	prime = True

	for y in range(x-1,1,-1):

		if x%y == 0:
			prime=False

	if prime == True:
		print("PRIME")
	else:
		print(x)