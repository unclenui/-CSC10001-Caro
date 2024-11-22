import pygame
from src.button    import Button
# from src.main_menu import Main_menu
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/audios/background.wav")
pygame.mixer.music.play(-1)
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600
# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Caro Game")

# Create button
start_normal  = "assets/graphics/buttons/start_button.png"
start_hover   = "assets/graphics/buttons/start_button_hover.png"
start_pressed = "assets/graphics/buttons/start_button_clicked.png"
start_button  = Button(SCREEN_WIDTH/2-100, SCREEN_HEIGHT/3, 160, 60, start_normal, start_hover)

exit_normal   = "assets/graphics/buttons/exit_button.png"
exit_hover    = "assets/graphics/buttons/exit_button_hover.png"
exit_pressed  = "assets/graphics/buttons/exit_button_clicked.png"
exit_button   = Button(SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2, 160, 60, exit_normal, exit_hover)

background0_surface = pygame.image.load("assets/graphics/backgrounds/bgl0.png")
background0_surface = pygame.transform.scale(background0_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
background1_surface = pygame.image.load("assets/graphics/backgrounds/bgl1.png")
background1_surface = pygame.transform.scale(background1_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
background2_surface = pygame.image.load("assets/graphics/backgrounds/bgl2.png")
background2_surface = pygame.transform.scale(background2_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
background3_surface = pygame.image.load("assets/graphics/backgrounds/bgl3.png")
background3_surface = pygame.transform.scale(background3_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.blit(background0_surface)
    screen.blit(background1_surface)
    screen.blit(background2_surface)
    screen.blit(background3_surface)
    
    for event in pygame.event.get():
        start_button.event = event
        exit_button.event = event
        
        if event.type == pygame.QUIT:
            running = False
        if start_button.is_pressed(event):
            print("Start Game Button Clicked")
        if exit_button.is_pressed(event):
            running = False
            print("Exit Game Button Clicked")
    # Update the display
    start_button.draw(screen)
    exit_button.draw(screen)
    pygame.display.update()

pygame.quit()
