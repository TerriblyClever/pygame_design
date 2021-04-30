import pygame

class Player(object):
    """Player sprite class."""
    #walk_right is a list of pygame images for the sprite walking to the right
    walk_right = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'),
    pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'),
    pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'),
    pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'),
    pygame.image.load('images/R9.png')]

    #walk_left is a list of pygame images for the sprite walking to the left
    walk_left = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'),
    pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'),
    pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'),
    pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'),
    pygame.image.load('images/L9.png')]

    def __init__(self, x, y, width, height):
        self.x_coord = x
        self.y_coord = y
        self.height = height
        self.width = width
        self.velocity = 5
        self.is_jump = False
        self.jump_count = 7
        self.right = False
        self.left = False
        self.walk_count = 0
        self.standing = True

    def draw(self, game_window):
        """Player class method for re-drawing the sprite on the game_window surface."""
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if not self.standing:
            if self.left:
                game_window.blit(self.walk_left[self.walk_count//3], (self.x_coord, self.y_coord))
                self.walk_count += 1
            elif self.right:
                game_window.blit(self.walk_right[self.walk_count//3], (self.x_coord, self.y_coord))
                self.walk_count += 1
        else:
            if self.right:
                game_window.blit(self.walk_right[0], (self.x_coord, self.y_coord))
            else:
                game_window.blit(self.walk_left[0], (self.x_coord, self.y_coord))