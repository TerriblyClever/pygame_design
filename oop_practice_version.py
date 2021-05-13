import pygame, random

from pygame.constants import JOYBUTTONDOWN
from game_variables import *
from player_class import Player
from enemy_class import Enemy
from projectile_class import Projectile

pygame.init()
pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick)

pygame.display.set_caption("Change This Title Later")

clock = pygame.time.Clock()

def redraw_game_window():
    """Primary method to redraw the game window at the end of each Main Loop iteration."""
    GAME_WINDOW.blit(background, (0,0))
    text = calibri.render('Score: ' + str(score), 1, (0,0,0))
    GAME_WINDOW.blit(text, (390, 10))
    hero.draw(GAME_WINDOW)
    for enemy in enemy_list:
        enemy.draw(GAME_WINDOW)
    for bullet in bullets:
        bullet.draw(GAME_WINDOW)
    pygame.display.update()

#first instance of a player sprite, requires x,y coordinates and a width,height
hero = Player(GAME_WINDOW_CENTER, GAME_WINDOW_BOTTOM, 64, 64)

#first instances of an enemy sprite
enemy_list = []
for i in range(1):
    enemy_list.append(Enemy(random.randint(32, GAME_WINDOW_X - 64), GAME_WINDOW_BOTTOM, 64, 64, GAME_WINDOW_X - 32, random.randint(0, 33)))

#collection of instances from the Projectile class
bullets = [] #list for keeping track of all bullet sprites


calibri = pygame.font.SysFont('calibri', 24, True) #can't be in game_variables because must be in file where pygame.init() called
#MAIN GAME LOOP
def main_game_loop():
    """Runs the main game loop, looking for input from the user."""
    global score
    run = True
    while run:
        clock.tick(GAME_DELAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == JOYBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shooting = True

        for bullet in bullets:
            for goblin in enemy_list:
                if (bullet.y_coord - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y_coord + bullet.radius > goblin.hitbox[1]):
                    if (bullet.x_coord + bullet.radius > goblin.hitbox[0] and bullet.x_coord - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]):
                        goblin.hit()
                        score += 1
                        bullets.pop(bullets.index(bullet))
            if bullet.x_coord < 500 and bullet.x_coord > 0:
                bullet.x_coord += bullet.velocity
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shooting:
            if hero.left:
                facing = -1
            else:
                facing = 1
            if len(bullets) < 7:
                bullets.append(Projectile(round(hero.x_coord + hero.width//2), round(hero.y_coord + hero.height//2), PROJECTILE_DIAMETER, (153,0,0), facing))
            shooting = False

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
            hero.jump()
        redraw_game_window()
    pygame.quit()

if __name__ == '__main__':
    main_game_loop()
