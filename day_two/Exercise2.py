word1 = "reprint"
word2 = "printer"

#1st method Sorting lists

word_list_1 = list(word1)

word_list_2 = list(word2)

#Sort word_list_1 using the sort list method
word_list_1.sort()

#Sort word_list_2 using the built in sorted function
word_list_2 = sorted(word_list_2)

if word_list_1 == word_list_2:
	print("Anagrams")
else:
	print("not an anagram")

#2nd method dictionary of letters

word_dict_1 = {}

word_dict_2 = {}

#For every letter in the first word
for letter in word1:
	#If that letter is in our dictionary
	if letter in word_dict_1.keys():
		#Increase it's value by 1
		word_dict_1[letter] = word_dict_1[letter] + 1
	#If the letter is not in the dictionary
	else:
		#Add it to the dictionary with the value of 1
		word_dict_1[letter] = 1

#Same as the first loop but for word2 and word_dict_2
for letter in word2:
	if letter in word_dict_2.keys():
		word_dict_2[letter] = word_dict_2[letter] + 1
	else:
		word_dict_2[letter] = 1

print(word_dict_1)
print(word_dict_2)

if word_dict_1 == word_dict_2:
	print("Anagram")
else:
	print("not an anagram")