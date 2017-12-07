
class View:

	def takeInput(self, prompt):
		return input(prompt)

	def printOutput(self, output):
		print(output)

	def menu(self):
		print("1. Read from file")
		print("2. Create user")
		print("3. View all users")
		print("4. View user by id")
		print("5. View phone numbers of user")
		print("6. Exit program")

		return input("Enter a menu option: ")