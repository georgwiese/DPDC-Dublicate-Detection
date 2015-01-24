import argparse
from core.tc import TransitiveClosure
from data.reader import RestaurantReader, CDReader, AddressesReader

def print_goldstandard_diff(resultfile, goldstandard):
  result_tuples = set(get_tuples(resultfile))
  gold_tuples = set(get_tuples(goldstandard))

  fp = result_tuples.difference(gold_tuples)
  fn = gold_tuples.difference(result_tuples)
  print "Result, but not gold standard (FP):", fp
  print "Gold standard, but not result (FN):", fn

  precision = float(len(result_tuples) - len(fp)) / len(result_tuples)
  recall = float(len(result_tuples) - len(fp)) / len(gold_tuples)
  f_measure = 2 * precision * recall / (precision + recall)

  print "Precision %f, recall %f, f-measure %f" % (precision, recall, f_measure)


def print_data(resultfile, reader):
  classes = TransitiveClosure(get_tuples(resultfile)).get_classes()
  data = {int(t[0]) : t for t in reader.get_tuples()}

  for i, tuple_class in enumerate(classes):
    print "Class", i
    for member in tuple_class:
      print data[member]


def get_tuples(resultfile):
  lines = [line.strip() for line in open(resultfile)]
  return [tuple([int(x) for x in line.split(",")]) for line in lines]

def get_args():
  parser = argparse.ArgumentParser(description='Evaluate a given result file')
  parser.add_argument('--resultfile',
    dest='resultfile', action='store', default='',
    help='Result file to evaluate')
  parser.add_argument('--goldstandard',
    dest='goldstandard', action='store', default='',
    help='Gold standard to compare with')
  parser.add_argument('--dataset',
    dest='dataset', action='store', default='',
    help='Data set')
  return parser.parse_args()

READERS = {
  'restaurants': RestaurantReader(),
  'cd': CDReader(),
  'addresses': AddressesReader()
}

if __name__ == '__main__':
  args = get_args()
  if not args.resultfile:
    print "Error: You must specify a result file"
    exit(1)

  if args.goldstandard:
    print_goldstandard_diff(args.resultfile, args.goldstandard)
  elif args.dataset:
    print_data(args.resultfile, READERS[args.dataset])
  else:
    print "Error: You must specify a gold standard or data file"
    exit(1)
