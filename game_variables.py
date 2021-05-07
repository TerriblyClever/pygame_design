import pygame

GAME_WINDOW_X = 500
GAME_WINDOW_CENTER = GAME_WINDOW_X/2
GAME_WINDOW_Y = 480
GAME_WINDOW_BOTTOM = GAME_WINDOW_Y - 64
GAME_WINDOW = pygame.display.set_mode((GAME_WINDOW_X, GAME_WINDOW_Y))
GAME_DELAY = 27

PROJECTILE_DIAMETER = 3

background = pygame.image.load('images/bg.jpg')

standing = pygame.image.load('images/standing.png')

shooting = False
score = 0
#print(pygame.font.get_fonts())