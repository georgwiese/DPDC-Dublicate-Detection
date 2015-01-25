## -*- coding: utf-8 -*-

import re
import cleaners

class Comparator(object):

    def compare(self, tuple1, tuple2):
        raise NotImplementedError()


class DummyComparator(Comparator):

    def compare(self, tuple1, tuple2):
        return tuple1[0] - tuple2[0]

class AddressesGoldComparator(Comparator):

    def compare(self, tuple1, tuple2):
        return int(tuple1[12]) - int(tuple2[12])


class SortKeyComparator(Comparator):

    def compare(self, tuple1, tuple2):
        sk1 = self.get_sort_key(tuple1)
        sk2 = self.get_sort_key(tuple2)
        if sk1 < sk2:
            return -1
        elif sk1 == sk2:
            return 0
        else:
            return 1

    def get_sort_key(self, entity): raise NotImplementedError()


class AddressesAddressComparator(SortKeyComparator):

    ADDRESS_CLEANER = cleaners.AddressCleaner()

    def get_sort_key(self, entity):
        #6 straße nummer plz ort
        street_name = self.ADDRESS_CLEANER.clean_street_name(entity[6])
        number = entity[7]
        zip_code = self.ADDRESS_CLEANER.clean_zip_code(entity[8])
        return zip_code + street_name + number
