from direction import MapPos, Dir

class Player:
    def __init__(self):
        self.pos = MapPos(-1, -1)
        self.facing = Dir.NORTH
