from functools import reduce
from block import get_default_block, Block
from pygame import Vector2
from direction import get_line, DIR_CLOCK, DIR_COUNTER, dist_width, dist_half_width

class Map:
    def __init__(self, listgrid):
        self.listgrid = listgrid
        self.fill_in_map(listgrid)
        self.enclose_map(listgrid)
        self.size = Vector2(len(listgrid[0]), len(listgrid))

    def get_block(self, vect):
        return self.listgrid[vect.y][vect.x]

    def get_viewmap(self, location, facing, distance = 3):
        viewmap = []
        viewline = get_line(location, facing, distance, self.size)
        #need to iterate in reversed order, but also track distance from start
        for i in range(len(viewline)-1, -1, -1):
            viewmap_row = []
            if viewline[i] is None:
                viewmap_row = [None for x in range(dist_width(i))]
            else:
                leftside = get_line(viewline[i], DIR_COUNTER[facing], dist_half_width(i), self.size, True)
                rightside = get_line(viewline[i], DIR_CLOCK[facing], dist_half_width(i), self.size)
                for place in reversed(leftside):
                    if place is None:
                        viewmap_row.append(None)
                    else:
                        viewmap_row.append(self.get_block(place))
                for place in rightside:
                    if place is None:
                        viewmap_row.append(None)
                    else:
                        viewmap_row.append(self.get_block(place))
            viewmap.append(viewmap_row)
        return viewmap


    def fill_in_map(self, grid):
       max_width = reduce(max, map(len, grid))
       for row in grid:
           row.extend([get_default_block() for x in range(max_width-len(row))])

    def enclose_map(self, grid):
        for block in grid[0]:
            block.solid = True
        for block in grid[-1]:
            block.solid = True
        for row in grid[1:-1]:
            row[0].solid = True
            row[-1].solid = True

