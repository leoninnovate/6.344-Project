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
    # record extent of the signal
    self.n1_min = min(key[0] for key in values.keys())
    self.n1_max = max(key[0] for key in values.keys())
    self.width = self.n1_max - self.n1_min + 1
    self.n2_min = min(key[1] for key in values.keys())
    self.n2_max = max(key[1] for key in values.keys())
    self.height = self.n2_max - self.n2_min + 1
  def bounds(self):
    """
    Returns the bounds of this signal in the form (n1_min, n1_max, n2_min,
        n2_max).
    """
    return (self.n1_min, self.n1_max, self.n2_min, self.n2_max)
  def to_two_D_array(self, n1_shift=0, n2_shift=0):
    """
    Returns the content of this signal as a 2D array. By default, the array
        will have width self.width and height self.height. If |n1_shift| and
        |n2_shift| are provided, the array will be padded with 0s by the given
        amounts before the self.n1_min and self.n2_min values respectively.
    """
    return array([[self[n1, n2] for n1 in xrange(self.n1_min - n1_shift,
        self.n1_max + 1)] for n2 in xrange(self.n2_min - n2_shift,
        self.n2_max + 1)])
  @staticmethod
  def from_two_D_array(two_D_array, n1_min=0, n2_min=0):
    """
    Returns a Two_D_Signal constructed using using the given |two_D_array|.
        |n1_min| and |n2_min| will be the mins for the resulting Two_D_Signal.
    """
    values = {}
    num_rows, num_cols = two_D_array.shape
    for n1 in xrange(num_cols):
      for n2 in xrange(num_rows):
        values[(n1_min + n1, n2_min + n2)] = two_D_array[n2][n1]
    return Two_D_Signal(values)
  def __getitem__(self, (n1, n2)):
    return self.values[(n1, n2)] if (n1, n2) in self.values else 0
  def __str__(self):
    return str(self.values)
