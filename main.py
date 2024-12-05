#INCLUDE
import pygame
from src.main_menu import Main_menu
from src.run_type import Run_type
from src.in_game import In_game
from src.holder import Link
from src.exit_cf import Exit_cf
from src.rules import Rules

pygame.init()

#FONT
FONT = pygame.font.Font("assets/fonts/main_font.ttf", 30)

#MUSIC
pygame.mixer.init()
pygame.mixer.music.load("assets/audios/background.wav")
pygame.mixer.music.play(-1)


#SCREEN SETTINGS
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
background_color = (30, 30, 30)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Caro Game")


#MOUSE CURSOR
cursor_image = pygame.image.load(Link.mouse)  
cursor_image = pygame.transform.scale(cursor_image, (32, 32)) 
pygame.mouse.set_visible(False)


#SCREEN TYPE
main_menu = Main_menu(SCREEN_WIDTH,  SCREEN_HEIGHT)
in_game   = In_game(SCREEN_WIDTH, SCREEN_HEIGHT)
exit_cf   = Exit_cf(SCREEN_WIDTH, SCREEN_HEIGHT)
rules = Rules(SCREEN_WIDTH, SCREEN_HEIGHT, FONT)
clock = pygame.time.Clock()


#MAIN LOOP
running = Run_type().MAIN_MENU
while running != Run_type().EXIT:
    
    if running == Run_type().MAIN_MENU:
        running = main_menu.draw(screen)
    elif running == Run_type().IN_GAME:
        running = in_game.draw(screen)
    elif running == Run_type().RULES:
        running = rules.leave(screen)    
    elif running == Run_type().EXIT_CONFIRMATION:
        main_menu.draw(screen)
        running = exit_cf.draw(screen)
    screen.blit(cursor_image, pygame.mouse.get_pos())
    pygame.display.update()
    clock.tick(60)
#QUIT     
pygame.quit()
