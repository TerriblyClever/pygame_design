import pygame

game_window_x = 500
game_window_y = 500
game_window = pygame.display.set_mode((game_window_x, game_window_y))

class bullet(object):
    """Class for creating multiple bullet instances."""

    def __init__(self, x, y, color, radius):
        self.x_coord = x
        self.y_coord = y
        self.color = color
        self.radius = radius
        self.velocity = 5
        self.bullet_right = True
        self.bullet_left = False

    def draw(self, game_window):
        pygame.draw.circle(game_window, self.color, (self.x_coord, self.y_coord), self.radius)



ball_x = 250
ball_y = 250
ball_radius = 10
ball_velocity = 5

ball_right = True
ball_left = False

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    game_window.fill((255,255,255))

    if ball_x >= 490:
        ball_right = False
        ball_left = True
    elif ball_x <= 10: 
        ball_right = True 
        ball_left = False 

    if ball_x < game_window_x - ball_radius and ball_right:
        #requires 4 arguments: the surface, a color RGB tuple, (x,y) coordinates, and a radius
        pygame.draw.circle(game_window, (0,0,0), (ball_x, ball_y), ball_radius)
        ball_x += ball_velocity
    elif ball_x > 0 and ball_left:
        pygame.draw.circle(game_window, (0,0,0), (ball_x, ball_y), ball_radius)
        ball_x -= ball_velocity

    pygame.display.update()

pygame.quit()