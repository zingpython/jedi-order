word = input("Enter a word: ")

is_palindrome = True

for x in range( len(word)//2 ):
	
	if word[x] != word[ -(x+1) ]:
		is_palindrome = False
		

if is_palindrome == True:
	print("Palindrome")
else:
	print("Not a Palindome")