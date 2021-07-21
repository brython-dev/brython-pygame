
    
import pygame

print('pygame version is= ', end='')
print(pygame.ver)

pygame.init()

game_over = False

screen = pygame.display.set_mode((640,480))

screen.fill(pygame.color.Color('antiquewhite2'))

# let's create 20 rect objects...
fg_elements = list()
for rank in range(10):
    fg_elements.append(pygame.rect.Rect(16+ rank*55, 33, 25, 40))
for rank in range(10):
    fg_elements.append(pygame.rect.Rect(16+ rank*50, 93, 33, 12))

# it can be drawn
for elt in fg_elements:
    pygame.draw.rect(screen, pygame.color.Color('aquamarine4'), elt)
