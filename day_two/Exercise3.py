original_sentence = input("Enter a sentence: ")
shift = int( input("How much to shift by: ") )

#1st method; dictiony of letters and numbers

letter_to_number = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

number_to_letter = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"o",16:"p",17:"q",18:"r",19:"s",20:"t",21:"u",22:"v",23:"w",24:"x",25:"y",26:"z"}

new_sentence = ""

for letter in original_sentence:
	if letter.isalpha() == True:
		#if the letter is capitalized later we will recapitalize it
		capitalized = letter.isupper()

		#Convert letter to lowercase
		letter = letter.lower()

		#Convert letter to a number
		letter_number = letter_to_number[letter]

		#Shift the number by the shift variable
		letter_number = letter_number + shift

		#If letter-number is out of range return it to the range
		if letter_number < 1:
			letter_number = letter_number + 26
		elif letter_number > 26:
			letter_number = letter_number - 26

		#add to new_sentence and captialize if needed
		if capitalized == True:
			new_sentence = new_sentence + number_to_letter[ letter_number ].upper()
		else:
			new_sentence = new_sentence + number_to_letter[ letter_number ]
	#If non-letter then add to sentence withut any conversions
	else:
		new_sentence = new_sentence + letter

print(new_sentence)


#2nd method: unicode character conversions

new_sentence_2 = ""

for letter in original_sentence:
	if letter.isalpha() == True:
		unicode_number = ord(letter)

		#uppercase
		if unicode_number >= 65 and unicode_number <= 90:

			unicode_number = unicode_number + shift

			if unicode_number < 65:
				unicode_number = unicode_number + 26
			elif unicode_number > 90:
				unicode_number = unicode_number - 26

			new_sentence_2 = new_sentence_2 + chr( unicode_number )


		#lowercase
		elif unicode_number >= 97 and unicode_number <= 122:

			unicode_number = unicode_number + shift

			if unicode_number < 97:
				unicode_number = unicode_number + 26
			elif unicode_number > 122:
				unicode_number = unicode_number - 26

			new_sentence_2 = new_sentence_2 + chr( unicode_number )

	else:
		new_sentence_2 = new_sentence_2 + letter

print(new_sentence_2)