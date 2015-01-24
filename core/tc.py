class TransitiveClosure(object):

  def __init__(self, tuples):
    self.id_to_class = {}
    for id1, id2 in tuples:
      self.merge(id1, id2)

  def get_tuples(self):
    return self.tuples_from_classes(self.get_classes())

  def get_classes(self):
    return set([tuple(sorted(a)) for a in self.id_to_class.values()])

  def merge(self, id1, id2):
    new_class = self.get_class(id1).union(self.get_class(id2))
    for tuple_id in new_class:
      self.id_to_class[tuple_id] = new_class

  def get_class(self, tuple_id):
    if tuple_id in self.id_to_class:
      return self.id_to_class[tuple_id]
    return {tuple_id}

  def tuples_from_classes(self, classes):
    result = []
    for equivalence_class in classes:
      for i in range(len(equivalence_class) - 1):
        for j in range(i + 1, len(equivalence_class)):
          result.append((equivalence_class[i], equivalence_class[j]))
    return result
