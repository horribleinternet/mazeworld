from direction import Dir
from view import View

class Visual:
    def __init__(self):
        self.opaque = False

    def draw(self, view, face, distance, offset):
        pass

class WallVisual(Visual):
    def __init__(self):
        self.opaque = True

class VoidVisual(Visual):
    def __init__(self):
        self.opaque = False
