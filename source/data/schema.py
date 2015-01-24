import sqlite3

tables = []
current_statement = ""

for line in open('data.sql'):
	if line == "\n":
		tables.append(current_statement)
		current_statement = ""
	else:
		current_statement += line

print tables

connection = sqlite3.connect('../../data/data.sqlite')
cursor = connection.cursor()

for table_statement in tables:
	cursor.execute(table_statement)

connection.commit()
connection.close()
