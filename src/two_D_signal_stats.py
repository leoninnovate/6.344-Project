"""
Methods to collect statistics about 2D signals.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from two_D_convolution import clipped_fft_convolve
from two_D_signal import Two_D_Signal
from util import padded_signal

def mean_signal(signal, M):
  """
  Returns a Two_D_Signal representing the mean of |signal| at each point (n1,
      n2), where the average is taken including all points from (n1 - |M|,
      n2 - |M|) to (n1 + |M|, n2 + |M|).
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  mean_filter = Two_D_Signal({(n1, n2): 1. / (2 * M + 1) ** 2 for n1 in xrange(
      -M, M + 1) for n2 in xrange(-M, M + 1)})
  return clipped_fft_convolve(signal, mean_filter)

def var_signal(signal, M):
  """
  Returns a Two_D_Signal representing the variance of |signal| at each point
      (n1, n2), where the variance is taken including all points from
      (n1 - |M|, n2 - |M|) to (n1 + |M|, n2 + |M|).
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  padded = padded_signal(signal, M, M)
  mean = mean_signal(signal, M)
  var_values = {}
  for n1 in xrange(signal.n1_min, signal.n1_max + 1):
    for n2 in xrange(signal.n2_min, signal.n2_max + 1):
      var_values[(n1, n2)] = sum((padded[i, j] - mean[i, j]) ** 2 for i in
          xrange(n1 - M, n1 + M + 1) for j in xrange(n2 - M, n2 + M + 1)) / (
          2 * M + 1.) ** 2
  return Two_D_Signal(var_values)
