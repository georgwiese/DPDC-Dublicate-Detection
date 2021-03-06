import os
import sys

from core.snm import SortedNeighborhoodMethod
from core.tc import TransitiveClosure
from core.analyzers import *
from core.comparators import *
from data.reader import *

class DuplicateDetector(object):

  WINDOW_SIZE = 20
  OUT_FILE = 'results.txt'

  def __init__(self, reader, analyzer, comparators):
    self.reader = reader
    self.analyzer = analyzer
    self.comparators = comparators

  def find_duplicates(self):
    print "Reading dataset..."
    tuples = self.reader.get_tuples()
    duplicates = set()

    for i, comparator in enumerate(self.comparators):
      print "Finding duplicates (%d / %d)..." % (i + 1, len(self.comparators))
      smm = SortedNeighborhoodMethod(
        comparator.compare, self.analyzer.is_same,
        tuples, self.WINDOW_SIZE)
      duplicates = duplicates.union(smm.find_duplicates())

    print "Computing transitive closure..."
    duplicate_tuples = TransitiveClosure(duplicates).get_tuples()

    print "Writing file..."
    with open(self.OUT_FILE, 'w') as output_file:
      for duplicate_tuple in duplicate_tuples:
        output_file.write("%d,%d\n" % duplicate_tuple)


if __name__ == '__main__':
  if len(sys.argv) != 2:
    print "Usage: python duplicate_detector path/to/csv.file"
    exit(42)

  reader = AddressesReader(sys.argv[1])
  analyzer = AddressesAnalyzer()
  comparators = [
      AddressesAddressComparator(),
      AddressesFirstNameComparator(),
      AddressesLastNameComparator(),
      AddressesNamesReversedComparator(),
  ]

  DuplicateDetector(reader, analyzer, comparators).find_duplicates()
