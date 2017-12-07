import sqlite3

class Model:

	def __init__(self):
		self.connection = sqlite3.connect("employees.db")

		self.cursor = self.connection.cursor()


	def createTables(self):

		self.cursor.execute('''CREATE TABLE users(
							id INTEGER PRIMARY KEY,
							name VARCHAR(256),
							email VARCHAR(256),
							country VARCHAR(256))''')

		self.cursor.execute('''CREATE TABLE phone_numbers(
							id INTEGER PRIMARY KEY,
							phone_num VARCHAR(20),
							user_id INTEGER,
							FOREIGN KEY(user_id) REFERENCES users(id) ) ''')

		self.connection.commit()

	def closeConnection(self):
		self.connection.close()

	def insertUser(self, name, email, country):
		self.cursor.execute("INSERT INTO users(name,email,country) VALUES (?,?,?)",(name,email,country))

		self.connection.commit()

	def insertPhoneNumber(self, phone, user_id):
		self.cursor.execute("INSERT INTO phone_numbers(phone_num,user_id) VALUES (?,?)",(phone, user_id))

		self.connection.commit()

	def getLastRowID(self):
		return self.cursor.lastrowid

	def geAllUsers(self):
		self.cursor.execute("SELECT * FROM users")

		return self.cursor.fetchall()

	def getUserByID(self, user_id):
		self.cursor.execute("SELECT * FROM users WHERE id=?", (user_id,) )

		return self.cursor.fetchone()

	def getPhoneNumbers(self, user_id):
		self.cursor.execute("SELECT * FROM phone_numbers WHERE user_id=?", (user_id,) )

		return self.cursor.fetchall()

#Only runs this if statementif model.py is run directly from console/terminal
if __name__ == "__main__":
	my_model = Model()
	my_model.createTables()
	my_model.closeConnection()