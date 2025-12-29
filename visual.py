from direction import Dir
from view import View
import numpy as np

class Visual:
    def __init__(self):
        self.opaque = False

    def draw(self, view, face, distance, offset):
        pass

class WallVisual(Visual):
    _block = np.array([
        [-0.5, -0.5, -0.5],
        [ 0.5, -0.5, -0.5],
        [ 0.5,  0.5, -0.5],
        [-0.5,  0.5, -0.5],
        [-0.5, -0.5,  0.5],
        [ 0.5, -0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [-0.5,  0.5,  0.5]
    ])
    def __init__(self):
        self.opaque = True

class VoidVisual(Visual):
    def __init__(self):
        self.opaque = False
