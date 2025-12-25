from constants import *
import pygame
import testmaps
import map
from viewport import Viewport
from view import View
from direction import Dir, MapPos
from player import Player
from controller import Controller
from world import World

def main():
    initialized = pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.
    view = View(screen, viewport_coord)
    viewport = Viewport(view)
    testmap = map.Map(testmaps.testmap1)
    player = Player()
    controller = Controller(player, testmap)
    world = World(testmap, controller, MapPos(1,3))
    world.tick(viewport)
    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    return
                case pygame.KEYDOWN:
                    controller.input(event)
                    world.tick(viewport)
        screen.fill(pygame.Color(0,0,0))
        dt = clock.tick(60) / 1000

def test():
    testmap = map.Map(testmaps.testmap1)
    map.printgrid(testmaps.testmap1)
    print("")
    map.printgrid(testmap.get_viewmap(MapPos(2,3), Dir.EAST, 4))

if __name__ == "__main__":
    main()
    test()
