import pygame

pygame.init()

game_window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Change This Title Later")

x = 50
y = 50
height = 40
width = 60
velocity = 5
game_delay = 25

run = True

while run:
    pygame.time.delay(game_delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= velocity

    if keys[pygame.K_RIGHT]:
        x += velocity

    if keys[pygame.K_UP]:
        y -= velocity

    if keys[pygame.K_DOWN]:
        y += velocity
    
    game_window.fill((0,0,0))
    pygame.draw.rect(game_window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    
pygame.quit()