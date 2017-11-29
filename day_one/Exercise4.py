user_input = input("Enter a letter: ")

#This function isalpha will return true if all of the characters in the string are letters 
if user_input.isalpha() == True:

	#Set user_input equal to the first letter in user_input
	user_input = user_input[0]

	#If user_input is in the list ["a", "e", "i", "o", "u"] then it is a vowel
	if user_input in ["a", "e", "i", "o", "u"]:
		print("This is a vowel")
	#If user_inpus is a y then it is sometimes a vowel
	elif user_input == "y":
		print("sometimes a vowel, sometimes a consonant")
	#If user_input is not in the list and not a y then it is a consonant
	else:
		print("This is a consonant")

#If isalpha returns false then user_input has a non-letter character in it.
else:
	print("Not a letter, try again")