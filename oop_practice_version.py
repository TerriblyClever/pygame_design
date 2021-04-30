import pygame, random
from game_variables import *
from player_class import Player

pygame.init()

pygame.display.set_caption("Change This Title Later")

clock = pygame.time.Clock()

class Enemy(object):
    """Class for creating instances of enemy sprites."""
    walk_right = [pygame.image.load('images/R1E.png'), pygame.image.load('images/R2E.png'), 
    pygame.image.load('images/R3E.png'), pygame.image.load('images/R4E.png'), 
    pygame.image.load('images/R5E.png'), pygame.image.load('images/R6E.png'), 
    pygame.image.load('images/R7E.png'), pygame.image.load('images/R8E.png'), 
    pygame.image.load('images/R9E.png'), pygame.image.load('images/R10E.png'), 
    pygame.image.load('images/R11E.png')]

    walk_left= [pygame.image.load('images/L1E.png'), pygame.image.load('images/L2E.png'), 
    pygame.image.load('images/L3E.png'), pygame.image.load('images/L4E.png'), 
    pygame.image.load('images/L5E.png'), pygame.image.load('images/L6E.png'), 
    pygame.image.load('images/L7E.png'), pygame.image.load('images/L8E.png'), 
    pygame.image.load('images/L9E.png'), pygame.image.load('images/L10E.png'), 
    pygame.image.load('images/L11E.png')]

    def __init__(self, x, y, width, height, end, walk_count):
        self.x_coord = x
        self.y_coord = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [-32, GAME_WINDOW_X - 32]
        self.walk_count = walk_count
        self.velocity = random.randint(3, 6)

    def draw(self, GAME_WINDOW):
        self.move()
        if self.walk_count + 1 >= 33:
            self.walk_count = 0

        if self.velocity > 0: #means the sprite is moving right
            #.blit() requires an image and then a set of x,y coordinates
            GAME_WINDOW.blit(self.walk_right[self.walk_count//3], (self.x_coord, self.y_coord))
            self.walk_count += 1
        else: #means the sprite is moving to the left
            GAME_WINDOW.blit(self.walk_left[self.walk_count//3], (self.x_coord, self.y_coord))
            self.walk_count += 1
    
    def move(self):
        if self.velocity > 0: #indicates the character is moving to the right
            if self.x_coord + self.velocity < self.path[1]: #checks if character is past end coordinate
                self.x_coord += self.velocity
            else:
                self.velocity *= -1 #reverses the direction of travel
        else:
            if self.x_coord - self.velocity > self.path[0]: #checks if character past initial x coordinate
                self.x_coord += self.velocity
            else:
                self.velocity *= -1 #reverses the direction of travel

class Projectile(object):
    """Class for drawing projctiles that will originate at a particular character."""
    def __init__(self, x, y, radius, color, facing):
        self.x_coord = x
        self.y_coord = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing

    def draw(self, game_window):
        """Method for creating an instance of a projectile."""
        pygame.draw.circle(game_window, self.color, (self.x_coord, self.y_coord), self.radius)

def redraw_game_window():
    """Primary method to redraw the game window at the end of each Main Loop iteration."""
    GAME_WINDOW.blit(background, (0,0))
    hero.draw(GAME_WINDOW)
    goblin.draw(GAME_WINDOW)
    goblin2.draw(GAME_WINDOW)
    goblin3.draw(GAME_WINDOW)
    for bullet in bullets:
        bullet.draw(GAME_WINDOW)
    pygame.display.update()

#first instance of a player sprite, requires x,y coordinates and a width,height
hero = Player(GAME_WINDOW_CENTER, GAME_WINDOW_BOTTOM, 64, 64)

#first instance of an enemy sprite
goblin = Enemy(random.randint(32, GAME_WINDOW_X - 64), GAME_WINDOW_BOTTOM, 64, 64, GAME_WINDOW_X - 32, random.randint(0, 33))
goblin2 = Enemy(random.randint(32, GAME_WINDOW_X - 64), GAME_WINDOW_BOTTOM, 64, 64, GAME_WINDOW_X - 32, random.randint(0, 33))
goblin3 = Enemy(random.randint(32, GAME_WINDOW_X - 64), GAME_WINDOW_BOTTOM, 64, 64, GAME_WINDOW_X - 32, random.randint(0, 33))

bullets = [] #list for keeping track of all bullet sprites
#MAIN GAME LOOP
def main_game_loop():
    """Runs the main game loop, looking for input from the user."""
    run = True
    while run:
        clock.tick(GAME_DELAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bullet in bullets:
            if bullet.x_coord < 500 and bullet.x_coord > 0:
                bullet.x_coord += bullet.velocity
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            if hero.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 7:
                bullets.append(Projectile(round(hero.x_coord + hero.width//2), 
                round(hero.y_coord + hero.height//2), PROJECTILE_DIAMETER, (153,0,0), facing))

        if keys[pygame.K_LEFT] and hero.x_coord > hero.velocity:
            hero.x_coord -= hero.velocity
            hero.right = False
            hero.left = True
            hero.standing = False
        elif keys[pygame.K_RIGHT] and hero.x_coord < (GAME_WINDOW_X - hero.width - hero.velocity):
            hero.x_coord += hero.velocity
            hero.right = True
            hero.left = False
            hero.standing = False
        else:
            hero.standing = True
            hero.walk_count = 0

        if not hero.is_jump:
            if keys[pygame.K_UP]:
                hero.is_jump = True
                hero.right = False
                hero.left = False
                hero.walk_count = 0
        else:
            if hero.jump_count >= -7:
                neg = 1
                if hero.jump_count < 0:
                    neg = -1
                hero.y_coord -= (hero.jump_count ** 2) * neg
                hero.jump_count -= 1
            else:
                hero.is_jump = False
                hero.jump_count = 7
        redraw_game_window()
    pygame.quit()

if __name__ == '__main__':
    main_game_loop()
