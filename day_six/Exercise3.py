

unsorted_list = [23,14,5000,2,32,6]

swapped = True

while swapped == True:

	swapped = False

	for index in range( len(unsorted_list)-1 ):

		if unsorted_list[index+1] < unsorted_list[index]:
			unsorted_list[index+1], unsorted_list[index] = unsorted_list[index], unsorted_list[index+1]
			swapped = True

	print(unsorted_list)

print(unsorted_list)