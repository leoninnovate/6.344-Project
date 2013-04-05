"""
Script to convolve 2D signals.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from scipy.signal import fftconvolve
from two_D_signal import Two_D_Signal

def padded_signal(signal, n1_pad, n2_pad):
  """
  Returns a Two_D_Signal by repeating the edge values of |signal| by |n1_pad|
      values in the n1 direction and |n2_pad| in the n2 direction.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  new_values = signal.values.copy()
  for n1 in xrange(signal.n1_min, signal.n1_max + 1):
    for n2_p in xrange(1, n2_pad + 1):
      new_values[(n1, signal.n2_min - n2_p)] = signal.value(n1, signal.n2_min)
      new_values[(n1, signal.n2_max + n2_p)] = signal.value(n1, signal.n2_max)
  for n2 in xrange(signal.n2_min, signal.n2_max + 1):
    for n1_p in xrange(1, n1_pad + 1):
      new_values[(signal.n1_min - n1_p, n2)] = signal.value(signal.n1_min, n2)
      new_values[(signal.n1_max + n1_p, n2)] = signal.value(signal.n1_max, n2)
  for n1_p in xrange(1, n1_pad + 1):
    for n2_p in xrange(1, n2_pad + 1):
      new_values[(signal.n1_min - n1_p, signal.n2_min - n2_p)] = signal.value(
          signal.n1_min, signal.n2_min)
      new_values[(signal.n1_min - n1_p, signal.n2_max + n2_p)] = signal.value(
          signal.n1_min, signal.n2_max)
      new_values[(signal.n1_max + n1_p, signal.n2_min - n2_p)] = signal.value(
          signal.n1_max, signal.n2_min)
      new_values[(signal.n1_max + n1_p, signal.n2_max + n2_p)] = signal.value(
          signal.n1_max, signal.n2_max)
  return Two_D_Signal(new_values)

def clipped_signal(signal, new_n1_min, new_n1_max, new_n2_min, new_n2_max):
  """
  Returns clipped version of |signal|.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  def key_in_bound(key):
    n1, n2 = key
    return new_n1_min <= n1 <= new_n1_max and new_n2_min <= n2 <= new_n2_max
  return Two_D_Signal({key: value for key, value in signal.values.items() if
      key_in_bound(key)})

def fft_convolve(f, g):
  """
  TODO(mikemeko)
  """
  assert isinstance(f, Two_D_Signal), 'f must be a Two_D_Signal'
  assert isinstance(g, Two_D_Signal), 'g must be a Two_D_Signal'
  return Two_D_Signal.from_two_D_array(fftconvolve(f.to_two_D_array(max(0,
      g.n1_min - f.n1_min), max(0, g.n2_min - f.n2_min)), g.to_two_D_array(
      max(0, f.n1_min - g.n1_min), max(0, f.n2_min - g.n2_min))), f.n1_min,
      f.n2_min)

def clipped_fft_convolve(f, g):
  """
  TODO(mikemeko)
  """
  return clipped_signal(fft_convolve(padded_signal(f, g.n1_max - g.n1_min,
      g.n2_max - g.n2_min), g), f.n1_min - g.n1_min,
      f.n1_max + g.n1_max, f.n2_min - g.n2_min, f.n2_max + g.n2_max)
