#Selection Sort

def selectionSort(unsorted_list):
	sorted_list = []

	while len(unsorted_list) > 0:

		# print(unsorted_list)
		# print(sorted_list)
		# print("------------")

		min_index = 0

		for index in range( len(unsorted_list) ):

			if unsorted_list[index] < unsorted_list[min_index]:

				min_index = index

		min_value = unsorted_list.pop( min_index )

		sorted_list.append( min_value )

	# print( sorted_list )

	return sorted_list

my_list = [20, 10, 6, 15, 30, 12, 2, 6]

print( selectionSort(my_list) )