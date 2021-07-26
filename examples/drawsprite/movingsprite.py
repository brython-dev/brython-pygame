import coremon_main.conf_eng as conf
import coremon_main.engine as coremon
from coremon_main.events import EventReceiver, EngineEvTypes, CgmEvent, PygameBridge
from coremon_main.defs import enum_for_custom_event_types
import pygame

MyEvTypes = enum_for_custom_event_types(
    'InvadersMoveSide',
    'InvadersMoveDown',
    'PlayerReloads'
)
CgmEvent.inject_custom_names(MyEvTypes)


# --------------------------------------
#    CLASSES
# --------------------------------------
class GameModel:
    def __init__(self):
        self.invaders, self.colors, self.shots = [], [], []
        for x in range(15, 300, 15):
            for y in range(10, 100, 15):
                self.invaders.append(pygame.Rect(x, y, 7, 7))
                self.colors.append(((x * 0.7) % 256, (y * 2.4) % 256))


class InvadersView(EventReceiver):
    def __init__(self, ref_mod):
        super().__init__()
        self._mod = ref_mod

    def proc_event(self, ev, source):
        if ev.type == EngineEvTypes.PAINT:
            ev.screen.fill((0, 33, 0))
            for inva, (a, b) in zip(self._mod.invaders, self._mod.colors):
                pygame.draw.rect(ev.screen, (150, a, b), inva)
            for shotobj in self._mod.shots:
                pygame.draw.rect(ev.screen, (255, 180, 0), shotobj)
            pygame.draw.rect(ev.screen, (180, 180, 180), player)


class PlayerSpr(EventReceiver):  # represents the bird, not the game
    def __init__(self, img_path):
        super().__init__()

        print(img_path)
        self.image = pygame.image.load('assets/' + img_path)
        self.image.set_colorkey((0xff, 0x00, 0xff))

        # the bird's position
        self.x = 0
        self.y = 0

    def proc_event(self, ev, source):
        if ev.type == EngineEvTypes.PAINT:
            ev.screen.fill((25, 88, 0))
            ev.screen.blit(self.image, (self.x, self.y))

        elif ev.type == EngineEvTypes.LOGICUPDATE:
            dist = 2  # distance moved in each frame, try changing it to 5
            key = coremon.get_pressed_keys()
            if key[pygame.K_DOWN]:  # down key
                self.y += dist  # move down
            elif key[pygame.K_UP]:  # up key
                self.y -= dist  # move up
            if key[pygame.K_RIGHT]:  # right key
                self.x += dist  # move right
            elif key[pygame.K_LEFT]:  # left key
                self.x -= dist  # move left


##    def handle_keys(self):
##        """ Handles Keys """
##        key = coremon.get_pressed_keys()
##        
##
##    def draw(self, surface):
##        """ Draw on surface """
##        # blit yourself at your current position
##        surface.blit(self.image, (self.x, self.y))


# --------------------------------------
#    LAUNCHING
# --------------------------------------
##
### m v c
##player = pygame.Rect(150, 180, 10, 7)
##mod = GameModel()
##
##view = InvadersView(mod)
##
# activation
##view.turn_on()
##gctrl.turn_on()
##

# - from the bird program
# clock = pygame.time.Clock()
##running = True
##while running:
##    # handle every event since the last frame.
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##
##    bird.handle_keys() # handle the keys
##    
##    screen.fill((255,255,255)) # fill the screen with white
##    bird.draw(screen) # draw the bird to the screen
##    pygame.display.update() # update the screen
##    clock.tick(40)


def run():
    gctrl = coremon.retrieve_game_ticker()

    # activation
    bird = PlayerSpr('player.png')  # create an instance
    bird.turn_on()

    gctrl.turn_on()
    gctrl.loop()
