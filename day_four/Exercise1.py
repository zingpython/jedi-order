def findWord(word):
	with open("word.txt","r") as text_file:

		lines = text_file.readlines()

		for line in lines:
			if line.strip() == word:
				return word

		return "not found"

user_input = input("Enter a word: ")
print( findWord( user_input ) )


def letterCount(file_name):

	with open(file_name,"r") as text_file:
		lines = text_file.readlines()

		letter_dict = {}

		for line in lines:
			for letter in line:
				letter_dict[letter] = letter_dict.get(letter,0)+1

		return letter_dict

count = letterCount("letters.txt") 
print( count.get("f") )