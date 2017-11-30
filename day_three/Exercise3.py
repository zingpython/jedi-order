file_name = input("Enter a file name: ")
encoding_type = input("Enter the encoding the text file: ")
count = int( input("Enter how many words you want: ") )

#Open the file using the user input
with open(file_name, "r", encoding=encoding_type) as text_file:
	#Read each line into a list of strings
	lines = text_file.readlines()

	#Create a blank list to hold each word
	word_list = []

	#For each line in line
	for line in lines:
		#Begin building a new string with an empty string to start
		new_line = ""

		#For every letter in a line
		for letter in line:
			#If the letter is an alphabetic character or a space
			if letter.isalpha() == True or letter == " ":
				#Add that character to the new string the lower function converts the letter to lowercase)
				new_line = new_line + letter.lower()

		#COnvert the new string into a list of strings split on the spaces
		new_line = new_line.split(" ")

		#For every word in out list of strings add it to the blank list word_list
		for word in new_line:
			word_list.append( word )

	# print(word_list)

	#Create an empty dictionary that will have a key of a word and the value of how many times that word appears
	word_dict = {}

	#For each word in our word list
	for word in word_list:
		#If the word is not a blank string
		if word != "":
			#Add that word to the dictionary or if the word is already in the dictionary increase its value by 1
			word_dict[word] = word_dict.get(word,0)+1

	# print(word_dict)

	#Create an empty list that will hold a list of the highst keys and values in our dictionary
	word_result = []

	#Run the code to add to the word_result list a number of times equal to count (The user input)
	for x in range(count):

		#At the start of each for loop create an empty string and a value at 0
		#These will eventually hold the highest value and its key
		highest_key = ""
		highest_value = 0

		#For each word in our dictionary
		for word in word_dict.keys():

			#If the value of the word is greater than our highest_value
			if word_dict[word] > highest_value:
				#Set the highest value equalt to our current value
				highest_value = word_dict[word]
				#Set the highest key equalt to our current key/word
				highest_key = word

		#Add the higest_value and highest_key to the word_result list
		word_result.append( [ highest_key, highest_value ] )

		#Delete the highest key and value from the dictionary
		#This stops us from getting a list with the same item on it repeatedly
		del word_dict[highest_key]

	#Output the contents of word_result
	for word in word_result:
		print( word[0]+", "+ str( word[1] ) )