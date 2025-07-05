from direction import Dir

class Visual:
    def __init__(self, viewwidth, viewheight, coordfunc):
        self.viewwidth = viewwidth
        self.viewheight = viewheight
        self.coordfunc = coordfunc
        self.opaque = False

    def draw(surface, face, distance, offset):
        pass


class WallVisual(Visual):
    def __init__(self, viewwidth, viewheight, coordfunc):
        super().__init__(self, viewwidth, viewheight, coordfunc)
        self.opaque = True