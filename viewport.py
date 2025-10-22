from constants import *
from view import View
from pygame import Color, draw;
from map import printgrid
import numpy as np

class Viewport:
    def __init__(self, view):
        self.view = view

    def draw(self, forward_map):
        v = self.view
        printgrid(forward_map)
