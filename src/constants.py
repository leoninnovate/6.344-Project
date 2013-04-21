"""
Constants.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from two_D_signal import Two_D_Signal

# filters for gradient based method
HORIZONTAL_EDGE_FILTER = Two_D_Signal({(-1, -1): -1, (0, -1): -2, (1, -1): -1,
    (-1, 1): 1, (0, 1): 2, (1, 1): 1})
VERTICAL_EDGE_FILTER = Two_D_Signal({(-1, -1): -1, (-1, 0): -2, (-1, 1): -1,
    (1, -1): 1, (1, 0): 2, (1, 1): 1})

# filters for laplacian based method
LAPLACIAN_FILTER = Two_D_Signal({(0, 0): -8, (0, 1): 1, (0, -1): 1, (1, 0): 1,
    (-1, 0): 1, (-1, -1): 1, (-1, 1): 1, (1, -1): 1, (1, 1): 1})
