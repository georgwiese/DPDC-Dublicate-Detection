class NameTokenizer(object):

  def tokenize(self, first_name, last_name):
    tokens = first_name.split(" ") + last_name.split(" ")
    return [token for token in tokens if token]

