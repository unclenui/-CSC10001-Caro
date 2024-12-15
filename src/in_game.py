import pygame
from .run_type      import Run_type
from .background    import Background
from .holder        import Link
from .board         import Board
from .button        import Button
from .notification  import Notify   
from .setting       import Setting

class In_game:
    #INITIALIZE
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE=30):
        self.board          = Board(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
        self.back_ground    = Background(SCREEN_WIDTH, SCREEN_HEIGHT, Link.board)
        self.back_button    = Button(40, 20, 50, 50, Link.bb_normal, Link.bb_hover)
        self.setting        = Button(110, 20, 50, 50, Link.setting, Link.setting_hover)
        self.status         = Button(525, 80, 250, 80, Link.status, Link.status)
        self.undo           = Button(525, 180, 250, 80, Link.undo, Link.undo_hover)
        self.reset          = Button(525, 280, 250, 80, Link.reset, Link.reset_hover)
        self.click_sfx      = pygame.mixer.Sound(Link.click_sfx)
        self.notify         = Notify(SCREEN_WIDTH, SCREEN_HEIGHT)

    def draw(self, screen, running=Run_type().IN_GAME):
        #DRAW USER INTERFACE
        self.back_ground.draw(screen)
        self.board.draw_board(screen)
        self.back_button.draw(screen)
        self.setting.draw(screen)
        self.status.draw(screen)
        self.reset.draw(screen)
        self.undo.draw(screen)
        #STATUS BOARD
        TURN = (self.board.sm.x_img if self.board.player1 else self.board.sm.o_img)
        TURN = pygame.transform.scale(TURN, (60, 60))
        screen.blit(TURN, (680, 85))

        #EVENT CHECKER            
        for event in pygame.event.get():
            winner = self.board.check_winner()
            if winner == True:
                self.notify.update("Green won!")
                self.notify.draw(screen)
                self.board.reset()
            elif winner == False:
                self.notify.update("Brown won!")
                self.notify.draw(screen)
                self.board.reset()
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                status = self.board.update(x, y)
                if (status):
                    self.click_sfx.play()
                        
            if event.type == pygame.QUIT:
                running = Run_type().EXIT
            if self.back_button.is_pressed(event):
                running = Run_type().MAIN_MENU
                self.board.reset()
            if self.reset.is_pressed(event):
                self.board.reset()
            if self.undo.is_pressed(event):
                self.board.undo()
            if self.setting.is_pressed(event):
                running = self.board.sm.draw(screen)
        return running
            