import pygame
class Background:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, URL):
        self.background_surface    = pygame.image.load(URL) 
        self.background_surface    = pygame.transform.scale(self.background_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
    def draw(self, screen):
        screen.blit(self.background_surface,(0,0))