from functools import reduce
from block import get_default_block, Block

class Map:
    def __init__(self, listgrid):
        self.listgrid = listgrid
        self.fill_in_map(listgrid)
        self.enclose_map(listgrid)
        self.height = len(listgrid)
        self.width = len(listgrid[0])

    def get_viewmap(self, location, facing, distance = 3):
        pass

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
