
def draw_grid(size):
    # Vẽ các đường dọc
    for x in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT), LINE_WIDTH)
    # Vẽ các đường ngang
    for y in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, y * CELL_SIZE), (WIDTH, y * CELL_SIZE), LINE_WIDTH)