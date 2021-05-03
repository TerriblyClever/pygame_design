import pygame, random
from game_variables import *

class Enemy(object):
    """Class for creating instances of enemy sprites."""
    walk_right = [pygame.image.load('images/R1E.png'), pygame.image.load('images/R2E.png'), 
    pygame.image.load('images/R3E.png'), pygame.image.load('images/R4E.png'), 
    pygame.image.load('images/R5E.png'), pygame.image.load('images/R6E.png'), 
    pygame.image.load('images/R7E.png'), pygame.image.load('images/R8E.png'), 
    pygame.image.load('images/R9E.png'), pygame.image.load('images/R10E.png'), 
    pygame.image.load('images/R11E.png')]

    walk_left= [pygame.image.load('images/L1E.png'), pygame.image.load('images/L2E.png'), 
    pygame.image.load('images/L3E.png'), pygame.image.load('images/L4E.png'), 
    pygame.image.load('images/L5E.png'), pygame.image.load('images/L6E.png'), 
    pygame.image.load('images/L7E.png'), pygame.image.load('images/L8E.png'), 
    pygame.image.load('images/L9E.png'), pygame.image.load('images/L10E.png'), 
    pygame.image.load('images/L11E.png')]

    def __init__(self, x, y, width, height, end, walk_count):
        self.x_coord = x
        self.y_coord = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [-32, GAME_WINDOW_X - 32]
        self.walk_count = walk_count
        self.velocity = random.randint(3, 6)
        self.hitbox = (self.x_coord + 20, self.y_coord, 28, 60)

    def draw(self, game_window):
        self.move()
        if self.walk_count + 1 >= 33:
            self.walk_count = 0

        if self.velocity > 0: #means the sprite is moving right
            #.blit() requires an image and then a set of x,y coordinates
            GAME_WINDOW.blit(self.walk_right[self.walk_count//3], (self.x_coord, self.y_coord))
            self.walk_count += 1
        else: #means the sprite is moving to the left
            GAME_WINDOW.blit(self.walk_left[self.walk_count//3], (self.x_coord, self.y_coord))
            self.walk_count += 1
        #redefining the dimensions of the hitbox based on the current location of the player sprite
        self.hitbox = (self.x_coord + 20, self.y_coord, 28, 60) 
        #draw the hitbox as a rectangle in the game window, around the player (WHHS Red)
        pygame.draw.rect(game_window, (153,0,0), self.hitbox, 2)
    
    def move(self):
        if self.velocity > 0: #indicates the character is moving to the right
            if self.x_coord + self.velocity < self.path[1]: #checks if character is past end coordinate
                self.x_coord += self.velocity
            else:
                self.velocity *= -1 #reverses the direction of travel
        else:
            if self.x_coord - self.velocity > self.path[0]: #checks if character past initial x coordinate
                self.x_coord += self.velocity
            else:
                self.velocity *= -1 #reverses the direction of travel

    def hit(self):
        print("Hit! You sunk my battleship...")