## -*- coding: utf-8 -*-

import sqlite3

from reader import *


tables = {'Restaurants': RestaurantReader(), 'CD': CDReader(), 'Addresses': AddressesReader()}

connection = sqlite3.connect('../../data/data.sqlite')
connection.text_factory = str

cursor = connection.cursor()

for key in tables.keys():
	values = tables[key].get_tuples()
	value_string = '(' + ','.join(['?' for x in values[0]]) + ')'

	cursor.executemany("INSERT INTO " + key + " VALUES " + value_string, values)
	connection.commit()

connection.close()

