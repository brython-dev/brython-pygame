

is_web_context = '__BRYTHON__' in globals()
if not is_web_context:
    import sys
    sys.path.append('../../scripts/Lib/site-packages/')
    import os
    img_path = os.path.join('assets', 'player.png')
else:
    img_path = 'player.png'


# - - - bare pygame example, with a Sprite -  - -

import pygame
from pygame.constants import QUIT, K_LEFT, K_RIGHT

pygame.init()
screen = pygame.display.set_mode((400, 300))


def bring_image(fn):
    global is_web_context
    if is_web_context:
        r = pygame.image.get_cached(fn)
    else:
        r = pygame.image.load(fn)
    return r


class Avatar(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        self.image = bring_image(img_path)
        self.image.set_colorkey((0xff, 0x00, 0xff))  # ugly pink
        
        self.rect = self.image.get_rect()
        self.rect.centerx = init_pos[0]
        self.rect.centery = init_pos[1]
        self.vx = 0
    
    def update(self):
        self.rect.centerx += self.vx


pl = Avatar((55, 71))


if not is_web_context:
    # game loop = a while loop
    clock = pygame.time.Clock()
    gameover= False
    
    while not gameover:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                gameover = True

        # update players position
        keyb = pygame.key.get_pressed()
        if keyb[K_RIGHT]:
            pl.vx = +1  # moves right
        elif keyb[K_LEFT]:
            pl.vx = -1  # moves left
        else:
            pl.vx = 0
        pl.update()

        # refresh screen
        screen.fill((0x80, 00, 99))
        screen.blit(pl.image, pl.rect.topleft)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    print('clean exit')

else:
    from browser import window
    keyb = {
        K_LEFT: False,
        K_RIGHT: False
    }
        
    def gameloop(tinfo):
        for ev in pygame.event.get():
            if ev.type == KEYDOWN:
                key[ev.key] = True
            elif ev.type == KEYUP:
                key[ev.key] = False

        # update players position
        if keyb[K_RIGHT]:
            pl.vx = +1  # moves right
        elif keyb[K_LEFT]:
            pl.vx = -1  # moves left
        else:
            pl.vx = 0
        pl.update()

        # refresh screen
        screen.fill((0x80, 00, 99))
        screen.blit(pl.image, pl.rect.topleft)
        pygame.display.update()
        window.requestAnimationFrame(gameloop)
    
    gameloop(None)
