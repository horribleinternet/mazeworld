from constants import *
from view import View
from pygame import Color, draw;
from map import printgrid

class Viewport:
    def __init__(self, view):
        self.view = view

    def draw(self, forward_map):
        v = self.view
        draw.line(v.surface, v.default_color, v.coordfunc(0., 0.), v.coordfunc(1., 0.), v.default_width)
        draw.line(v.surface, v.default_color, v.coordfunc(0., 0.), v.coordfunc(0., 0.75), v.default_width)
        draw.line(v.surface, v.default_color, v.coordfunc(0., 0.75), v.coordfunc(1., 0.75), v.default_width)
        draw.line(v.surface, v.default_color, v.coordfunc(1., 0.), v.coordfunc(1., 0.75), v.default_width)
        draw.line(v.surface, v.default_color, v.coordfunc(0.125, 0.),  v.coordfunc(0.5, 0.375), v.default_width)
        draw.line(v.surface, v.default_color, v.coordfunc(0.875, 0.),  v.coordfunc(0.5, 0.375), v.default_width)
        draw.line(v.surface, v.default_color, v.coordfunc(0.125, 0.75),  v.coordfunc(0.5, 0.375), v.default_width)
        draw.line(v.surface, v.default_color, v.coordfunc(0.875, 0.75),  v.coordfunc(0.5, 0.375), v.default_width)
        printgrid(forward_map)
