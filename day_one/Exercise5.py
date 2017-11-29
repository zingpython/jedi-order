side_1 = input("Enter the first side: ")
side_2 = input("Enter the second side: ")
side_3 = input("Enter the third side: ")

#Check if equilateral
if side_1 == side_2 and side_2 == side_3:
	print("Equilateral")

elif side_1 == side_2 or side_2 == side_3 or side_1 == side_3:
	print("Isosceles")

else:
	print("Scalene")