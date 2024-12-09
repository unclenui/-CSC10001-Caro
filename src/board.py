import pygame
from .holder import Link
class Board:
    #INITIALIZE
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BOX_SZ):
        self.BOX_SZ         = BOX_SZ
        self.box            = pygame.image.load(Link.box)
        self.box            = pygame.transform.scale(self.box, (BOX_SZ, BOX_SZ))
        self.start_x        = 40
        self.start_y        = 80
        self.grid_size      = 9
        self.board          = [[0 for _ in range(9)] for _ in range(9)]
        self.move_history   = []

        self.x_img          = pygame.image.load(Link.x_img)
        self.x_img          = pygame.transform.scale(self.x_img, (BOX_SZ, BOX_SZ))
        self.o_img          = pygame.image.load(Link.o_img)
        self.o_img          = pygame.transform.scale(self.o_img, (BOX_SZ, BOX_SZ))
        self.player1        = True
    
    
    #RESET BOARD
    def reset(self):
        self.board          = [[0 for _ in range(9)] for _ in range(9)]
        self.move_history   = []


    #DRAW BOARD
    def draw_board(self, screen):
        for i in range(9):
            for j in range(9):
                    X = self.start_x + i*self.BOX_SZ
                    Y = self.start_y + j*self.BOX_SZ
                    if i != 8 and j != 8:
                        screen.blit(self.box, (X, Y))       
                    if self.board[i][j]   == 1: #X
                        screen.blit(self.x_img, (X, Y))
                    elif self.board[i][j] == 2: #O
                        screen.blit(self.o_img, (X, Y))
    
    
    #CHECKER 
    def check_winner(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.board[row][col] != 0:
                    #check colums
                    if col + 4 < self.grid_size and all(self.board[row][col + i] == self.board[row][col] for i in range(5)):
                        return self.board[row][col] == 1
                    # check row
                    if row + 4 < self.grid_size and all(self.board[row + i][col] == self.board[row][col] for i in range(5)):
                        return self.board[row][col] == 1
                    # check main diagnol
                    if row + 4 < self.grid_size and col + 4 < self.grid_size and all(self.board[row + i][col + i] == self.board[row][col] for i in range(5)):
                        return self.board[row][col] == 1
                    # check anti diagnol
                    if row - 4 >= 0 and col + 4 < self.grid_size and all(self.board[row - i][col + i] == self.board[row][col] for i in range(5)):
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
        if (self.start_x <= x and x <= self.start_x + 8*self.BOX_SZ) and (self.start_y <= y and y <= self.start_y + 8*self.BOX_SZ):
            i = (x - self.start_x)//self.BOX_SZ
            j = (y - self.start_y)//self.BOX_SZ
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


