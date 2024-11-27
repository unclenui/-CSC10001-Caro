import pygame
from .run_type   import Run_type
from .button     import Button
from .background import Background

class In_game:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.back_ground    = Background(SCREEN_WIDTH, SCREEN_HEIGHT, "assets/graphics/backgrounds/background-notitle.png")
        self.board          = pygame.Surface((400,400), pygame.SRCALPHA)
        self.SCREEN_WIDTH   = SCREEN_WIDTH
        self.SCREEN_HEIGHT  = SCREEN_HEIGHT

    def draw_grid(self, screen, GRID_SIZE):
        for x in range(2,GRID_SIZE+2):
            pygame.draw.line(screen, (255,255,255), (40*x, 40*2), (40*x, 440))
        for y in range(2,GRID_SIZE+2):
            pygame.draw.line(screen, (255,255,255), (40*2, 40*y), (440, 40*y))
        
    def draw(self, screen, running=Run_type().RULES):
        self.back_ground.draw(screen)
        screen.blit(self.board, (60, 60))
        self.draw_grid(screen, 10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = Run_type().EXIT
        # Update the display
        return running