import pygame
import direction
from pygame.event import Event

class Controller:
    def __init__(self, player, map):
        self.player = player
        self.map = map

    def input(self, event):
        match event.key:
            case pygame.K_w:
                self.move(direction.DIR_FORWARD)
            case pygame.K_s:
                self.move(direction.DIR_REVERSE)
            case pygame.K_a:
                self.turn(direction.DIR_COUNTER)
            case pygame.K_d:
                self.turn(direction.DIR_CLOCK)

    def turn(self, turns):
        self.player.facing = turns[self.player.facing]

    def move(self, sign):
        self.player.pos = self.map.move(self.player.pos, direction.DIR_VECTORS[sign[self.player.facing]])
