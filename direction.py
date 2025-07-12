from enum import Enum

class Dir(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class MapPos:
    def __init__(self, x, y):
        self.__pos = (x, y)

    @property
    def x(self):
        return self.__pos[0]

    @property
    def y(self):
        return self.__pos[1]
    
    def __add__(self, other):
        return MapPos(self.__pos[0] + other.__pos[0], self.__pos[1] + other.__pos[1])
    
    def __sub__(self, other):
        return MapPos(self.__pos[0] - other.__pos[0], self.__pos[1] - other.__pos[1])

    def __lt__(self, other):
        return self.__pos[0] < other.__pos[0] and self.__pos[1] < other.__pos[1]

    def __le__(self, other):
        return self.__pos[0] <= other.__pos[0] and self.__pos[1] <= other.__pos[1]

    def __eq__(self, other):
        return self.__pos[0] == other.__pos[0] and self.__pos[1] == other.__pos[1]

    def __ne__(self, other):
        return self.__pos[0] != other.__pos[0] and self.__pos[1] != other.__pos[1]

    def __gt__(self, other):
        return self.__pos[0] > other.__pos[0] and self.__pos[1] > other.__pos[1]

    def __ge__(self, other):
        return self.__pos[0] >= other.__pos[0] and self.__pos[1] >= other.__pos[1]

    def move(self, dir):
        return self + DIR_VECTORS[dir]

    def in_bounds(self, limit):
        return self.__ge__(ZERO_POS) and self.__lt__(limit)

    def __copy__(self):
        return MapPos(self.__pos[0], self.__pos[1])

    def __deepcopy__(self, memo):
        return MapPos(self.__pos[0], self.__pos[1])

    def copy(self):
        return self.__copy__()

ZERO_POS = MapPos(0,0)

DIR_VECTORS = { Dir.NORTH: MapPos(0, -1), Dir.EAST: MapPos(1, 0), Dir.SOUTH: MapPos(0, 1), Dir.WEST: MapPos(-1,0) }

DIR_REVERSE = { Dir.NORTH: Dir.SOUTH, Dir.EAST: Dir.WEST, Dir.SOUTH: Dir.NORTH, Dir.WEST: Dir.EAST }

DIR_CLOCK = { Dir.NORTH: Dir.EAST, Dir.EAST: Dir.SOUTH, Dir.SOUTH: Dir.WEST, Dir.WEST: Dir.NORTH }

DIR_COUNTER = { Dir.NORTH: Dir.WEST, Dir.EAST: Dir.NORTH, Dir.SOUTH: Dir.EAST, Dir.WEST: Dir.SOUTH }

#DIR_TURNS = {Turn.COUNTER: DIR_COUNTER, Turn.CLOCK: DIR_CLOCK}

def dist_width(dist):
    return ((dist + 1) * 2) + 1

def dist_half_width(dist):
    return dist + 2

def dist_width_range(dist):
    return -(dist + 1), dist + 1

def seeable(facing, face, offset):
    if facing == DIR_REVERSE(face):
        return True
    if offset < 0:
        if DIR_CLOCK[facing] == face:
            return True
    elif offset > 0:
        if DIR_COUNTER[facing] == face:
            return True
    return False

def vect_contained(vect, gridsize):
    return vect.x >= 0 and vect.y >= 0 and vect.x < gridsize.x and vect.y < gridsize.y

def get_line(start, facing, length, gridsize, skip_start = False):
    line = []
    pos = start.copy()
    if skip_start:
        pos = pos.move(facing)
        length -= 1
    for i in range(length):
        if not vect_contained(pos, gridsize):
            line.append(None)
        else:
            line.append(pos.copy())
        pos = pos.move(facing)
    return line
