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
from util import invert
from util import scaler
from util import strip_dir
from util import strip_file_name

def detect_edges_gradient(image_path, alpha):
  """
  Saves a new image that presents the non-directional edges in the image saved
      at the given |image_path|. This method uses the Gradient based method for
      edge detection. |alpha|, a number greater than 0, is a parameter to
      determine which pixels to consider edges. The higher the value of |alpha|
      the higher the gradient has to be to for a pixel to be selected.
  """
  print '\tcomputing 2D signal from image path'
  signal = image_to_two_D_signal(image_path)
  print '\tcomputing horizontal gradient'
  horizontal_gradient = clipped_fft_convolve(signal, HORIZONTAL_EDGE_FILTER)
  print '\tcomputing vertical gradient'
  vertical_gradient = clipped_fft_convolve(signal, VERTICAL_EDGE_FILTER)
  print '\tcomputing non-directional gradient'
  non_directional_gradient = Two_D_Signal({key: sqrt(horizontal_gradient[
      key] ** 2 + vertical_gradient[key] ** 2) for key in
      horizontal_gradient.values})
  print '\tfinding maximum gradient magnitude'
  max_abs = max(non_directional_gradient.non_zero_values())
  print '\tscaling gradient image with alpha=%s' % alpha
  scale_f = scaler(max_abs, 255, alpha)
  scaled = Two_D_Signal({key: scale_f(non_directional_gradient[key]) for key in
      non_directional_gradient.values})
  print '\tinverting scaled image'
  inverted = invert(scaled, 255)
  print '\tsaving result image'
  new_image_path = join(strip_dir(image_path), '%s_gradient_edges.%s' % tuple(
      strip_file_name(image_path).split('.')))
  two_D_signal_to_image(inverted, new_image_path)
  print '\tdone'
