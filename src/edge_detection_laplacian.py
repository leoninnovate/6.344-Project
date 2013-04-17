"""
Edge detection using the laplacian method.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from constants import GAUSSIAN_FILTER
from constants import LAPLACIAN_FILTER
from image_two_D_signal_conversion import image_to_two_D_signal
from image_two_D_signal_conversion import two_D_signal_to_image
from os.path import join
from scipy.stats import scoreatpercentile
from two_D_signal_stats import var_signal
from two_D_convolution import clipped_fft_convolve
from util import invert
from util import strip_dir
from util import strip_file_name

def detect_edges_laplacian(image_path):
  """
  Saves a new image that presentsthe edges in the image saved at the given
      |image_path|. This method uses the Laplacian based method for edge
      detection.
  """
  print '\tcomputing 2D signal from image path'
  signal = image_to_two_D_signal(image_path)
  print '\tblurring image'
  blurred = clipped_fft_convolve(signal, GAUSSIAN_FILTER)
  print '\tcomputing laplacian'
  laplacian = clipped_fft_convolve(blurred, LAPLACIAN_FILTER)
  print '\tcomputing abs'
  abs_laplacian = abs(laplacian)
  print '\tfinding cutoff abs: 95th percentile abs'
  cutoff_abs = scoreatpercentile(abs_laplacian.non_zero_values(), 95)
  print '\tscaling abs image by 255 / cutoff abs'
  scaled = (255 / cutoff_abs) * abs_laplacian
  print '\tinverting scaled image'
  inverted = invert(scaled, 255)
  print '\tcomputing variance'
  var = var_signal(blurred, 2)
  print '\tfinding cutoff variance'
  cutoff_var = scoreatpercentile(var.non_zero_values(), 60)
  print '\tupdating result image with cutoff variance'
  for n1 in xrange(inverted.n1_min, inverted.n1_max + 1):
    for n2 in xrange(inverted.n2_min, inverted.n2_max + 1):
      if var[n1, n2] < cutoff_var:
        inverted.set_value(n1, n2, 255)
  print '\tsaving result image'
  new_image_path = join(strip_dir(image_path), '%s_laplacian_edges.%s' % tuple(
      strip_file_name(image_path).split('.')))
  two_D_signal_to_image(inverted, new_image_path)
  print '\tdone'
