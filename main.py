import pygame
from src.main_menu import Main_menu
pygame.init()
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
running = True
screen_status = "main menu"
while running:
    if screen_status == "main menu":
        running = main_menu.draw(screen)
    
pygame.quit()
