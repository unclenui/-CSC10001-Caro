import pygame
from .run_type   import Run_type
from .button     import Button
from .background import Background
rt = Run_type()
class Main_menu:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.start_normal  = "assets/graphics/buttons/start_button.png"
        self.start_hover   = "assets/graphics/buttons/start_button_hover.png"
        self.start_button  = Button(SCREEN_WIDTH//3+10, SCREEN_HEIGHT// 3, 240, 90, self.start_normal, self.start_hover)
        
        self.rules_normal   = "assets/graphics/buttons/rules_button.png"
        self.rules_hover    = "assets/graphics/buttons/rules_button_hover.png"
        self.rules_button   = Button(SCREEN_WIDTH//3+10, SCREEN_HEIGHT//2, 240, 90, self.rules_normal, self.rules_hover)

        self.exit_normal    = "assets/graphics/buttons/exit_button.png"
        self.exit_hover     = "assets/graphics/buttons/exit_button_hover.png"
        self.exit_button    = Button(SCREEN_WIDTH//3+10, SCREEN_HEIGHT//1.5, 240, 90, self.exit_normal, self.exit_hover)
        self.back_ground    = Background(SCREEN_WIDTH, SCREEN_HEIGHT)

    def draw(self, screen, running=rt.MAIN_MENU):
        self.back_ground.draw(screen)
        
        for event in pygame.event.get():
            self.start_button.event  = event
            self.exit_button.event   = event
            self.rules_button.event  = event
            if event.type == pygame.QUIT:
                running = rt.EXIT
            if self.start_button.is_pressed(event):
                print("Start Game Button Clicked")
            if self.exit_button.is_pressed(event):
                running = rt.EXIT
                print("Exit Game Button Clicked")
            if self.rules_button.is_pressed(event):
                print("Rules Game Button Clicked")
        # Update the display
        self.start_button.draw(screen)
        self.exit_button.draw(screen)
        self.rules_button.draw(screen)
        
        return running