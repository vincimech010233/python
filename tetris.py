import pygame
import random
import time

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 300, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tetris")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

# Tamaño del bloque y tablero
block_size = 30
board_width = 10
board_height = 20

# Define las piezas del Tetris (matrices 2D)
pieces = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]]
]

# Clase para representar el tablero
class Board:
    def __init__(self):
        self.grid = [[0] * board_width for _ in range(board_height)]

    def draw(self):
        for y in range(board_height):
            for x in range(board_width):
                if self.grid[y][x]:
                    pygame.draw.rect(screen, COLORS[self.grid[y][x]], (x * block_size, y * block_size, block_size, block_size))

# Clase principal del juego
class TetrisGame:
    def __init__(self):
        self.board = Board()
        self.current_piece = None
        self.piece_x = 0
        self.piece_y = 0
        self.last_fall_time = time.time()
        self.piece_color = None
        self.score = 0

    def generate_piece(self):
        piece_type = random.randint(0, len(pieces) - 1)
        self.current_piece = pieces[piece_type]
        self.piece_color = piece_type + 1
        self.piece_x = board_width // 2 - len(self.current_piece[0]) // 2
        self.piece_y = 0

    def draw(self):
        screen.fill(BLACK)
        self.board.draw()

        if self.current_piece:
            for y in range(len(self.current_piece)):
                for x in range(len(self.current_piece[y])):
                    if self.current_piece[y][x]:
                        pygame.draw.rect(screen, COLORS[self.piece_color], ((self.piece_x + x) * block_size, (self.piece_y + y) * block_size, block_size, block_size))

    def check_collision(self):
        for y in range(len(self.current_piece)):
            for x in range(len(self.current_piece[y])):
                if self.current_piece[y][x] and (self.piece_x + x < 0 or self.piece_x + x >= board_width or self.piece_y + y >= board_height or self.board.grid[self.piece_y + y][self.piece_x + x]):
                    return True
        return False

    def lock_piece(self):
        for y in range(len(self.current_piece)):
            for x in range(len(self.current_piece[y])):
                if self.current_piece[y][x]:
                    self.board.grid[self.piece_y + y][self.piece_x + x] = self.piece_color

    def clear_rows(self):
        rows_to_clear = []
        for y in range(board_height):
            if all(self.board.grid[y]):
                rows_to_clear.append(y)

        for row in rows_to_clear:
            self.board.grid.pop(row)
            self.board.grid.insert(0, [0] * board_width)
            self.score += 10  # Ganar puntos por cada fila completada

    def rotate_piece(self):
        if self.current_piece:
            original_piece = self.current_piece
            self.current_piece = list(zip(*reversed(self.current_piece)))
            if self.check_collision():
                self.current_piece = original_piece

    def run(self):
        clock = pygame.time.Clock()
        self.generate_piece()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.piece_x -= 1
                if self.check_collision():
                    self.piece_x += 1
            if keys[pygame.K_RIGHT]:
                self.piece_x += 1
                if self.check_collision():
                    self.piece_x -= 1
            if keys[pygame.K_DOWN]:
                self.piece_y += 1
                if self.check_collision():
                    self.piece_y -= 1
            if keys[pygame.K_SPACE]:
                self.rotate_piece()

            # Lógica de caída automática
            current_time = time.time()
            if current_time - self.last_fall_time > 1:  # Cambiar la velocidad de caída ajustando el valor
                self.piece_y += 1
                self.last_fall_time = current_time
                if self.check_collision():
                    self.piece_y -= 1
                    self.lock_piece()
                    self.clear_rows()
                    self.generate_piece()

            self.board.draw()
            self.draw()
            self.draw_score()
            pygame.display.flip()
            clock.tick(10)

    def draw_score(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(self.score), True, WHITE)
        screen.blit(score_text, (10, 10))

if __name__ == "__main__":
    game = TetrisGame()
    game.run()
