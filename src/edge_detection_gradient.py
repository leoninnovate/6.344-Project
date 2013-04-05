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
from two_D_convolution import clipped_fft_convolve
from two_D_signal import Two_D_Signal
from util import strip_dir
from util import strip_file_name

def compute_gradient(signal, h):
  """
  Computes the gradient of the given |signal| using the given filter |h|.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  assert isinstance(h, Two_D_Signal), 'h must be a Two_D_Signal'
  return clipped_fft_convolve(signal, h)

def invert(signal, MAX):
  """
  Returns the given |signal| inverted.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  return Two_D_Signal({key: MAX - value for (key, value) in
      signal.values.items()})

def detect_edges(image_path):
  """
  Saves a new image that presents the non-directional edges in the image saved
      at the given |image_path|.
  """
  print '\tcomputing 2D signal from image path'
  signal = image_to_two_D_signal(image_path)
  print '\tcomputing horizontal gradient'
  horizontal_gradient = compute_gradient(signal, HORIZONTAL_EDGE_FILTER)
  print '\tcomputing vertical gradient'
  vertical_gradient = compute_gradient(signal, VERTICAL_EDGE_FILTER)
  print '\tcomputing non-directional gradient'
  non_directional_gradient = Two_D_Signal({key: sqrt(horizontal_gradient[
      key] ** 2 + vertical_gradient[key] ** 2) for key in
      horizontal_gradient.values})
  print '\tcomputing gradient magnitude'
  abs_gradient = abs(non_directional_gradient)
  print '\tfinding maximum gradient magnitude'
  max_abs = max(abs_gradient.non_zero_values())
  print '\tscaling abs image by 255 / maximum gradient magnitude'
  scaled = (255 / max_abs) * abs_gradient
  print '\tinverting scaled image'
  inverted = invert(scaled, 255)
  print '\tsaving result image'
  new_image_path = join(strip_dir(image_path), '%s_edges.%s' % tuple(
      strip_file_name(image_path).split('.')))
  two_D_signal_to_image(inverted, new_image_path)
  print '\tdone'
