"""
Utility methods.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from os.path import isdir
from os.path import isfile
from os.path import split
from two_D_signal import Two_D_Signal

def padded_signal(signal, n1_pad, n2_pad):
  """
  Returns a Two_D_Signal by repeating the edge values of |signal| by |n1_pad|
      values in the n1 directions and |n2_pad| in the n2 directions.
  """
  # input signal: X
  #                ABC
  # output signal: DXE
  #                FGH
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  new_values = signal.values.copy()
  for n1 in xrange(signal.n1_min, signal.n1_max + 1):
    for n2_p in xrange(1, n2_pad + 1):
      new_values[(n1, signal.n2_min - n2_p)] = signal[n1, signal.n2_min] # G
      new_values[(n1, signal.n2_max + n2_p)] = signal[n1, signal.n2_max] # B
  for n2 in xrange(signal.n2_min, signal.n2_max + 1):
    for n1_p in xrange(1, n1_pad + 1):
      new_values[(signal.n1_min - n1_p, n2)] = signal[signal.n1_min, n2] # D
      new_values[(signal.n1_max + n1_p, n2)] = signal[signal.n1_max, n2] # E
  for n1_p in xrange(1, n1_pad + 1):
    for n2_p in xrange(1, n2_pad + 1):
      new_values[(signal.n1_min - n1_p, signal.n2_min - n2_p)] = signal[
          signal.n1_min, signal.n2_min] # F
      new_values[(signal.n1_min - n1_p, signal.n2_max + n2_p)] = signal[
          signal.n1_min, signal.n2_max] # H
      new_values[(signal.n1_max + n1_p, signal.n2_min - n2_p)] = signal[
          signal.n1_max, signal.n2_min] # A
      new_values[(signal.n1_max + n1_p, signal.n2_max + n2_p)] = signal[
          signal.n1_max, signal.n2_max] # C
  return Two_D_Signal(new_values)

def clipped_signal(signal, new_n1_min, new_n1_max, new_n2_min, new_n2_max):
  """
  Returns a clipped version of |signal|, clipped by the given parameters.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  def key_in_bound(key):
    n1, n2 = key
    return new_n1_min <= n1 <= new_n1_max and new_n2_min <= n2 <= new_n2_max
  return Two_D_Signal({key: value for key, value in signal.values.items() if
      key_in_bound(key)})

def invert(signal, MAX):
  """
  Returns the given |signal| inverted.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  return Two_D_Signal({key: MAX - value for (key, value) in
      signal.values.items()})

def scaler(max_x, max_y, alpha):
  """
  Returns a function that given a number x returns
      |max_y| * (x / |max_x|) ** |alpha|.
  When |alpha| is one, the return function is just a line through (0, 0) and
      (|max_x|, |max_y|). |alpha| can be thought of as a parameter to control
      the curveture of the curve through those two points.
  """
  return lambda x: max_y * (float(x) / max_x) ** alpha

def strip_file_name(path):
  """
  Returns the file name of the given |path|, or '' on failure.
  """
  return split(path)[-1] if path and isfile(path) else ''

def strip_dir(path):
  """
  Returns the directory for the given |path|, or '' on failure.
  """
  if path:
    if isdir(path):
      return path
    elif isfile(path):
      return split(path)[0]
  return ''
