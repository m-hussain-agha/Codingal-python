import pacman
import random

# Initialize Pygame
pacman.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
PACMAN_SIZE = 20
SPEED = 5
FPS = 30

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pacman.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pacman.display.set_caption("Pac-Man Game")

# Pac-Man class
class PacMan:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.size = PACMAN_SIZE

    def draw(self):
        pacman.draw.circle(screen, YELLOW, (self.x, self.y), self.size)

    def move(self, dx, dy):
        self.x += dx * SPEED
        self.y += dy * SPEED
        self.x = max(self.size, min(SCREEN_WIDTH - self.size, self.x))
        self.y = max(self.size, min(SCREEN_HEIGHT - self.size, self.y))

# Main game loop
def main():
    clock = pacman.time.Clock()
    pacman = PacMan()
    running = True

    while running:
        for event in pacman.event.get():
            if event.type == pacman.QUIT:
                running = False

        keys = pacman.key.get_pressed()
        dx = keys[pacman.K_RIGHT] - keys[pacman.K_LEFT]
        dy = keys[pacman.K_DOWN] - keys[pacman.K_UP]

        pacman.move(dx, dy)

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw Pac-Man
        pacman.draw()

        # Update the display
        pacman.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pacman.quit()

if __name__ == "__main__":
    main()
