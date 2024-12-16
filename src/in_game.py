import pygame
from .run_type      import Run_type
from .background    import Background
from .holder        import Link
from .board         import Board
from .button        import Button
from .notification  import Notify   
from .setting       import Setting

class In_game:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE=30):
        self.board          = Board(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
        self.back_ground    = Background(SCREEN_WIDTH, SCREEN_HEIGHT, Link.board)
        self.back_button    = Button(40, 20, 50, 50, Link.bb_normal, Link.bb_hover)
        self.setting        = Button(110, 20, 50, 50, Link.setting, Link.setting_hover)
        self.status         = Button(525, 80, 250, 80, Link.status, Link.status)
        self.undo           = Button(525, 180, 250, 80, Link.undo, Link.undo_hover)
        self.reset          = Button(525, 280, 250, 80, Link.reset, Link.reset_hover)
        self.replay         = Button(525, 380, 250, 80, Link.replay_hover, Link.replay_hover)
        self.click_sfx      = pygame.mixer.Sound(Link.click_sfx)
        self.notify         = Notify(SCREEN_WIDTH, SCREEN_HEIGHT)

    def event_handle(self, screen, running=Run_type().IN_GAME):
        winner = None

        for event in pygame.event.get():
            winner = self.board.check_winner()
            if winner != None:
                self.notify.update("Game over!")
                self.notify.draw(screen)
                self.replay.normal_img = Link.replay
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if winner == None: status = self.board.update(x, y)
                self.click_sfx.play()
                        
            if self.undo.is_pressed(event) and winner == None:
                self.board.undo()
            
            if event.type == pygame.QUIT:
                running = Run_type().EXIT
            
            if self.back_button.is_pressed(event):
                running = Run_type().MAIN_MENU
                self.notify.time = 0
                self.board.reset()
            
            if self.reset.is_pressed(event):
                self.board.reset()
                self.notify.time = 0
            
            if self.replay.is_pressed(event) and winner != None:
                self.board.replay(screen)
                self.notify.time = 0
                self.replay.normal_img = Link.replay_hover
                
            if self.setting.is_pressed(event):
                running = self.board.sm.draw(screen)
                TURN = pygame.transform.scale((self.board.sm.x_img if self.board.player1 else self.board.sm.o_img), (60, 60))
                self.notify.time = 0
        return running
    
    def draw(self, screen, running=Run_type().IN_GAME):
        #DRAW USER INTERFACE
        self.back_ground.draw(screen)
        self.board.draw_board(screen)
        self.back_button.draw(screen)
        self.setting.draw(screen)
        self.status.draw(screen)
        self.reset.draw(screen)
        self.undo.draw(screen)
        self.replay.draw(screen)
        TURN = pygame.transform.scale((self.board.sm.x_img if self.board.player1 else self.board.sm.o_img), (60, 60))
        screen.blit(TURN, (680, 85))

        return self.event_handle(screen)
        #EVENT CHECKER            
            
        