from direction import Dir
from view import View
import numpy as np
from models import cube

class Visual:
    def __init__(self):
        self.opaque = False

    def draw(self, view, face, distance, offset):
        pass

class WallVisual(Visual):
    _block = cube.copy()

    def __init__(self):
        self.opaque = True

    def draw(self, view, face, distance, offset):
        pass

class VoidVisual(Visual):
    def __init__(self):
        self.opaque = False

