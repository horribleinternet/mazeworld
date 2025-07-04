from constants import *
from pygame import Color, draw;

class Viewport:
    def __init__(self, default_color = Color(192, 192, 192)):
        self.default_color = default_color

    def draw(self, surface, forward_map):
        draw.lines(surface, self.default_color, True, [viewport_coord(0,0), viewport_coord(639, 0), viewport_coord(639, 479)])
        draw.line(surface, self.default_color, viewport_coord(80, 0),  viewport_coord(320, 240))
        draw.line(surface, self.default_color, viewport_coord(560, 0),  viewport_coord(320, 240))
        draw.line(surface, self.default_color, viewport_coord(80, 479),  viewport_coord(320, 240))
        draw.line(surface, self.default_color, viewport_coord(560, 479),  viewport_coord(320, 240))