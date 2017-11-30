
word_search = input("Enter a word: ")

with open("word.txt", "r") as text_file:
	lines = text_file.readlines()

	found = False

	for word in lines:
		if word.strip() == word_search:
			found = True

	if found == True:
		print(word_search)
	else:
		print("NOT FOUND")