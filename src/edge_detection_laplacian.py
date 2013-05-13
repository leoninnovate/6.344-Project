"""
Edge detection using the laplacian method.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from constants import LAPLACIAN_FILTER
from image_two_D_signal_conversion import image_to_two_D_signal
from image_two_D_signal_conversion import two_D_signal_to_image
from os.path import join
from scipy.stats import scoreatpercentile
from two_D_signal import Two_D_Signal
from two_D_signal_stats import var_signal
from two_D_convolution import clipped_fft_convolve
from util import invert
from util import scaler
from util import strip_dir
from util import strip_file_name

def detect_edges_laplacian(image_path, alpha, variance_filter=True):
  """
  Saves a new image that presents the edges in the image saved at the given
      |image_path|. This method uses the Laplacian based method for edge
      detection. |alpha|, a number greater than 0, is a parameter to
      determine which pixels to consider edges. The higher the value of |alpha|
      the higher the laplacian has to be to for a pixel to be selected. If
      |variance_filter| is set, only pixels with high variance have a chance at
      all of being selected as edges.
  """
  print '\tcomputing 2D signal from image path'
  signal = image_to_two_D_signal(image_path)
  print '\tcomputing laplacian'
  laplacian = clipped_fft_convolve(signal, LAPLACIAN_FILTER)
  print '\tcomputing abs'
  abs_laplacian = abs(laplacian)
  print '\tfinding cutoff abs: 95th percentile abs'
  cutoff_abs = scoreatpercentile(abs_laplacian.non_zero_values(), 95)
  print '\tscaling abs image with alpha=%s' % alpha
  scale_f = scaler(cutoff_abs, 255, alpha)
  scaled = Two_D_Signal({key: scale_f(abs_laplacian[key]) for key in
      abs_laplacian.values})
  print '\tinverting scaled image'
  inverted = invert(scaled, 255)
  if variance_filter:
    print '\tcomputing variance'
    var = var_signal(signal, 2)
    print '\tfinding cutoff variance'
    cutoff_var = scoreatpercentile(var.non_zero_values(), 70)
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
  return new_image_path
