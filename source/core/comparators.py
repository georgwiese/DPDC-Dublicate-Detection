## -*- coding: utf-8 -*-

import re

class Comparator(object):

    def compare(self, tuple1, tuple2):
        raise NotImplementedError()


class DummyComparator(Comparator):

    def compare(self, tuple1, tuple2):
        return tuple1[0] - tuple2[0]

class AddressesGoldComparator(Comparator):

    def compare(self, tuple1, tuple2):
        return int(tuple1[12]) - int(tuple2[12])


class AddressesAddressComparator(Comparator):

    number_regex = re.compile(r"\D", re.IGNORECASE)

    def compare(self, tuple1, tuple2):
        sk1 = self.get_sort_key(tuple1)
        sk2 = self.get_sort_key(tuple2)
        if sk1 < sk2:
            return -1
        elif sk1 == sk2:
            return 0
        else:
            return 1

    def get_sort_key(self, entity):
        #6 straße nummer plz ort
        street_name = self.get_cleaned_street_name(entity[6])
        number = self.get_cleaned_number(entity[7])
        zip_code = self.get_cleaned_zip_code(entity[8])
        return zip_code + street_name + number

    def get_cleaned_zip_code(self, zip_code):
        return zip_code.replace('D-', '')

    def get_cleaned_street_name(self, street_name):
        return (street_name
            .replace('str.', '')
            .replace('strasse', '')
            .replace('straße', '')
            .strip())

    def get_cleaned_number(self, number):
        return self.number_regex.sub('', number)

