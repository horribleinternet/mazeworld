from constants import *
from view import View
from pygame import Color, draw;
from map import printgrid
import numpy as np

class Viewport:
    def __init__(self, view):
        self.view = view
        self.screen = [[VIEWPORT_WIDTH / 2, 0, 0, VIEWPORT_WIDTH / 2],
                 [0, -VIEWPORT_HEIGHT / 2, 0, VIEWPORT_HEIGHT / 2],
                 [0,0,1,0],
                 [0,0,0,1]]
        model = [[1,0,0,-3],
                [0,1,0,0],
                [0,0,1,3.5],
                [0,0,0,1]]
        proj = [[1,0,0,0],
               [0,4/3,0,0],
               [0,0,-5.1/4.9,-1/4.9],
               [0,0,-1,0]]
        self.composed = np.matmul(proj, model)


    def draw(self, forward_map):
        v = self.view
        p1mat = [[-3.5],[-0.5],[3],[1]]
        p2mat = [[-3.5],[0.5],[3],[1]]
        p1c = np.matmul(self.composed, p1mat)
        p2c = np.matmul(self.composed, p2mat)
        p1  = np.matmul(self.screen, p1c)
        p2  = np.matmul(self.screen, p2c)
        print(p1, "\n", p2)
        printgrid(forward_map)

