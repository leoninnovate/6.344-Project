"""
Image enhancement using edge detection.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from os.path import join
from PIL import Image
from util import strip_dir
from util import strip_file_name

def compose(image_pel, edge_map_val):
  """
  Returns a pixel value using an image pixel |image_pel| and edge pixel
      |edge_map_val| such that the edges in the image are more pronounced.
  """
  def _compose(image_val):
    return image_val + edge_map_val - 255
  if isinstance(image_pel, tuple):
    return tuple(map(_compose, image_pel))
  else:
    return _compose(image_pel)

def enhance_image(image_path, edge_map_path):
  """
  Saves a new image that pronounces the edges in the image at |image_path|
      using the edge map for the imave, as given at |edge_map_path|.
  """
  print '\tcreating enhanced image'
  image = Image.open(image_path)
  image_pixels = image.load()
  width, height = image.size
  edges = Image.open(edge_map_path)
  assert edges.size == (width, height), 'image and edge map do not match'
  edge_pixels = edges.load()
  output_image = Image.new(image.mode, (width, height))
  output_pixels = output_image.load()
  for n1 in xrange(width):
    for n2 in xrange(height):
      output_pixels[n1, n2] = compose(image_pixels[n1, n2],
          edge_pixels[n1, n2])
  enhanced_image_path = join(strip_dir(image_path), '%s_enhanced.%s' % tuple(
      strip_file_name(image_path).split('.')))
  output_image.save(enhanced_image_path)
