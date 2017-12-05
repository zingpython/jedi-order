import sqlite3


def createTables():
	connection = sqlite3.connect("lecture.db")

	cursor = connection.cursor()

	cursor.execute('''CREATE TABLE students(
					id INTEGER PRIMARY KEY,
					name VARCHAR(256),
					gpa REAL) ''')

	connection.commit()

	connection.close()

# createTables()

connection = sqlite3.connect("lecture.db")

cursor = connection.cursor()

name = "Matthew"

cursor.execute("INSERT INTO students(name,gpa) VALUES (?,?)", (name, 3.2) )

connection.commit()

cursor.execute("SELECT * FROM students")

rows = cursor.fetchall()

print(rows)

connection.close()