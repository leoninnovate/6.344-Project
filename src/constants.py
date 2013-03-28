"""
Constants.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from two_D_signal import Two_D_Signal

HORIZONTAL_EDGE_FILTER = Two_D_Signal({(-1, -1): 1, (-1, 0): 1, (-1, 1): 1,
    (1, -1): 1, (1, 0): 1, (1, 1): 1})
