"""
Constants.
"""

__author__ = 'mikemeko@mit.edu (Michael Mekonnen)'

from numpy import array
from two_D_signal import Two_D_Signal

# filters for gradient based method
HORIZONTAL_EDGE_FILTER = Two_D_Signal({(-1, -1): -1, (0, -1): -2, (1, -1): -1,
    (-1, 1): 1, (0, 1): 2, (1, 1): 1})
VERTICAL_EDGE_FILTER = Two_D_Signal({(-1, -1): -1, (-1, 0): -2, (-1, 1): -1,
    (1, -1): 1, (1, 0): 2, (1, 1): 1})

# filters for laplacian based method
LAPLACIAN_FILTER = Two_D_Signal({(0, 0): -8, (0, 1): 1, (0, -1): 1, (1, 0): 1,
    (-1, 0): 1, (-1, -1): 1, (-1, 1): 1, (1, -1): 1, (1, 1): 1})

# gaussian blurring filter
GAUSSIAN_FILTER = Two_D_Signal.from_two_D_array(array([
    [1, 4, 7, 4, 1],
    [4, 16, 26, 16, 4],
    [7, 26, 41, 26, 7],
    [4, 16, 26, 16, 4],
    [1, 4, 7, 4, 1]]) / 273., -2, -2)
