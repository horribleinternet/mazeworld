from direction import seeable
from visual import WallVisual, VoidVisual

def get_default_block():
    return Block(True)

class Block:
    def __init__(self, solid=True, visual = WallVisual(), faceobjs = None, centerobjs = None):
        self.solid = solid
        self.visual = visual
        self.faceobjs = faceobjs
        self.centerobjs = centerobjs

    def set_solid(self, s = True):
        self.solid = s
    
    def draw(self, surface, facing, distance, offset):
        if self.visual is not None:
            self.visual.draw(surface, facing, distance, offset)
        if not self.is_opaque():
            for obj in self.centerobjs:
                if obj is not None:
                    obj.visual.draw(surface, facing, distance, offset)
        for dir, obj in self.faceobjs.items():
            if seeable(facing, dir, offset):
                obj.visual.draw(surface, facing, distance, offset)

    def is_opaque(self):
        return self.visual is not None and self.visual.opaque

class VoidBlock(Block):
    def __init__(self):
        super().__init__(False, VoidVisual())
