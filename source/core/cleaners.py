## -*- coding: utf-8 -*-

class AddressCleaner:

  def clean_zip_code(self, zip_code):
    return zip_code.replace('D-', '')

  def clean_street_name(self, street_name):
    return (street_name
        .replace('strasse', 'str.')
        .replace('straße', 'str.')
        .strip())

class PhoneNumberCleaner:

  def clean(self, phone_number):
    return (phone_number
        .replace('+49(0)', '0')
        .replace('0049(0)', '0')
        .replace('+49', '0')
        .replace('0049', '0')
        .replace('/', '')
        .replace('-', '')
        .strip())
