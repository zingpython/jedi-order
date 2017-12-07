import sqlite3
import csv

def createTables():
	connection = sqlite3.connect("employees.db")

	cursor = connection.cursor()

	cursor.execute(''' CREATE TABLE users(
		id INTEGER PRIMARY KEY,
		name VARCHAR(256),
		email VARCHAR(256),
		country VARCHAR(256) ) ''')

	cursor.execute('''CREATE TABLE phone_numbers(
		id INTEGER PRIMARY KEY,
		phone_num VARCHAR(20),
		user_id INTEGER,
		FOREIGN KEY(user_id) REFERENCES users(id) ) ''')

	connection.commit()

	connection.close()

createTables()

connection = sqlite3.connect("employees.db")

cursor = connection.cursor()

with open("employees.csv") as employee_file:
	employee_data = csv.reader(employee_file)

	for row in employee_data:
		# print(row)

		cursor.execute("INSERT INTO users(name,email,country) VALUES (?,?,?)", (row[0], row[4], row[5]) )

		connection.commit()

		user_id = cursor.lastrowid

		cursor.execute("INSERT INTO phone_numbers(phone_num,user_id) VALUES (?,?)", (row[1], user_id) )

		cursor.execute("INSERT INTO phone_numbers(phone_num,user_id) VALUES (?,?)", (row[2], user_id) )

		cursor.execute("INSERT INTO phone_numbers(phone_num,user_id) VALUES (?,?)", (row[3], user_id) )

		connection.commit()

cursor.execute("SELECT * FROM users INNER JOIN phone_numbers ON users.id=phone_numbers.user_id")

user = cursor.fetchall()

for line in user:
	print(line)


connection.close()