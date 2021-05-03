import pygame, random
from game_variables import *
from player_class import Player
from enemy_class import Enemy
from projectile_class import Projectile

pygame.init()

pygame.display.set_caption("Change This Title Later")

clock = pygame.time.Clock()


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

#first instances of an enemy sprite
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
