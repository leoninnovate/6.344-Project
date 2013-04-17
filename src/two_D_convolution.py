"""
Script to convolve 2D signals.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from scipy.signal import fftconvolve
from two_D_signal import Two_D_Signal
from util import clipped_signal
from util import padded_signal

def fft_convolve(f, g):
  """
  Returns a Two_D_Signal representing the convolution of the given
      Two_D_Signals |f| and |g|.
  """
  assert isinstance(f, Two_D_Signal), 'f must be a Two_D_Signal'
  assert isinstance(g, Two_D_Signal), 'g must be a Two_D_Signal'
  return Two_D_Signal.from_two_D_array(fftconvolve(f.to_two_D_array(max(0,
      g.n1_min - f.n1_min), max(0, g.n2_min - f.n2_min)), g.to_two_D_array(
      max(0, f.n1_min - g.n1_min), max(0, f.n2_min - g.n2_min))), f.n1_min,
      f.n2_min)

def clipped_fft_convolve(f, g):
  """
  Returns a Two_D_Signal representing the convolution of the given
      Two_D_Signal |f| and |g|, but the result will have the same extent as
      |f|. This is done by first padding |f|, convolving with |g|, and then
      clipping the result.
  """
  return clipped_signal(fft_convolve(padded_signal(f, g.n1_max - g.n1_min,
      g.n2_max - g.n2_min), g), f.n1_min - g.n1_min,
      f.n1_max + g.n1_max, f.n2_min - g.n2_min, f.n2_max + g.n2_max)
