import pygame
from .run_type   import Run_type
from .button     import Button
from .background import Background
from .holder     import Link
rt = Run_type()

class Main_menu:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        #MAIN MENU BUTTONs
        self.SCREEN_WIDTH   = SCREEN_WIDTH
        self.SCREEN_HEIGHT  = SCREEN_HEIGHT
        self.start_button   = Button(SCREEN_WIDTH//2-40, SCREEN_HEIGHT//6*3.75, 120, 45, Link.start_normal, Link.start_hover)
        self.rules_button   = Button(SCREEN_WIDTH//2-40, SCREEN_HEIGHT//6*4.375, 120, 45, Link.rules_normal, Link.rules_hover)
        self.exit_button    = Button(SCREEN_WIDTH//2-40, SCREEN_HEIGHT//6*5, 120, 45, Link.exit_normal, Link.exit_hover)
        self.yes_button     = Button(SCREEN_WIDTH//2-40, SCREEN_HEIGHT//6*5, 120, 45, Link.yes_normal, Link.yes_hover)
        self.no_button      = Button(SCREEN_WIDTH//3*2, SCREEN_HEIGHT//6*5, 120, 45, Link.no_normal, Link.no_hover)
        #MAIN MENU BACKGROUND
        self.back_ground    = Background(SCREEN_WIDTH, SCREEN_HEIGHT, Link.menu_bg)
    
    def draw(self, screen, running=rt.MAIN_MENU):
        self.back_ground.draw(screen)
        #MENU EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = rt.EXIT
            #START BUTTON
            if self.start_button.is_pressed(event):
                running = Run_type().IN_GAME
                print("Start Game Button Clicked")
            #RULES BUTTON 
            if self.rules_button.is_pressed(event):
                running = rt.RULES
                print("Rules Game Button Clicked")
            #EXIT BUTTON                
            if self.exit_button.is_pressed(event):
                running = rt.EXIT_CONFIRMATION
                print("Exit Game Button Clicked")
                
        # Update the display
        self.start_button.draw(screen)
        self.exit_button.draw(screen)
        self.rules_button.draw(screen)
        
        return running
    def exit(self, screen, running=rt.EXIT_CONFIRMATION):
        bg = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pygame.SRCALPHA)
        bg.fill((255, 0, 0, 128))
        screen.blit(bg)
        self.yes_button.draw(screen)
        self.no_button.draw(screen)
        
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