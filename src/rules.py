import pygame
from .run_type   import Run_type
from .button     import Button
from .background import Background
from .holder     import Link

class Rules:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, FONT):
        #RULES BUTTONs
        self.SCREEN_WIDTH   = SCREEN_WIDTH
        self.SCREEN_HEIGHT  = SCREEN_HEIGHT
        self.leave_button   = Button(SCREEN_WIDTH//3*2, SCREEN_HEIGHT//6*5, 120, 45, Link.leave_normal, Link.leave_hover)
        #RULES BACKGROUND
        self.back_ground    = Background(SCREEN_WIDTH, SCREEN_HEIGHT, Link.rules_bg)
        self.board    = Background(SCREEN_WIDTH, SCREEN_HEIGHT, Link.board)
        # CONTENT
        header_text = "Tic-Tac-Toe Rules:"
        rules_text = [
            "1. The game is played on a grid.",
            "2. Players take turns to mark a cell.",
            "3. Winner is the first to get 5 marks in a row.",
            "4. Marks can be horizontal, vertical, or diagonal.",
        ]
        # Prepare text surfaces for header and rules
        self.header_surface = FONT.render(header_text, True, (0,0,0)) # Black text
        self.rule_surfaces = [FONT.render(rule, True, (0,0,0)) for rule in rules_text]
        self.header_x = (self.SCREEN_WIDTH - self.header_surface.get_width()) // 2
    
    def leave(self, screen, running=Run_type().RULES):
        self.back_ground.draw(screen)
        self.board.draw(screen)
        self.leave_button.draw(screen)
        screen.blit(self.header_surface, (self.header_x, 50))
        current_y = 100
        # Draw the rules text (aligned to the left)
        for rule_surface in self.rule_surfaces:
            screen.blit(rule_surface, (30, current_y)) 
            current_y += rule_surface.get_height() + 10  
        
        for event in pygame.event.get():
            #YES BUTTON
            if self.leave_button.is_pressed(event):
                running = Run_type().MAIN_MENU
                print("Leave Button Clicked")
        return running