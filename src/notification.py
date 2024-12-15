import pygame
import time
from .holder import Link

class Notify:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.SCREEN_WIDTH  = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        
        self.win_sfx   = pygame.mixer.Sound(Link.win_sfx)
        self.bg        = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.bg.fill((0, 0, 0, 128))
        self.font             = pygame.font.Font(Link.font, 100)
        self.text             = None
        self.text_surf        = self.font.render(self.text, True, Link.color)
        self.text_rect        = self.text_surf.get_rect() 
        self.text_rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        self.time             = 0
    
    def update(self, text):
        self.text = text
        self.text_surf        = self.font.render(self.text, True, Link.color)
        self.text_rect        = self.text_surf.get_rect() 
        self.text_rect.center = (self.SCREEN_WIDTH//2, self.SCREEN_HEIGHT//2)
        
    def draw(self, screen):
        if self.time: return 
        screen.blit(self.bg, (0, 0))
        screen.blit(self.text_surf, self.text_rect)
        pygame.display.update()
        self.win_sfx.play()
        time.sleep(2)
        self.time = self.time + 1
    