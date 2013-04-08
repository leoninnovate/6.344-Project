"""
Main.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from edge_detection_gradient import detect_edges_gradient
from edge_detection_laplacian import detect_edges_laplacian
from sys import argv

def show_help():
  """
  Displays help message.
  """
  print 'Enter "python main.py [option] [images]"'
  print ('Where [option] is one of "-g" (gradient based method) and "-l" '
      '(laplacian based method).')
  print '[images] is a space separated list of images to process.'

if __name__ == '__main__':
  if len(argv) > 2:
    if argv[1].lower() not in ('-g', '-l'):
      show_help()
    else:
      detect_edges = detect_edges_gradient if argv[1].lower() == '-g' else (
          detect_edges_laplacian)
      for image_file in argv[2:]:
        print 'Processing %s' % image_file
        try:
          detect_edges(image_file)
          print 'Success'
        except:
          print 'Failure'
        print
  else:
    show_help()
