import pygame

pygame.init()

GAME_WINDOW_X = 500
GAME_WINDOW_CENTER = GAME_WINDOW_X/2
GAME_WINDOW_Y = 480
GAME_WINDOW_BOTTOM = GAME_WINDOW_Y - 64
GAME_WINDOW = pygame.display.set_mode((GAME_WINDOW_X, GAME_WINDOW_Y))
GAME_DELAY = 27
pygame.display.set_caption("Change This Title Later")

walk_right = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'),
pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'),
pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'),
pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'),
pygame.image.load('images/R9.png')]

walk_left = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'),
pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'),
pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'),
pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'),
pygame.image.load('images/L9.png')]
background = pygame.image.load('images/bg.jpg')
character = pygame.image.load('images/standing.png')

clock = pygame.time.Clock()

class Player(object):
    """Player sprite class."""
    def __init__(self, x, y, width, height):
        self.x_coord = x
        self.y_coord = y
        self.height = height
        self.width = width
        self.velocity = 5
        self.is_jump = False
        self.jump_count = 7
        self.right = False
        self.left = False
        self.walk_count = 0

    def draw(self, game_window):
        """Player class method for re-drawing the sprite on the game_window surface."""
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        if self.left:
            game_window.blit(walk_left[self.walk_count//3], (self.x_coord, self.y_coord))
            self.walk_count += 1
        elif self.right:
            game_window.blit(walk_right[self.walk_count//3], (self.x_coord, self.y_coord))
            self.walk_count += 1
        else:
            game_window.blit(character, (self.x_coord, self.y_coord))
            self.walk_count += 1

def redraw_game_window():
    """Primary method to redraw the game window at the end of each Main Loop iteration."""
    GAME_WINDOW.blit(background, (0,0))
    sprite_1.draw(GAME_WINDOW)
    pygame.display.update()

sprite_1 = Player(GAME_WINDOW_CENTER, GAME_WINDOW_BOTTOM, 64, 64)

#MAIN GAME LOOP
def main_game_loop():
    """Runs the main game loop, looking for input from the user."""
    run = True
    while run:
        #pygame.time.delay(game_delay)
        clock.tick(GAME_DELAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and sprite_1.x_coord > sprite_1.velocity:
            sprite_1.x_coord -= sprite_1.velocity
            sprite_1.right = False
            sprite_1.left = True
        elif keys[pygame.K_RIGHT] and sprite_1.x_coord < (GAME_WINDOW_X - sprite_1.width - sprite_1.velocity):
            sprite_1.x_coord += sprite_1.velocity
            sprite_1.right = True
            sprite_1.left = False
        else:
            sprite_1.right = False
            sprite_1.left = False
            sprite_1.walk_count = 0

        if not sprite_1.is_jump:
            if keys[pygame.K_SPACE]:
                sprite_1.is_jump = True
                sprite_1.right = False
                sprite_1.left = False
                sprite_1.walk_count = 0
        else:
            if sprite_1.jump_count >= -7:
                neg = 1
                if sprite_1.jump_count < 0:
                    neg = -1
                sprite_1.y_coord -= (sprite_1.jump_count ** 2) * neg
                sprite_1.jump_count -= 1
            else:
                sprite_1.is_jump = False
                sprite_1.jump_count = 7
        redraw_game_window()
    pygame.quit()

if __name__ == '__main__':
    main_game_loop()
