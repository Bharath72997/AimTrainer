import pygame
import math
import random

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Initialize the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIM TRAINER")

# Font setup
font = pygame.font.SysFont("comicsans", 40)
score_font = pygame.font.SysFont("comicsans", 30)

# Target class
class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.05

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.grow:
            self.size += self.GROWTH_RATE
            if self.size >= self.MAX_SIZE:
                self.size = self.MAX_SIZE
                self.grow = False
        else:
            self.size -= self.GROWTH_RATE
            if self.size <= 0:
                self.size = 0
                self.grow = True

    def draw(self, win):
        pygame.draw.circle(win, RED, (self.x, self.y), int(self.size))
    
    def check_collision(self, mouse_x, mouse_y):
        distance = math.sqrt((self.x - mouse_x) ** 2 + (self.y - mouse_y) ** 2)
        return distance <= self.size


# Main game loop
def main():
    run = True
    score = 0
    targets = [Target(random.randint(100, WIDTH - 400), random.randint(100, HEIGHT - 100)) for _ in range(5)]  # 5 targets initially

    # Game loop
    while run:
        WIN.fill(LIGHT_BLUE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for target in targets:
                    if target.check_collision(mouse_x, mouse_y):
                        score += 1
                        targets.remove(target)  # Remove the target clicked
                        # Add a new target at a random position
                        targets.append(Target(random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100)))

        # Update and draw targets
        for target in targets:
            target.update()
            target.draw(WIN)

        # Display score
        score_text = score_font.render(f"Score: {score}", True, BLACK)
        WIN.blit(score_text, (10, 10))

        pygame.display.update()

    pygame.quit()


# Start Menu
def start_menu():
    run = True
    while run:
        WIN.fill(LIGHT_BLUE)

        # Draw Start Menu text
        title_text = font.render("AIM TRAINER", True, BLACK)
        start_text = font.render("Click to Start", True, GREEN)

        WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 100))
        WIN.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + 50))

        # Event handling for starting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()  # Start the game when clicked

        pygame.display.update()


# Game Over Screen
def game_over(score):
    run = True
    while run:
        WIN.fill(LIGHT_BLUE)

        # Draw Game Over text
        game_over_text = font.render("GAME OVER", True, BLACK)
        final_score_text = score_font.render(f"Your Score: {score}", True, BLACK)
        restart_text = score_font.render("Click to Restart", True, GREEN)

        WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))
        WIN.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2))
        WIN.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))

        # Event handling for restarting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_menu()  # Restart the game when clicked

        pygame.display.update()


# Run the start menu
if __name__ == "__main__":
    start_menu()
