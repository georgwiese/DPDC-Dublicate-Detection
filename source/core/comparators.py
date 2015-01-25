class Comparator(object):

  def compare(self, tuple1, tuple2):
    pass


class DummyComparator(Comparator):

  def compare(self, tuple1, tuple2):
    return tuple1[0] - tuple2[0]

class AddressesGoldComparator(Comparator):

  def compare(self, tuple1, tuple2):
    return int(tuple1[12]) - int(tuple2[12])
