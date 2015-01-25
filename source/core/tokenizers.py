import cleaners

class NameTokenizer(object):

  def tokenize(self, first_name, last_name):
    tokens = (
      first_name.replace('-', ' ').split() +
      last_name.replace('-', ' ').split()
    )
    return [token for token in tokens if token]

class AddressTokenizer(object):

  ADDRESS_CLEANER = cleaners.AddressCleaner()

  def tokenize(self, street, number, zipcode, city):
    street = self.ADDRESS_CLEANER.clean_street_name(street)
    zipcode = self.ADDRESS_CLEANER.clean_zip_code(zipcode)

    tokens = (
      street.replace('-', ' ').split() +
      number.split() +
      zipcode.split() +
      city.split()
    )

    return [token for token in tokens if token]
