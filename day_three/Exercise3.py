file_name = input("Enter a file name: ")
encoding_type = input("Enter the encoding the text file: ")
count = int( input("Enter how many words you want: ") )

with open(file_name, "r", encoding=encoding_type) as text_file:
	lines = text_file.readlines()

	word_list = []

	for line in lines:
		new_line = ""

		for letter in line:
			if letter.isalpha() == True or letter == " ":
				new_line = new_line + letter.lower()

		new_line = new_line.split(" ")

		for word in new_line:
			word_list.append( word )

	print(word_list)