
with open("letters.txt","r") as text_file:
	lines = text_file.readlines()

	letters = {}

	for line in lines:

		for character in line:

			letters[character] = letters.get(character,0) + 1

	for key in letters.keys():
		print(key+", "+ str( letters[key] ) )