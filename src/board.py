import pygame
from .holder import Link
class Board:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BOX_SZ):
        self.BOX_SZ         = BOX_SZ
        self.box            = pygame.image.load(Link.box)
        self.box            = pygame.transform.scale(self.box, (BOX_SZ, BOX_SZ))
        self.start_x        = 40
        self.start_y        = 40
        self.board          = [[0 for _ in range(9)] for _ in range(9)]

        self.x_img          = pygame.image.load(Link.x_img)
        self.x_img          = pygame.transform.scale(self.x_img, (BOX_SZ, BOX_SZ))
        self.o_img          = pygame.image.load(Link.o_img)
        self.o_img          = pygame.transform.scale(self.o_img, (BOX_SZ, BOX_SZ))
        self.player1       = True
    
    def draw_board(self, screen):
        for i in range(9):
            for j in range(9):
                    X = self.start_x + i*self.BOX_SZ
                    Y = self.start_y + j*self.BOX_SZ
                    screen.blit(self.box, (X, Y))       
                    if self.board[i][j]   == 1: #X
                        screen.blit(self.x_img, (X, Y))
                    elif self.board[i][j] == 2: #O
                        screen.blit(self.o_img, (X, Y))
    
    def update(self, x, y):
        if (self.start_x <= x and x <= self.start_x + 8*self.BOX_SZ) and (self.start_y <= y and y <= self.start_y + 8*self.BOX_SZ):
            i = (x - self.start_x)//self.BOX_SZ
            j = (y - self.start_y)//self.BOX_SZ
            if self.player1: self.board[i][j] = 1
            else: self.board[i][j] = 2
            self.player1 = not self.player1