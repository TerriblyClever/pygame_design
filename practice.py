import pygame

pygame.init()

game_window_x = 500
game_window_y = 500
game_window = pygame.display.set_mode((game_window_x, game_window_y))
pygame.display.set_caption("Change This Title Later")

x_center = game_window_x/2
y_center = game_window_x/2
height = 40
width = 60
velocity = 5
game_delay = 15

is_jump = False
jump_count = 10

run = True

while run:
    pygame.time.delay(game_delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_center > velocity:
        x_center -= velocity

    if keys[pygame.K_RIGHT] and x_center < (game_window_x - width - velocity):
        x_center  += velocity

    if not is_jump:
        if keys[pygame.K_UP] and y_center > velocity:
            y_center -= velocity

        if keys[pygame.K_DOWN] and y_center < (game_window_y - height - velocity):
            y_center  += velocity

        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            y_center -= (jump_count ** 2) * 0.5 * neg #multiplier to slow down the jump
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
        
    game_window.fill((0,0,0))
    pygame.draw.rect(game_window, (255, 0, 0), (x_center, y_center, width, height))
    pygame.display.update()
    
pygame.quit()