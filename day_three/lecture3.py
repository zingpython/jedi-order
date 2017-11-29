
with open("test.txt", "r") as text_file:
	with open("test2.txt", "w") as text_file_2:
		print(text_file)
		lines = text_file.readlines()
		for line in lines:

			line = line.strip()

			print(line)

			text_file_2.write(line+" THIS IS A TEST\n")

			# print(line, end="")