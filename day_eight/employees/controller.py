from model import Model
from view import View
import csv

my_model = Model()
my_view = View()

# my_view.printOutput("THIs is a test")

running = True

while running == True:

	choice = my_view.menu()

	if choice == "1":
		file_name = my_view.takeInput("Enter a file name: ")

		with open(file_name) as data_file:
			lines = csv.reader(data_file)
			for row in lines:
				my_model.insertUser(row[0], row[4], row[5])

				user_id = my_model.getLastRowID()

				my_model.insertPhoneNumber(row[1], user_id)
				my_model.insertPhoneNumber(row[2], user_id)
				my_model.insertPhoneNumber(row[3], user_id)


	elif choice == "2":
		pass
	elif choice == "3":
		pass
	elif choice == "4":
		pass
	elif choice == "5":
		pass
	elif choice == "6":
		running = False
	else:
		my_view.printOutput("\nInvalid choice. Try again.\n")