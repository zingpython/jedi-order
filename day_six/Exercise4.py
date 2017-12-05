

unsorted_list = [23,14,5000,2,32,6]

for index in range( len(unsorted_list) ):
	unsorted_list[index] = [ unsorted_list[index] ]

print(unsorted_list)


while len( unsorted_list ) > 1:
	print(unsorted_list)
	sorted_list = []
	
	for index in range( 0, len(unsorted_list), 2 ):

		temp_list = []

		if index == len(unsorted_list)-1:
			sorted_list.append( unsorted_list[index] )

		else:

			while len( unsorted_list[index] ) >0 or len( unsorted_list[index+1] ) >0:

				if unsorted_list[index] == []:
					temp_list.append( unsorted_list[index+1].pop(0) )

				elif unsorted_list[index+1] == []:
					temp_list.append( unsorted_list[index].pop(0) )

				elif unsorted_list[index][0] <= unsorted_list[index+1][0]:
					temp_list.append( unsorted_list[index].pop(0) )

				else:
					temp_list.append( unsorted_list[index+1].pop(0) )

			# print(temp_list)

			sorted_list.append(temp_list)

	# print(sorted_list)

	unsorted_list = sorted_list

print( unsorted_list[0] )