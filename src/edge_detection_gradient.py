"""
Edge detection using the gradient method.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from constants import HORIZONTAL_EDGE_FILTER
from constants import VERTICAL_EDGE_FILTER
from image_two_D_signal_conversion import image_to_two_D_signal
from image_two_D_signal_conversion import two_D_signal_to_image
from math import sqrt
from os.path import join
from two_D_convolution import fft_convolve
from two_D_signal import Two_D_Signal
from util import strip_dir
from util import strip_file_name

def compute_gradient(signal, h):
  """
  Computes the gradient of the given |signal| using the given filter |h|.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  assert isinstance(h, Two_D_Signal), 'h must be a Two_D_Signal'
  return fft_convolve(signal, h)

def compute_abs(signal):
  """
  Computes the absolute value of the given |signal|.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  return Two_D_Signal({key: abs(value) for (key, value) in
      signal.values.items()})

def compare_with_threshold(signal, threshold):
  """
  Returns a new Two_D_Signal with 1s at indices where |signal| is above the
      |threshold|, and 0s elsewhere.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  return Two_D_Signal({key: int(value > threshold) for (key, value) in
      signal.values.items()})

def scale(signal, k):
  """
  Returns the given |signal| scaled by |k|.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  return Two_D_Signal({key: k * value for (key, value) in
      signal.values.items()})

def invert(signal, MAX=255):
  """
  Returns the given |signal| inverted.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  return Two_D_Signal({key: MAX - value for (key, value) in
      signal.values.items()})

def detect_edges(image_path):
  """
  TODO(mikemeko)
  """
  print 'computing 2D signal from image path'
  signal = image_to_two_D_signal(image_path)
  print 'computing horizontal gradient'
  horizontal_gradient = compute_gradient(signal, HORIZONTAL_EDGE_FILTER)
  print 'computing vertical gradient'
  vertical_gradient = compute_gradient(signal, VERTICAL_EDGE_FILTER)
  print 'computing non-directional gradient'
  non_directional_gradient = Two_D_Signal({key: sqrt(horizontal_gradient.value(
      *key) ** 2 + vertical_gradient.value(*key) ** 2) for key in
      horizontal_gradient.values})
  print 'computing gradient magnitude'
  abs_gradient = compute_abs(non_directional_gradient)
  print 'comparing with threshold'
  vs_threshold = compare_with_threshold(abs_gradient, 50)
  print 'scaling threshold image'
  scaled = scale(vs_threshold, 255)
  print 'inverting scaled image'
  inverted = invert(scaled)
  print 'computing new image path'
  new_image_path = join(strip_dir(image_path), 'edges_%s' % strip_file_name(
      image_path))
  two_D_signal_to_image(inverted, new_image_path)
  print 'done'

if __name__ == '__main__':
  detect_edges('../images/lena.png')
