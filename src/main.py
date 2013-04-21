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
  print 'Enter "python main.py [method] [optional: -alpha <n>] [images ...]"'
  print '[method] is either "-g" (gradient based) or "-l" (laplacian based)'
  print '[images ...] is a space separated list of images to process'
  print '[-alpha <n>], optional, lets you choose the scaling alpha value'

if __name__ == '__main__':
  if len(argv) > 2:
    if argv[1].lower() not in ('-g', '-l'):
      show_help()
    else:
      detect_edges = detect_edges_gradient if argv[1].lower() == '-g' else (
          detect_edges_laplacian)
      alpha_given = argv[2].lower() == '-alpha'
      alpha = 1 # default
      if alpha_given:
        try:
          alpha = float(argv[3])
        except:
          print 'alpha value must be a floating point number, using default 1'
      for image_file in argv[(4 if alpha_given else 2):]:
        print 'Processing %s' % image_file
        try:
          detect_edges(image_file, alpha)
          print 'Success'
        except Exception as e:
          print 'Failure: %s' % e
        print
  else:
    show_help()
