import pygame

pygame.init()

game_window_x = 500
game_window_y = 500
game_window = pygame.display.set_mode((game_window_x, game_window_y))
pygame.display.set_caption("Change This Title Later")

clock = pygame.time.Clock()

x_center = game_window_x/2
y_center = game_window_y - 100
height = 64 #variables for the height of a rectangle sprite
width = 64 #width of the rectangle sprite
velocity = 5 #the number of pixels to move by each game loop
game_delay = 27 #equates to a frame rate per second for now

is_jump = False #Boolean to detect whether the sprite is in a jump
jump_count = 5 #controls the height of your jump 

def redraw_game_window(): #created a function to update the game window
    #code commented out that was used to animate the red rectangle
    game_window.fill((0,0,0)) #redraw black where the rectangle used to be
    #draw.rect takes 3 arguments: where to draw the rect, rgb colors to draw, a 4-tuple of x-loc,y-loc,width,height
    pygame.draw.rect(game_window, (153, 0, 0), (x_center, y_center, width, height))
    pygame.display.update()

#MAIN GAME LOOP
run = True
while run:
    clock.tick(game_delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x_center -= velocity
    if keys[pygame.K_RIGHT]:
        x_center += velocity
    if not is_jump: #will run when is_jump = False
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -5:
            neg = 1
            if jump_count < 0:
                neg = -1
            y_center -= (jump_count ** 2) * neg 
            jump_count -= 1
        else:
            is_jump = False #setting the jump condition back to No
            jump_count = 5 #reset jump count for another jump
    
    redraw_game_window()
    
pygame.quit()