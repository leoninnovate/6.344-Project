"""
Script to convolve 2D signals.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from two_D_signal import Two_D_Signal

def convolve(f, g):
  """
  Returns a Two_D_Signal representing the convolution of the two given
      Two_D_Signal |f| and |g|.
  TODO(mikemeko): use row-column decomposition; maybe use FFT.
  """
  assert isinstance(f, Two_D_Signal), 'f must be a Two_D_Signal'
  assert isinstance(g, Two_D_Signal), 'g must be a Two_D_Signal'
  return Two_D_Signal({(n1, n2): sum(f.value(k1, k2) * g.value(n1 - k1,
      n2 - k2) for k1 in xrange(f.n1_min, f.n1_max + 1) for k2 in xrange(
      f.n2_min, f.n2_max + 1)) for n1 in xrange(f.n1_min + g.n1_min, f.n1_max +
      g.n1_max + 1) for n2 in xrange(f.n2_min + g.n2_min, f.n2_max + g.n2_max +
      1)})
