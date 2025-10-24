from constants import *
from view import View
from pygame import Color, draw;
from map import printgrid
import numpy as np

class Viewport:
    def __init__(self, view):
        self.view = view
        screen = np.array([VIEWPORT_WIDTH / 2, 0, 0, VIEWPORT_WIDTH / 2],
                               [0, -VIEWPORT_HEIGHT / 2, 0, VIEWPORT_HEIGHT / 2],
                               [0,0,1,0],
                               [0,0,0,1])
        model = np.array([1,0,0,-3],
                              [0,1,0,0],
                              [0,0,1,3.5],
                              [0,0,0,1])
        proj = np.array([1,0,0,0],
                             [0,4/3,0,0],
                             [0,0,-5.1/4.9,-1/4.9],
                             [0,0,-1,0])
        mat = np.matmult(model, proj)
        self.composed = np.matmult(mat, screen)

    def draw(self, forward_map):
        v = self.view
        printgrid(forward_map)
