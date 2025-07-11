from enum import Enum
from pygame import Vector2

class Dir(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Turn(Enum):
    COUNTER = 0
    LEFT = 0
    CLOCK = 1
    RIGHT = 1

DIR_VECTORS = { Dir.NORTH: Vector2(0, -1), Dir.EAST: Vector2(1, 0), Dir.SOUTH: Vector2(0, 1), Dir.WEST: Vector2(-1,0) }

DIR_REVERSE = { Dir.NORTH: Dir.SOUTH, Dir.EAST: Dir.WEST, Dir.SOUTH: Dir.NORTH, Dir.WEST: Dir.EAST }

DIR_CLOCK = { Dir.NORTH: Dir.EAST, Dir.EAST: Dir.SOUTH, Dir.SOUTH: Dir.WEST, Dir.WEST: Dir.NORTH }

DIR_COUNTER = { Dir.NORTH: Dir.WEST, Dir.EAST: Dir.NORTH, Dir.SOUTH: Dir.EAST, Dir.WEST: Dir.SOUTH }

DIR_TURNS = {Turn.COUNTER: DIR_COUNTER, Turn.CLOCK: DIR_CLOCK}

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
        pos += DIR_VECTORS[facing]
        length -= 1
    for i in range(length):
        if not vect_contained(pos, gridsize):
            line.append(None)
        else:
            line.append(pos.copy())
        pos += DIR_VECTORS[facing]
    return line