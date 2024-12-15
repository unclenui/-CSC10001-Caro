import pygame
class Background:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, URL, x=0, y=0):
        self.background_surface    = pygame.image.load(URL) 
        self.background_surface    = pygame.transform.scale(self.background_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.x                     = x
        self.y                     = y
    
    def draw(self, screen):
        screen.blit(self.background_surface,(self.x,self.y))