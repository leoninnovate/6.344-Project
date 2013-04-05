"""
Script to convert between images and 2D signals.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from os.path import isfile
from PIL import Image
from two_D_signal import Two_D_Signal

def luminance(rgb):
  """
  Computes the limunance of the given color |rgb|, a tuple containing the red,
      blue, and green intensities of the color.
  Equation taken from "Two-Dimensional Signal and Image Processing", Jae Lim,
      (7.8a), p.422.
  """
  r, g, b = rgb
  return 0.299 * r + 0.587 * g + 0.114 * b

def image_to_two_D_signal(image_path):
  """
  Returns a Two_D_Signal representing the image stored at the given
      |image_path|.
  """
  assert isfile(image_path), 'invalid image_path'
  image = Image.open(image_path)
  image_pixels = image.load()
  width, height = image.size
  given_rgb = isinstance(image_pixels[0, 0], tuple)
  return Two_D_Signal({(n1, n2): luminance(image_pixels[n1, n2]) if given_rgb
      else image_pixels[n1, n2] for n1 in xrange(width) for n2 in xrange(
      height)})

def two_D_signal_to_image(signal, image_path):
  """
  Saves the given 2D |signal| as an image at the given |image_path|.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  image = Image.new('L', (signal.width, signal.height))
  image_pixels = image.load()
  for n1 in xrange(signal.width):
    for n2 in xrange(signal.height):
      image_pixels[n1, n2] = signal[signal.n1_min + n1, signal.n2_min + n2]
  image.save(image_path)
