## -*- coding: utf-8 -*-

import csv

class Reader:

  FILENAME = ''
  ATTRIBUTES = []

  def get_tuples(self):
    tuples = []
    with open(self.FILENAME) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        tupled_row = tuple(row[attribute] for attribute in self.ATTRIBUTES)
        tuples.append(tupled_row)
    return tuples
      
class RestaurantReader(Reader):
  
  FILENAME = '../../data/restaurant.csv'
  ATTRIBUTES = ['id', 'name', 'addr', 'city', 'phone', 'type', 'class']

class AddressesReader(Reader):

  FILENAME = '../../data/addresses.csv'
  ATTRIBUTES = ['id', 'anrede', 'titel', 'vorname', 'nachname', 'nummer_1', 'adresse_strasse', 'adresse_nr', 'adresse_plz', 'adresse_ort', 'tel', 'nummer_2', 'nummer_3']

class CDReader(Reader):

  FILENAME = '../../data/cd.csv'
  ATTRIBUTES = ['pk', 'id', 'artist', 'title', 'category', 'genre', 'cdextra', 'year', 'track01', 'track02', 'track03', 'track04', 'track05', 'track06', 'track07', 'track08', 'track09', 'track10', 'track11', 'track12', 'track13', 'track14', 'track15', 'track16', 'track17', 'track18', 'track19', 'track20', 'track21', 'track22', 'track23', 'track24', 'track25', 'track26', 'track27', 'track28', 'track29', 'track30', 'track31', 'track32', 'track33', 'track34', 'track35', 'track36', 'track37', 'track38', 'track39', 'track40', 'track41', 'track42', 'track43', 'track44', 'track45', 'track46', 'track47', 'track48', 'track49', 'track50', 'track51', 'track52', 'track53', 'track54', 'track55', 'track56', 'track57', 'track58', 'track59', 'track60', 'track61', 'track62', 'track63', 'track64', 'track65', 'track66', 'track67', 'track68', 'track69', 'track70', 'track71', 'track72', 'track73', 'track74', 'track75', 'track76', 'track77', 'track78', 'track79', 'track80', 'track81', 'track82', 'track83', 'track84', 'track85', 'track86', 'track87', 'track88', 'track89', 'track90', 'track91', 'track92', 'track93', 'track94', 'track95', 'track96', 'track97', 'track98', 'track99']
