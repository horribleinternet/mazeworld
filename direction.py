from enum import Enum
from pygame import Vector2

class Dir(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

DIR_VECTORS = { Dir.NORTH: (0, -1), Dir.EAST: (1, 0), Dir.SOUTH: (0, 1), Dir.WEST: (-1,0) }

DIR_REVERSE = { Dir.NORTH: Dir.SOUTH, Dir.EAST: Dir.WEST, Dir.SOUTH: Dir.NORTH, Dir.WEST: Dir.EAST }

DIR_CLOCK = { Dir.NORTH: Dir.EAST, Dir.EAST: Dir.SOUTH, Dir.SOUTH: Dir.WEST, Dir.WEST: Dir.NORTH }

DIR_COUNTER = { Dir.NORTH: Dir.WEST, Dir.EAST: Dir.NORTH, Dir.SOUTH: Dir.EAST, Dir.WEST: Dir.SOUTH }

def dist_half_width(dist):
    return dist + 1

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
