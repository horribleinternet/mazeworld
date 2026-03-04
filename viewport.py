from constants import *
from view import View
from pygame import Color, draw;
from map import printgrid
import numpy as np
from models import cube

class Viewport:
    def __init__(self, view):
        self.view = view
        self.screen = [
                [VIEWPORT_WIDTH / 2, 0, 0, VIEWPORT_WIDTH / 2],
                [0, -VIEWPORT_HEIGHT / 2, 0, VIEWPORT_HEIGHT / 2],
                [0,0,1,0],
                [0,0,0,1]]
        model = np.array([
                [1,0,0,-3],
                [0,1,0,0],
                [0,0,1,3.5],
                [0,0,0,1]])
        proj = np.array([
                [1,0,0,0],
                [0,4/3,0,0],
                [0,0,-5.1/4.9,-1/4.9],
                [0,0,-1,0]])
        viewmat = np.eye(4)
        self.composed = proj @ viewmat


    def draw(self, forward_map, facing):
        test_cube = cube.copy()
        if test_cube.ndim == 1:
            test_cube.reshape(1, -1)
        cube_shape = test_cube.shape[0]
        points = np.hstack([test_cube, np.ones((cube_shape, 1))])
        v = self.view
        p1mat = [[-3.5],[-0.5],[3],[1]]
        p2mat = [[-3.5],[0.5],[3],[1]]
        p1c = np.matmul(self.composed, p1mat)
        p2c = np.matmul(self.composed, p2mat)
        p1  = np.matmul(self.screen, p1c)
        p2  = np.matmul(self.screen, p2c)
        #print(p1, "\n", p2)
        printgrid(forward_map)

