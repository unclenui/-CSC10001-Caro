import pygame
from src.main_menu import Main_menu
from src.run_type import Run_type

pygame.init()
FONT = pygame.font.Font("assets/fonts/main_font.ttf", 100)
pygame.mixer.init()
pygame.mixer.music.load("assets/audios/background.wav")
pygame.mixer.music.play(-1)

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600


# Screen setup


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Caro Game")

main_menu = Main_menu(SCREEN_WIDTH,  SCREEN_HEIGHT)
clock = pygame.time.Clock()

# Main loop
running = Run_type().MAIN_MENU
while running != Run_type().EXIT:
    if running == Run_type().MAIN_MENU:
        running = main_menu.draw(screen)
        pygame.display.update()
    elif running == Run_type().EXIT_CONFIRMATION:
        pass
    
pygame.quit()
