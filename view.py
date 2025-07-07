from pygame import Color

class View:
    def __init__(self, surface, coordfunc, default_color = Color(192, 192, 192), default_width = 5):
        self.surface = surface
        self.coordfunc = coordfunc
        self.default_color = default_color
        self.default_width = default_width
        print(self.default_color)