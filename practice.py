import pygame

pygame.init()

game_window_x = 500
game_window_y = 500
game_window = pygame.display.set_mode((game_window_x, game_window_y))
pygame.display.set_caption("Change This Title Later")

walk_right = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walk_left = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
background = pygame.image.load('images/bg.jpg')
character = pygame.image.load('images/standing.png')

clock = pygame.time.Clock()

x_center = game_window_x/2
#y_center = game_window_y/2
y_center = game_window_y - 100
height = 64 
width = 64 
velocity = 5
game_delay = 27
left = False
right = False
walk_count = 0

is_jump = False
jump_count = 5 

def redraw_game_window():
    global walk_count 
    game_window.blit(background, (0,0))
    if walk_count + 1 > 27:
        walk_count = 0
    if left:
        game_window.blit(walk_left[walk_count//3], (x_center, y_center))
        walk_count += 1
    elif right:
        game_window.blit(walk_right[walk_count//3], (x_center, y_center))
        walk_count += 1
    else:
        game_window.blit(character, (x_center, y_center))
        walk_count += 1
        
    pygame.display.update()

    #code commented out that was used to animate the red rectangle
    #pygame.draw.rect(game_window, (255, 0, 0), (x_center, y_center, width, height))
    #pygame.display.update()

#MAIN GAME LOOP
run = True
while run:
    #pygame.time.delay(game_delay)
    clock.tick(game_delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_center > velocity:
        x_center -= velocity
        right = False
        left = True
    elif keys[pygame.K_RIGHT] and x_center < (game_window_x - width - velocity):
        x_center  += velocity
        right = True
        left = False
    else:
        right = False 
        left = False
        walk_count = 0

    if not is_jump:
#code has been commented out that would allow vertical movement of the character
#        if keys[pygame.K_UP] and y_center > velocity:
#            y_center -= velocity
#
#        if keys[pygame.K_DOWN] and y_center < (game_window_y - height - velocity):
#            y_center  += velocity
#
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False 
            left = False
            walk_count = 0
    else:
        if jump_count >= -5:
            neg = 1
            if jump_count < 0:
                neg = -1
            y_center -= (jump_count ** 2) * neg 
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 5 
    
    redraw_game_window()
        
    
pygame.quit()