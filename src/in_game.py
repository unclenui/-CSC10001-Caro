import pygame
from .run_type   import Run_type
from .background import Background
from .holder     import Link
from .board      import Board
from .button     import Button
class In_game:
    #INITIALIZE
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE=60):
        self.board          = Board(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
        self.back_ground    = Background(SCREEN_WIDTH, SCREEN_HEIGHT, Link.board)
        self.back_button    = Button(40, 20, 50, 50, Link.bb_normal, Link.bb_hover)
        self.status         = Button(520, 70, 250, 80, Link.status, Link.status)


    def draw(self, screen, running=Run_type().IN_GAME):
        #DRAW USER INTERFACE
        self.back_ground.draw(screen)
        self.board.draw_board(screen)
        self.back_button.draw(screen)
        self.status.draw(screen)
        if self.board.player1: screen.blit(self.board.x_img, (680, 75))
        else: screen.blit(self.board.o_img, (680, 75))

        #EVENT CHECKER            
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                winner = self.board.check_winner()
                if winner == None:
                    self.board.update(x, y)
                if winner == True:
                    print("Green won!")
                elif winner == False:
                    print("Brown won!")
            if event.type == pygame.QUIT:
                running = Run_type().EXIT
            if self.back_button.is_pressed(event):
                running = Run_type().MAIN_MENU
                self.board.reset()
        return running