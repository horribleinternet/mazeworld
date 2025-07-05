from constants import *
from pygame import Color, draw;

class Viewport:
    def __init__(self, default_color = Color(192, 192, 192), default_width = 3):
        self.default_color = default_color
        self.default_width = default_width

    def draw(self, surface, forward_map):
        draw.line(surface, self.default_color, viewport_coord(1., 0.), viewport_coord(1., 0.75), self.default_width)
        draw.line(surface, self.default_color, viewport_coord(0.125, 0.0),  viewport_coord(0.5, 0.375), self.default_width)
        draw.line(surface, self.default_color, viewport_coord(0.875, 0),  viewport_coord(0.5, 0.375), self.default_width)
        draw.line(surface, self.default_color, viewport_coord(0.125, 0.75),  viewport_coord(0.5, 0.375), self.default_width)
        draw.line(surface, self.default_color, viewport_coord(0.875, 0.75),  viewport_coord(0.5, 0.375), self.default_width)
