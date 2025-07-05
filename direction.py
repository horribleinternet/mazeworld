from enum import Enum

class Dir(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

def reverse_dir(direction):
    return (direction + 2) % 4

def clock_dir(direction):
    return (direction + 1) % 4

def counter_dir(direction):
    if (direction > 0):
        return direction - 1
    else:
        return Dir.WEST

def seeable(facing, face, offset):
    if facing == reverse_dir(face):
        return True
    if offset < 0:
        if clock_dir(facing) == face:
            return True
    elif offset > 0:
        if counter_dir(facing) == face:
            return True
    return False
