"""
Script to convert between images and 2D signals.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from PIL import Image
from two_D_signal import Two_D_Signal

def image_to_two_D_signal(image_path):
  """
  Returns a Two_D_Signal representing the image stored at the given
      |image_path|.
  """
  image = Image.open(image_path)
  image_pixels = image.load()
  width, height = image.size
  return Two_D_Signal({(n1, n2): image_pixels[n1, n2] for n1 in xrange(width)
      for n2 in xrange(height)})

def two_D_signal_to_image(signal, image_path):
  """
  Saves the given 2D |signal| as an image at the given |image_path|.
  """
  assert isinstance(signal, Two_D_Signal), 'signal must be a Two_D_Signal'
  width = signal.n1_max - signal.n1_min + 1
  height = signal.n2_max - signal.n2_min + 1
  image = Image.new('L', (width, height))
  image_pixels = image.load()
  for n1 in xrange(width):
    for n2 in xrange(height):
      image_pixels[n1, n2] = signal.value(signal.n1_min + n1, signal.n2_min +
          n2)
  image.save(image_path)
