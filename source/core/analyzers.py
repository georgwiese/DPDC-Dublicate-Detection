
class Analyzer(object):

  def is_same(self, tuple1, tuple2):
    pass


class DummyAnalyzer(Analyzer):

  def is_same(self, tuple1, tuple2):
    return tuple1[0] % 10 == 0 and tuple2[0] % 10 == 0
