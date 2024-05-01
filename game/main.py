import pygame
import random
import math 

pygame.init()

FPS = 60

WIDTH, HEIGHT = 800, 800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = "#808080"
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = "#FFFFFF"
FONT_COLOR = "#776E65"


FONT = pygame.font.SysFont('freesansbold.ttf', 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')

class Tile:
    COLORS = [
        "#EEE4DA", "#EDE0C8", "#F2B179", "#F59563",
        "#F67C5F", "#F65E3B", "#EDCF72", "#EDCC61",
        "#EDC850", "#EDC53F", "#EDC22E", "#3C3A32"
    
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = self.col * RECT_WIDTH
        self.y = self.row * RECT_HEIGHT

    def get_color(self):
        return self.COLORS[int(math.log2(self.value)-1)]
    

    def draw(self, window):
        pygame.draw.rect(window, self.get_color(), (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))
        text = FONT.render(str(self.value), True, FONT_COLOR)
        text_rect = text.get_rect(center=(self.x + RECT_WIDTH // 2, self.y + RECT_HEIGHT // 2))
        window.blit(text, text_rect)

    def set_pos(self):
        self.x = self.col * RECT_WIDTH
        self.y = self.row * RECT_HEIGHT

    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]
        self.col = self.x // RECT_WIDTH
        self.row = self.y // RECT_HEIGHT



def draw_grid(window):
    for row in range(1, ROWS):
        y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
    for col in range(1, COLS):
        x = col * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)
    

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)
        
def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)
    pygame.display.update()

def get_random_pos(tiles):
    row = None
    col = None
    while True:
        row = random.randint(0, ROWS-1)
        col = random.randint(0, COLS-1)
        if f"{row}{col}" not in tiles:
            return row,col
    
def generate_tiles():
    tiles = {}
    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tile(2, row, col)
    return tiles

        

     

def main(window):

    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()  # Dictionary gives instant access to tiles

    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, tiles)
    pygame.quit()

if __name__ == '__main__':
    main(WINDOW)
    

