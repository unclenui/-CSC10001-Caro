import pygame
from button import Button

class Main_menu:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        start_normal  = "../assets/graphics/buttons/start_button.png"
        start_hover   = "../assets/graphics/buttons/start_button_hover.png"
        start_button  = Button(SCREEN_WIDTH/2-100, SCREEN_HEIGHT/3, 160, 60, start_normal, start_hover)

        exit_normal   = "../assets/graphics/buttons/exit_button.png"
        exit_hover    = "../assets/graphics/buttons/exit_button_hover.png"
        exit_button   = Button(SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2, 160, 60, exit_normal, exit_hover)

        background0_surface = pygame.image.load("../assets/graphics/backgrounds/bgl0.png")
        background0_surface = pygame.transform.scale(background0_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        background1_surface = pygame.image.load("../assets/graphics/backgrounds/bgl1.png")
        background1_surface = pygame.transform.scale(background1_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        background2_surface = pygame.image.load("../assets/graphics/backgrounds/bgl2.png")
        background2_surface = pygame.transform.scale(background2_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        background3_surface = pygame.image.load("../assets/graphics/backgrounds/bgl3.png")
        background3_surface = pygame.transform.scale(background3_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
    def draw(self, screen):
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