import pygame
from .run_type   import Run_type
from .background import Background
from .holder     import Link
from .board      import Board

class In_game:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE=60):
        self.board          = Board(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)
        self.back_ground    = Background(SCREEN_WIDTH, SCREEN_HEIGHT, Link.ingame_bg)
        
    def draw(self, screen, running=Run_type().IN_GAME):
        self.back_ground.draw(screen)
        self.board.draw_board(screen)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                self.board.update(x, y)
            if event.type == pygame.QUIT:
                running = Run_type().EXIT
        return running