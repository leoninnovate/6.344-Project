"""
Representation for 2D signals.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

class Two_D_Signal:
  """
  Representation for a 2D signal.
  """
  def __init__(self, values):
    """
    The values of this 2D signal represented as a dictionary mapping (n1, n2)
        tuples to the corresponding values.
    """
    assert isinstance(values, dict), 'values must be a dictionary'
    self.values = values
    self.n1_min = min(key[0] for key in values.keys())
    self.n1_max = max(key[0] for key in values.keys())
    self.n2_min = min(key[1] for key in values.keys())
    self.n2_max = max(key[1] for key in values.keys())
  def value(self, n1, n2):
    """
    Returns the value corresponding to the tuple (n1, n2), assuming that this
        value has been recorded.
    """
    assert (n1, n2) in self.values
    return self.values[(n1, n2)]
  def __str__(self):
    return str(self.values)
