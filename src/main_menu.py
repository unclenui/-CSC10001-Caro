import pygame
from .run_type          import Run_type
from .button            import Button
from .background        import Background
from .holder            import Link
from .exit_cf           import Exit_cf
rt = Run_type()
class Main_menu:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        #MAIN MENU BUTTONs
        self.SCREEN_WIDTH   = SCREEN_WIDTH
        self.SCREEN_HEIGHT  = SCREEN_HEIGHT
        self.start_button   = Button(SCREEN_WIDTH//2-40, SCREEN_HEIGHT//6*3.75, 120, 45, Link.start_normal, Link.start_hover)
        self.rules_button   = Button(SCREEN_WIDTH//2-40, SCREEN_HEIGHT//6*4.375, 120, 45, Link.rules_normal, Link.rules_hover)
        self.exit_button    = Button(SCREEN_WIDTH//2-40, SCREEN_HEIGHT//6*5, 120, 45, Link.exit_normal, Link.exit_hover)
        self.yes_button     = Button(SCREEN_WIDTH//2-120, SCREEN_HEIGHT//2, 120, 60, Link.yes_normal, Link.yes_hover)
        self.no_button      = Button(SCREEN_WIDTH//2+40, SCREEN_HEIGHT//2, 120, 60, Link.no_normal, Link.no_hover)
        self.font           = pygame.font.Font(Link.font, 50)
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