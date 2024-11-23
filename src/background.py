import pygame

class Background:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.background0_surface = pygame.image.load("assets/graphics/backgrounds/bgl0.png")
        self.background0_surface = pygame.transform.scale(self.background0_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background1_surface = pygame.image.load("assets/graphics/backgrounds/bgl1.png")
        self.background1_surface = pygame.transform.scale(self.background1_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background2_surface = pygame.image.load("assets/graphics/backgrounds/bgl2.png")
        self.background2_surface = pygame.transform.scale(self.background2_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background3_surface = pygame.image.load("assets/graphics/backgrounds/bgl3.png")
        self.background3_surface = pygame.transform.scale(self.background3_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
    def draw(self, screen):
        screen.blit(self.background0_surface)
        screen.blit(self.background1_surface)
        screen.blit(self.background2_surface)
        screen.blit(self.background3_surface)