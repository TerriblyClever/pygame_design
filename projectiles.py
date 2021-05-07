import pygame

game_window_x = 500
game_window_y = 500
game_window = pygame.display.set_mode((game_window_x, game_window_y))

bullet_y_coord_spawn = 400

class Bullet(object):
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

clock = pygame.time.Clock()

bullets_list = []

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    game_window.fill((255,255,255))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        bullets_list.append(Bullet(100, bullet_y_coord_spawn, (0,0,255), 10))
    if keys[pygame.K_UP]:
        bullet_y_coord_spawn -= item.velocity
    if keys[pygame.K_DOWN]:
        bullet_y_coord_spawn += item.velocity
    
    for item in bullets_list:
        item.x_coord += item.velocity
        item.draw(game_window)
        if item.x_coord > game_window_x:
            bullets_list.pop(bullets_list.index(item))

    pygame.display.update()

pygame.quit()