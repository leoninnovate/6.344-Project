"""
Main.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from edge_detection_gradient import detect_edges
from sys import argv

if __name__ == '__main__':
  image_files = argv[1:]
  if image_files:
    for image_file in image_files:
      print 'Processing %s' % image_file
      try:
        detect_edges(image_file)
        print 'Success'
      except:
        print 'Failure'
      print
  else:
    print 'No images provided to process'
