import pygame
from .holder import Link
from .run_type import Run_type
from .button import Button
rt = Run_type()

class Exit_cf:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.SCREEN_WIDTH   = SCREEN_WIDTH
        self.SCREEN_HEIGHT  = SCREEN_HEIGHT
        self.yes_button     = Button(SCREEN_WIDTH//2-120, SCREEN_HEIGHT//4*3, 120, 60, Link.yes_normal, Link.yes_hover)
        self.no_button      = Button(SCREEN_WIDTH//2+40, SCREEN_HEIGHT//4*3, 120, 60, Link.no_normal, Link.no_hover)
        self.font           = pygame.font.Font(Link.font, 50)
    
    def event_handle(self, screen, running=rt.EXIT_CONFIRMATION):
        for event in pygame.event.get():
            #YES BUTTON
            if self.yes_button.is_pressed(event):
                running = Run_type().EXIT
                print("Yes Button Clicked")
            #NO BUTTON 
            if self.no_button.is_pressed(event):
                running = Run_type().MAIN_MENU
                print("No Button Clicked")
        return running
    
    def draw(self, screen, running=rt.EXIT_CONFIRMATION):
        bg = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.SRCALPHA)
        bg.fill((0, 0, 0, 128))
        text = self.font.render("Are you sure?", True, Link.color)
        screen.blit(bg, (0,0))
        screen.blit(text,  (260,380))
        self.yes_button.draw(screen)
        self.no_button.draw(screen)
        return self.event_handle(screen)
    
     