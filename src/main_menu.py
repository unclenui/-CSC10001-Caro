import pygame
from .button import Button

class Main_menu:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.start_normal  = "assets/graphics/buttons/start_button.png"
        self.start_hover   = "assets/graphics/buttons/start_button_hover.png"
        self.start_button  = Button(SCREEN_WIDTH/2-100, SCREEN_HEIGHT/3, 160, 60, self.start_normal, self.start_hover)

        self.exit_normal   = "assets/graphics/buttons/exit_button.png"
        self.exit_hover    = "assets/graphics/buttons/exit_button_hover.png"
        self.exit_button   = Button(SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2, 160, 60, self.exit_normal, self.exit_hover)

        self.background0_surface = pygame.image.load("assets/graphics/backgrounds/bgl0.png")
        self.background0_surface = pygame.transform.scale(self.background0_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background1_surface = pygame.image.load("assets/graphics/backgrounds/bgl1.png")
        self.background1_surface = pygame.transform.scale(self.background1_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background2_surface = pygame.image.load("assets/graphics/backgrounds/bgl2.png")
        self.background2_surface = pygame.transform.scale(self.background2_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background3_surface = pygame.image.load("assets/graphics/backgrounds/bgl3.png")
        self.background3_surface = pygame.transform.scale(self.background3_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
    def draw(self, screen, running=True):
        screen.blit(self.background0_surface)
        screen.blit(self.background1_surface)
        screen.blit(self.background2_surface)
        screen.blit(self.background3_surface)
        
        for event in pygame.event.get():
            self.start_button.event = event
            self.exit_button.event = event
            
            if event.type == pygame.QUIT:
                running = False
            if self.start_button.is_pressed(event):
                print("Start Game Button Clicked")
            if self.exit_button.is_pressed(event):
                running = False
                print("Exit Game Button Clicked")
        # Update the display
        self.start_button.draw(screen)
        self.exit_button.draw(screen)
        pygame.display.update()
        
        return running