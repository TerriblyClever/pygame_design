import pygame

pygame.init()

game_window_x = 500
game_window_center = game_window_x/2
game_window_y = 500
game_window_bottom = game_window_y - 10
game_window = pygame.display.set_mode((game_window_x, game_window_y))
pygame.display.set_caption("Change This Title Later")

walk_right = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
walk_left = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
background = pygame.image.load('images/bg.jpg')
character = pygame.image.load('images/standing.png')

clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.velocity = 5
        self.is_jump = False
        self.jump_count = 5
        self.right = False
        self.left = False
        self.walk_count = 0

    def draw(self, game_window):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if self.left:
            game_window.blit(walk_left[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        elif self.right:
            game_window.blit(walk_right[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        else:
            game_window.blit(character, (self.x, self.y))
            self.walk_count += 1


game_delay = 27

is_jump = False
jump_count = 5 

def redraw_game_window():
    game_window.blit(background, (0,0))
    sprite_1.draw(game_window)
    pygame.display.update()

    #code commented out that was used to animate the red rectangle
    #pygame.draw.rect(game_window, (255, 0, 0), (x, y, width, height))
    #pygame.display.update()


#MAIN GAME LOOP
sprite_1 = Player(game_window_center, game_window_bottom, 64, 64)
run = True
while run:
    #pygame.time.delay(game_delay)
    clock.tick(game_delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and sprite_1.x > sprite_1.velocity:
        sprite_1.x -= sprite_1.velocity
        sprite_1.right = False
        sprite_1.left = True
    elif keys[pygame.K_RIGHT] and sprite_1.x < (game_window_x - sprite_1.width - sprite_1.velocity):
        sprite_1.x += sprite_1.velocity
        sprite_1.right = True
        sprite_1.left = False
    else:
        sprite_1.right = False 
        sprite_1.left = False
        sprite_1.walk_count = 0

    if not sprite_1.is_jump:
#code has been commented out that would allow vertical movement of the character
#        if keys[pygame.K_UP] and y > velocity:
#            y -= velocity
#
#        if keys[pygame.K_DOWN] and y < (game_window_y - height - velocity):
#            y += velocity
#
        if keys[pygame.K_SPACE]:
            sprite_1.is_jump = True
            sprite_1.right = False 
            sprite_1.left = False
            sprite_1.walk_count = 0
    else:
        if sprite_1.jump_count >= -5:
            neg = 1
            if sprite_1.jump_count < 0:
                neg = -1
            sprite_1.y -= (sprite_1.jump_count ** 2) * neg 
            sprite_1.jump_count -= 1
        else:
            sprite_1.is_jump = False
            sprite_1.jump_count = 5 
    redraw_game_window()
pygame.quit()
