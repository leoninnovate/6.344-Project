"""
Representation for finite-extent 2D signals.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from numpy import array

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
    Returns the value corresponding to the tuple (n1, n2).
    """
    return self.values[(n1, n2)] if (n1, n2) in self.values else 0
  def to_two_D_array(self):
    """
    TODO(mikemeko)
    """
    return array([[self.value(n1, n2) for n2 in xrange(self.n2_min,
        self.n2_max + 1)] for n1 in xrange(self.n1_min, self.n1_max + 1)])
  @staticmethod
  def from_two_D_array(two_D_array):
    """
    TODO(mikemeko)
    """
    # TODO(mikemeko): row/col vs. n1/n2
    values = {}
    num_rows, num_cols = two_D_array.shape
    for n1 in xrange(num_rows):
      for n2 in xrange(num_cols):
        values[(n1, n2)] = two_D_array[n1][n2]
    return Two_D_Signal(values)
  def __str__(self):
    return str(self.values)
