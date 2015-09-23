import pygame
from pygame.locals import *
import util 
from sound import play_sound

class Menu:
    OPTS = [
            'STYLE 1',
            'STYLE 2',
            'QUIT'
        ]
    def __init__(self, screen):
        self.screen = screen
    
        self.current = 0

    def run(self, elapse):
        self.draw()
        for e in pygame.event.get():
            if e.type == QUIT:
                return 'quit'
            elif e.type == KEYDOWN:
                if e.key == K_UP:
                    self.current = (self.current - 1) % len(self.OPTS)
                    play_sound('menu')
                elif e.key == K_DOWN:
                    self.current = (self.current + 1) % len(self.OPTS)
                    play_sound('menu')
                elif e.key == K_RETURN:
                    return self.OPTS[self.current].lower()
        return 'menu'

    def draw(self):
        #self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.image.load(util.file_path("menu.jpg")).convert(), (0, 0))
        for idx in xrange(len(self.OPTS)):
            if idx == self.current:
                util.myprint(self.screen, self.OPTS[idx], (280, 80 * idx + 250))
            else:
                util.myprint(self.screen, self.OPTS[idx], (280, 80 * idx + 250),
                        's', (160, 160, 160))

