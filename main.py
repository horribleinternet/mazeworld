from constants import *
import pygame
import testmaps
import map
from viewport import Viewport
from view import View
from direction import Dir, MapPos

def main():
    initialized = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.
    view = View(screen, viewport_coord)
    viewport = Viewport(view)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color(0,0,0))
        viewport.draw(None)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def test():
    map.printgrid(testmaps.testmap1)
    print("")
    testmap = map.Map(testmaps.testmap1)
    map.printgrid(testmap.get_viewmap(MapPos(2,3), Dir.EAST, 4))

if __name__ == "__main__":
    #main()
    test()
