import pygame
from .holder import Link
from .setting       import Setting

class Board:
    #INITIALIZE
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BOX_SZ):
        self.sm             = Setting(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.start_x        = 40
        self.start_y        = 80
        self.board          = [[0 for _ in range(20)] for _ in range(20)]
        self.move_history   = []

        self.player1        = True
        
    #RESET BOARD
    def reset(self):
        self.board          = [[0 for _ in range(20)] for _ in range(20)]
        self.move_history   = []


    def draw_board(self, screen):
        for i in range(self.sm.grid_div):
            for j in range(self.sm.grid_div):
                    X = self.start_x + i*self.sm.box_sz
                    Y = self.start_y + j*self.sm.box_sz
                    if i != self.sm.box_sz-1 and j != self.sm.box_sz-1:
                        screen.blit(self.sm.box, (X, Y))       
                    if self.board[i][j]   == 1: #X
                        screen.blit(self.sm.x_img, (X, Y))
                    elif self.board[i][j] == 2: #O
                        screen.blit(self.sm.o_img, (X, Y))
    
    
    #CHECKER 
    def check_winner(self):
        for row in range(self.sm.grid_div):
            for col in range(self.sm.grid_div):
                if self.board[row][col] != 0:
                    #check colums
                    if col + 4 < self.sm.grid_div and all(self.board[row][col + i] == self.board[row][col] for i in range(5)):
                        return self.board[row][col] == 1
                    # check row
                    if row + 4 < self.sm.grid_div and all(self.board[row + i][col] == self.board[row][col] for i in range(5)):
                        return self.board[row][col] == 1
                    # check main diagnol
                    if row + 4 < self.sm.grid_div and col + 4 < self.sm.grid_div and all(self.board[row + i][col + i] == self.board[row][col] for i in range(5)):
                        return self.board[row][col] == 1
                    # check anti diagnol
                    if row - 4 >= 0 and col + 4 < self.sm.grid_div and all(self.board[row - i][col + i] == self.board[row][col] for i in range(5)):
                        return self.board[row][col] == 1
        return None
    ##RETURN TRUE if PLAYER1 WINS ELIF FALSE IF PLAYER2WIN, ELSE NONE
    
    def undo(self):
        if self.move_history:
            last_move = self.move_history.pop()
            self.board[last_move[0]][last_move[1]] = 0
            self.player1 = not self.player1
    
    #UPDATE IN-GAME STATUS
    def update(self, x, y):
        if (self.start_x <= x <= self.start_x + self.sm.grid_size) and (self.start_y <= y <= self.start_y + self.sm.grid_size):
            i = int((x - self.start_x)//self.sm.box_sz)
            j = int((y - self.start_y)//self.sm.box_sz)
            if self.player1 and not self.board[i][j]: 
                self.board[i][j] = 1
                self.move_history.append((i,j))
                self.player1 = not self.player1
                return True
            elif not self.player1 and not self.board[i][j]: 
                self.board[i][j] = 2
                self.move_history.append((i,j))
                self.player1 = not self.player1
                return True
        else: 
            return False


