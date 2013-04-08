"""
Edge detection using the laplacian method.
TODO(mikemeko): add a noise reduction system prior to edge detection.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from constants import EPSILON
from constants import LAPLACIAN_FILTER
from image_two_D_signal_conversion import image_to_two_D_signal
from image_two_D_signal_conversion import two_D_signal_to_image
from os.path import join
from two_D_convolution import clipped_fft_convolve
from two_D_signal import Two_D_Signal
from util import strip_dir
from util import strip_file_name

def compute_laplacian(signal):
  """
  Computes (approximately) the laplacian of the given |signal|.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  return clipped_fft_convolve(signal, LAPLACIAN_FILTER)

def detect_edges_laplacian(image_path):
  """
  Saves a new image that presentsthe edges in the image saved at the given
      |image_path|. This method uses the Laplacian based method for edge
      detection.
  """
  print '\tcomputing 2D signal from image path'
  signal = image_to_two_D_signal(image_path)
  print '\tcomputing laplacian'
  laplacian = compute_laplacian(signal)
  print '\tcomputing zero crossings'
  zero_crossings = Two_D_Signal({key: 255 * (abs(laplacian[key]) < EPSILON) for
      key in laplacian.values})
  print '\tsaving result image'
  new_image_path = join(strip_dir(image_path), '%s_laplacian_edges.%s' % tuple(
      strip_file_name(image_path).split('.')))
  two_D_signal_to_image(zero_crossings, new_image_path)
  print '\tdone'
