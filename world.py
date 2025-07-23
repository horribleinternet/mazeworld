import pygame

class World:
    def __init__(self, map, controller, start):
        self.map = map
        self.controller = controller
        self.controller.player.pos = start

    def tick(self, viewport):
        viewport.draw(self.map.get_viewmap(self.controller.player.pos, self.controller.player.facing))
        pygame.display.flip()
