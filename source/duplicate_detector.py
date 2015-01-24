import os

from core.snm import SortedNeighborhoodMethod
from core.tc import TransitiveClosure
from core.analyzers import *
from data.reader import *

class DuplicateDetector(object):

  ANALYZER = DummyAnalyzer()
  WINDOW_SIZE = 20
  OUT_DIR = '../out/'
  OUT_FILE = 'result.txt'

  def __init__(self, reader):
    self.reader = reader

  def find_duplicates(self):
    tuples = self.reader.get_tuples()
    smm = SortedNeighborhoodMethod(
      self.ANALYZER.compare, self.ANALYZER.is_same,
      tuples, self.WINDOW_SIZE)

    print "Finding duplicates..."
    duplicates = smm.find_duplicates()
    print "Computing transitive closure..."
    duplicate_tuples = TransitiveClosure(duplicates).get_tuples()

    print "Writing file..."
    if not os.path.exists(self.OUT_DIR):
      os.makedirs(self.OUT_DIR)
    with open(self.OUT_DIR + self.OUT_FILE, 'w') as output_file:
      for duplicate_tuple in duplicate_tuples:
        output_file.write("%d,%d\n" % duplicate_tuple)


if __name__ == '__main__':
  DuplicateDetector(CDReader()).find_duplicates()
