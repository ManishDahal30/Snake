import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
GRID_COLOR = (50, 50, 50)
BACKGROUND_COLOR = (0, 128, 0)  # Green background color

# Set up snake
SNAKE_COLOR = (255, 0, 0)  # Red snake color
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (0, -1)  # Initial direction: up

# Set up food
FOOD_COLOR = (255, 255, 0)  # Yellow food color
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Set up game variables
clock = pygame.time.Clock()
score = 0
lives = 3

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Main game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    # Move snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    if new_head in snake or new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
        # Snake hits itself or the wall, reduce one life
        lives -= 1
        if lives == 0:
            running = False
        else:
            snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]  # Reset snake position
            snake_direction = (0, -1)  # Reset snake direction
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))  # Respawn food
    else:
        snake.insert(0, new_head)
        if new_head == food:
            # Snake eats food, increase score and generate new food
            score += 1
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, FOOD_COLOR, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw lives
    for i in range(lives):
        pygame.draw.circle(screen, (255, 0, 0), (WIDTH - 50 - i * 30, 25), 10)  # Draw red circles to indicate lives

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(8)  # Reduced speed by 20%

# Quit Pygame
pygame.quit()
