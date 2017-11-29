sentence = input("Enter a sentence: ")

new_sentence = ""

capitalize_next = TEST_RUNNER = ''

for index in range( len(sentence) ):

	#Capitalize i's
	if sentence[index] == "i" and sentence[index-1].isalpha() == False and sentence[index+1].isalpha() == False:
		new_sentence = new_sentence + "I"
		capitalize_next = False

	#Check for the end of a sentence
	elif sentence[index] in [".","!","?"]:
		capitalize_next = True
		new_sentence = new_sentence + sentence[index]

	#Capitalize the first letter of a sentence
	elif capitalize_next == True and sentence[index].isalpha() == True:
		new_sentence = new_sentence + sentence[index].upper()
		capitalize_next = False

	else:
		new_sentence = new_sentence + sentence[index]

print(new_sentence)