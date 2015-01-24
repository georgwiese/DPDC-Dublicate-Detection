class SortedNeighborhoodMethod(object):

  def __init__(self, compare, is_same, data, window_size):
    self.compare = compare
    self.is_same = is_same
    self.data = data
    self.window_size = window_size

  def find_duplicates(self):
    result = []
    sorted_data = sorted(self.data, key=self.compare)

    for i in range(0, len(sorted_data) - window_size):
      for j in range(i + 1, i + window_size):
        if is_same(sorted_data[i], sorted_data[j]):
          result.append((sorted_data[i][0], sorted_data[j][0]))

    return result
