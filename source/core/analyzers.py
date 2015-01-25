import tokenizers
import cleaners
import Levenshtein

class Analyzer(object):

  def is_same(self, tuple1, tuple2): raise NotImplementedError()

  def combine_weighted(self, features):
    weighted_features = [(weight, weight * feature)
                            for (weight, feature) in features]
    def sum((weight1, feature1), (weight2, feature2)):
      return (weight1 + weight2, feature1 + feature2)
    (weightSum, featureSum) = reduce(sum, weighted_features)
    return featureSum / weightSum

  def compare_distinct_values(self, string1, string2, base_weight):
    if not string1 or not string2:
      return (0, 0)
    if string1 == string2:
      return (base_weight, 1)
    if string1 in string2 or string2 in string1:
      return (base_weight / 2, 0.5)
    return (base_weight, 0)

  def monge_elkan(self, tokenset1, tokenset2, sim):
    best_similarities = []
    for token1 in tokenset1:
      best_similarity = 0
      for token2 in tokenset2:
        best_similarity = max(best_similarity, sim(token1, token2))
      best_similarities.append(best_similarity)
    return sum(best_similarities) / len(best_similarities)

class DummyAnalyzer(Analyzer):

  def is_same(self, tuple1, tuple2):
    return tuple1[0] % 10 == 0 and tuple2[0] % 10 == 0

class AddressesGoldAnalyzer(Analyzer):

  def is_same(self, tuple1, tuple2):
    return tuple1[12] == tuple2[12]

class AbstractAddressesAnalyzers(Analyzer):

  SALUTATION_WEIGHT = 10
  TITLE_WEIGHT = 10
  NAME_WEIGHT = 50
  ADDRESS_WEIGHT = 50
  PHONE_WEIGHT = 50
  THRESHOLD = 0.85

  def is_same(self, tuple1, tuple2):
    similarity = self.combine_weighted([
      self.salutation_similarity(tuple1, tuple2),
      self.title_similarity(tuple1, tuple2),
      self.name_similarity(tuple1, tuple2),
      self.address_similarity(tuple1, tuple2),
      self.tel_similarity(tuple1, tuple2),
    ])
    return similarity > self.THRESHOLD

  def salutation_similarity(self, tuple1, tuple2): raise NotImplementedError()
  def title_similarity(self, tuple1, tuple2): raise NotImplementedError()
  def name_similarity(self, tuple1, tuple2): raise NotImplementedError()
  def address_similarity(self, tuple1, tuple2): raise NotImplementedError()
  def tel_similarity(self, tuple1, tuple2): raise NotImplementedError()

class AddressesAnalyzer(AbstractAddressesAnalyzers):

  def __init__(self):
    self.name_tokenizer = tokenizers.NameTokenizer()
    self.address_tokenizer = tokenizers.AddressTokenizer()
    self.phone_cleaner = cleaners.PhoneNumberCleaner()

  def salutation_similarity(self, tuple1, tuple2):
    return self.compare_distinct_values(tuple1[1], tuple2[1], self.SALUTATION_WEIGHT)

  def title_similarity(self, tuple1, tuple2):
    return self.compare_distinct_values(tuple1[1], tuple2[1], self.TITLE_WEIGHT)

  def name_similarity(self, tuple1, tuple2):
    tokenset1 = self.name_tokenizer.tokenize(tuple1[3], tuple1[4])
    tokenset2 = self.name_tokenizer.tokenize(tuple2[3], tuple2[4])
    similarity = self.monge_elkan(tokenset1, tokenset2, Levenshtein.ratio)
    return (self.NAME_WEIGHT, similarity)

  def address_similarity(self, tuple1, tuple2):
    tokenset1 = self.address_tokenizer.tokenize(tuple1[6], tuple1[7], tuple1[8], tuple1[9])
    tokenset2 = self.address_tokenizer.tokenize(tuple2[6], tuple2[7], tuple2[8], tuple2[9])
    similarity = self.monge_elkan(tokenset1, tokenset2, Levenshtein.ratio)
    return (self.ADDRESS_WEIGHT, similarity)

  def tel_similarity(self, tuple1, tuple2):
    tel1 = self.phone_cleaner.clean(tuple1[10])
    tel2 = self.phone_cleaner.clean(tuple2[10])

    if not tel1 or not tel2:
      return (0, 0)

    similarity = Levenshtein.ratio(tel1, tel2)
    return (self.PHONE_WEIGHT, similarity)

