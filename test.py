import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dropdown Menu Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (100, 149, 237)

# Font
FONT = pygame.font.Font(None, 25)

# Maze data example
mazeDatas = [
    (1, "Maze 1", "Simple Maze"),
    (2, "Maze 2", "Medium Maze"),
    (3, "Maze 3", "Complex Maze"),
]

# Dropdown Class
class DropdownMenu:
    def __init__(self, x, y, width, height, options, starting_option):
        self.rect = pygame.Rect(x, y, width, height)
        self.options = options
        self.selected = starting_option
        self.is_open = False
        self.option_height = height
        self.option_rects = [
            pygame.Rect(x, y + (i + 1) * height, width, height) for i in range(len(options))
        ]

    def draw(self, surface):
        # Draw main dropdown menu
        pygame.draw.rect(surface, GRAY, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 2)  # Border
        text = FONT.render(self.selected, True, BLACK)
        surface.blit(text, (self.rect.x + 5, self.rect.y + 5))

        # Draw options if menu is open
        if self.is_open:
            for i, option in enumerate(self.options):
                pygame.draw.rect(surface, WHITE, self.option_rects[i])
                pygame.draw.rect(surface, BLACK, self.option_rects[i], 2)
                text = FONT.render(option, True, BLACK)
                surface.blit(text, (self.option_rects[i].x + 5, self.option_rects[i].y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                # Toggle dropdown menu
                self.is_open = not self.is_open
            elif self.is_open:
                # Check if clicked on any option
                for i, option_rect in enumerate(self.option_rects):
                    if option_rect.collidepoint(event.pos):
                        self.selected = self.options[i]
                        self.is_open = False
                        return self.selected
                # Close menu if clicked outside
                self.is_open = False
        return None

# Dropdown setup
options_list = [f"{mazeData[10]}" for mazeData in mazeDatas]
starting_option = mazeDatas[0][10]
dropdown = DropdownMenu(10, 50, 180, 30, options_list, starting_option)

# Main loop
clock = pygame.time.Clock()
while True:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        selected_option = dropdown.handle_event(event)
        if selected_option:
            print(f"Selected: {selected_option}")

    # Draw dropdown
    dropdown.draw(screen)

    pygame.display.flip()
    clock.tick(30)
