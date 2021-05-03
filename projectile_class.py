import pygame, random
from game_variables import *

class Projectile(object):
    """Class for drawing projctiles that will originate at a particular character."""
    def __init__(self, x, y, radius, color, facing):
        self.x_coord = x
        self.y_coord = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self, game_window):
        """Method for creating an instance of a projectile."""
        pygame.draw.circle(game_window, self.color, (self.x_coord, self.y_coord), self.radius)