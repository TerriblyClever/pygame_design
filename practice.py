import pygame, random
from pygame.constants import JOYAXISMOTION, JOYBUTTONDOWN, JOYHATMOTION

pygame.init()
pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick)

game_window_x = 750 
game_window_y = 750
game_window = pygame.display.set_mode((game_window_x, game_window_y))
pygame.display.set_caption("Change This Title Later")

clock = pygame.time.Clock()

x_center = game_window_x/2
y_center = game_window_y - 100
height = 64 #variables for the height of a rectangle sprite
width = 64 #width of the rectangle sprite
velocity = 10 #the number of pixels to move by each game loop
game_delay = 27 #equates to a frame rate per second for now

color_floor = 50
red_value, green_value, blue_value = color_floor, color_floor, color_floor
red_loop, green_loop, blue_loop = True, False, False
color_increment = 5

is_jump = False #Boolean to detect whether the sprite is in a jump
moving_right = False
moving_left = False 
moving_up = False
moving_down = False
jump_count = 5 #controls the height of your jump 
jump_increment = 5

def redraw_game_window(): #created a function to update the game window
    #code commented out that was used to animate the red rectangle
    game_window.fill((0,0,0)) #redraw black where the rectangle used to be
    #draw.rect takes 3 arguments: where to draw the rect, rgb colors to draw, a 4-tuple of x-loc,y-loc,width,height
    if x_center > 0 and x_center < game_window_x - width:
        pygame.draw.rect(game_window, (red_value, green_value, blue_value), (x_center, y_center, width, height))
    pygame.display.update()

#MAIN GAME LOOP
run = True
while run:
    clock.tick(game_delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == JOYBUTTONDOWN and event.button == 1:
            is_jump = True
        if event.type == JOYBUTTONDOWN and event.button == 5:
            jump_increment += 2
            print("Jump Height", jump_increment)
            jump_count = jump_increment
        elif event.type == JOYBUTTONDOWN and event.button == 4:
            jump_increment -= 2
            print("Jump Height", jump_increment)
            jump_count = jump_increment
        if event.type == JOYAXISMOTION:
            if event.axis == 0:
                if event.value < -0.1:
                    moving_left = True
                    moving_right = False 
                elif event.value > 0.1:
                    moving_right = True
                    moving_left = False
                else:
                    moving_right = False
                    moving_left = False
            if event.axis == 1:
                print(event.value)
                if event.value > 0.1:
                    moving_down = True
                    moving_up = False 
                elif event.value < -0.1:
                    moving_up = True
                    moving_down = False
                else:
                    moving_up = False
                    moving_down = False
        if event.type == JOYHATMOTION and event.value == (1,0):
            velocity += 5
            print("Velocity", velocity)
        elif event.type == JOYHATMOTION and event.value == (-1, 0):
            velocity -= 5
            print("Velocity", velocity)

    keys = pygame.key.get_pressed()

    if red_loop:
        if red_value >= 250:
            red_loop = False
            green_loop = True
        red_value += color_increment 
    elif green_loop:
        if green_value >= 250:
            green_loop = False
            blue_loop = True
        elif red_value >= color_floor:
            red_value -= color_increment 
        else:
            green_value += color_increment
    elif blue_loop:
        if blue_value >= 250:
            blue_loop = False
        elif green_value >= color_floor:
            green_value -= color_increment 
        else:
            blue_value += color_increment
    elif blue_value >= color_floor:
        blue_value -= color_increment
    else:
        red_value, green_value, blue_value = color_floor, color_floor, color_floor
        red_loop, green_loop, blue_loop = True, False, False

    if x_center <= 0:
        x_center = 5
    elif x_center > (game_window_x - width - 5):
        x_center = (game_window_x - width - 5)
    if moving_left and x_center > 5:
        x_center -= velocity
    if moving_right and x_center < (game_window_x - width - 5):
        x_center += velocity

    if y_center <= 0:
        y_center = 5
    elif y_center > (game_window_y - height - 5):
        y_center = (game_window_y - height - 5)
    if moving_up and y_center > 5:
        y_center -= velocity
    if moving_down and y_center < (game_window_y - height - 5):
        y_center += velocity
    

    if is_jump: #will run when is_jump = False
        if jump_count >= -jump_increment:
            neg = 1
            if jump_count < 0:
                neg = -1
            y_center -= (jump_count ** 2) * neg 
            jump_count -= 1
        else:
            is_jump = False #setting the jump condition back to No
            jump_count = jump_increment #reset jump count for another jump
    
    redraw_game_window()

pygame.quit()