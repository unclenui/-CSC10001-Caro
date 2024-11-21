import pygame

class Button:
    def __init__(self, x, y, width, height, normal, hover):
        #rect init
        self.rect            = pygame.Rect(x, y, width, height)
        self.width           = width
        self.height          = height
        self.x               = x
        self.y               = y
        self.normal_img      = normal
        self.hover_img       = hover
        self.button_type     = normal

    def button_phase(self):
        self.button_type = self.hover_img if self.is_hovered() else self.normal_img
    
    def is_hovered(self)->bool:
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def is_pressed(self, event)->bool:
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1 
            and self.rect.collidepoint(event.pos)
        )
    
    def draw(self, screen):
        self.button_phase()
        button_surface = pygame.image.load(self.button_type)
        button_surface = pygame.transform.scale(button_surface, (self.width, self.height))
        screen.blit(button_surface, (self.x, self.y))

    