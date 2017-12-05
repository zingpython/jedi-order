#Insertion Sort


unsorted_list = [23,14,5000,2,32,6]

for index in range( len( unsorted_list ) ):

	for reverse in range( index-1, -1, -1 ):

		if unsorted_list[index] > unsorted_list[reverse]:
			value = unsorted_list.pop(index)
			unsorted_list.insert( reverse+1, value )
			break
			
		elif unsorted_list[index] < unsorted_list[reverse] and reverse == 0:
			value = unsorted_list.pop(index)
			unsorted_list.insert( 0, value)


print(unsorted_list)