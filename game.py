import pygame
import random

# Initialize pygame
pygame.init()

# Full-screen mode
info = pygame.display.Info()  # Get screen dimensions
WIDTH, HEIGHT = info.current_w, info.current_h - 200  # Deduct 200px for the scoreboard
GRID_SIZE = 32
NUM_AGENTS = 5
NUM_RESOURCES = 20
NUM_OBSTACLES = 10
SCOREBOARD_HEIGHT = 200  # Height reserved for the scoreboard
CELL_PADDING = 10  # Padding inside table cells
BORDER_WIDTH = 2  # Width of the border around each cell

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
DARK_GREY = (40, 40, 40)  # For scoreboard background
BLUE = (0, 0, 255)
BORDER_COLOR = (255, 255, 255)  # Color of the table borders
SCORE_FLASH_COLOR = (255, 255, 0)  # Color to flash when an agent scores
WINNER_COLOR = (0, 255, 0)  # Color for winner text

# Set up the screen for full-screen mode
screen = pygame.display.set_mode((WIDTH, HEIGHT + SCOREBOARD_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Resource Hunters")

# Clock to control the game's framerate
clock = pygame.time.Clock()

# Load agent images (each agent has a unique image)
agent_images = [pygame.transform.scale(pygame.image.load(f'agent-{i+1}.png'), (GRID_SIZE, GRID_SIZE)) for i in range(NUM_AGENTS)]

# Load images for resources and obstacles
resource_img = pygame.transform.scale(pygame.image.load('resource.png'), (GRID_SIZE, GRID_SIZE))
obstacle_img = pygame.transform.scale(pygame.image.load('obstacle.png'), (GRID_SIZE, GRID_SIZE))

# Define creative font for the scoreboard (custom font)
creative_font = pygame.font.Font(pygame.font.match_font('Comic Sans MS'), 40)  # Comic Sans as an example
# Define regular font for agent scores
font = pygame.font.SysFont(None, 30)

# Agent class
class Agent:
    def __init__(self, x, y, name, img, human_control=False):
        self.x = x
        self.y = y
        self.name = name
        self.image = img
        self.score = 0  # Initial score set to zero
        self.speed = GRID_SIZE
        self.flash_count = 0  # Tracks border flash duration when agent scores
        self.human_control = human_control  # Whether this agent is controlled by the user

    def move(self, obstacles):
        if self.human_control:
            keys = pygame.key.get_pressed()  # Get key presses
            if keys[pygame.K_LEFT]:
                dx, dy = -1, 0
            elif keys[pygame.K_RIGHT]:
                dx, dy = 1, 0
            elif keys[pygame.K_UP]:
                dx, dy = 0, -1
            elif keys[pygame.K_DOWN]:
                dx, dy = 0, 1
            else:
                dx, dy = 0, 0
        else:
            # Random movement (up, down, left, right)
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            dx, dy = random.choice(directions)

        new_x = self.x + dx * self.speed
        new_y = self.y + dy * self.speed

        # Stay within bounds and avoid obstacles
        if (0 <= new_x < WIDTH) and (0 <= new_y < HEIGHT):
            if (new_x, new_y) not in [(obs.x, obs.y) for obs in obstacles]:  # Avoid obstacles
                self.x = new_x
                self.y = new_y
            else:
                # Deduct points if agent hits an obstacle
                self.score -= 2

    def draw(self, screen):
        # Draw agent image
        screen.blit(self.image, (self.x, self.y))

# Resource class
class Resource:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(resource_img, (self.x, self.y))

# Obstacle class
class Obstacle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(obstacle_img, (self.x, self.y))

# Function to check if a position overlaps with an existing object
def is_overlap(x, y, obstacles, resources):
    return (x, y) in [(obs.x, obs.y) for obs in obstacles] or (x, y) in [(r.x, r.y) for r in resources]

# Create obstacles, ensuring no overlap with resources
obstacles = []
while len(obstacles) < NUM_OBSTACLES:
    x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    if not is_overlap(x, y, obstacles, []):  # Check for obstacle overlap only
        obstacles.append(Obstacle(x, y))

# Create resources, ensuring no overlap with obstacles
resources = []
while len(resources) < NUM_RESOURCES:
    x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    if not is_overlap(x, y, obstacles, resources):  # Check for overlap with both obstacles and existing resources
        resources.append(Resource(x, y))

# Draw scoreboard in a tabular format with borders and padding
def draw_scoreboard(screen, agents):
    pygame.draw.rect(screen, DARK_GREY, (0, HEIGHT, WIDTH, SCOREBOARD_HEIGHT))  # Dark grey background for scoreboard
    
    # Adjust the title position
    title_text = creative_font.render("RESOURCE HUNTERS-Scorecard", True, WHITE)
    title_width = title_text.get_width()
    screen.blit(title_text, (WIDTH // 2 - title_width // 2, HEIGHT + 30))  # Increased space above the title

    cell_width = WIDTH // 3  # Three columns
    cell_height = (SCOREBOARD_HEIGHT - 80) // 2  # Space for title and padding (increased)

    # Display agents in a 3x2 table format
    for i, agent in enumerate(agents):
        row = i // 3  # Row index (0 or 1)
        col = i % 3   # Column index (0, 1, or 2)
        
        cell_x = col * cell_width
        cell_y = HEIGHT + 80 + row * cell_height  # Increased space below the title

        # Determine the border color: flash if the agent recently scored
        if agent.flash_count > 0:
            border_color = SCORE_FLASH_COLOR
            agent.flash_count -= 1  # Decrease flash count
        else:
            border_color = BORDER_COLOR

        # Draw cell border
        pygame.draw.rect(screen, border_color, (cell_x, cell_y, cell_width, cell_height), BORDER_WIDTH)

        # Display agent image inside the cell with padding
        screen.blit(agent.image, (cell_x + CELL_PADDING, cell_y + CELL_PADDING))

        # Display agent name and score next to the image inside the cell
        score_text = font.render(f"{agent.name}: {agent.score}", True, WHITE)
        screen.blit(score_text, (cell_x + GRID_SIZE + 2 * CELL_PADDING, cell_y + CELL_PADDING))

# Create agents, including one human-controlled agent
agents = [Agent(random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE, 
                f"Agent {i+1}", agent_images[i], human_control=(i == 0))  # First agent is human-controlled
          for i in range(NUM_AGENTS)]

def display_winner(winner):
    # Display winner pop-up
    popup_width, popup_height = 400, 200
    popup_x = (WIDTH - popup_width) // 2
    popup_y = (HEIGHT - popup_height) // 2

    # Create a fade effect
    for alpha in range(0, 255, 5):  # Fade in
        screen.fill((0, 0, 0))  # Clear the screen
        pygame.draw.rect(screen, (0, 0, 0, alpha), (popup_x, popup_y, popup_width, popup_height))
        winner_text = creative_font.render(f"{winner} is the Winner!", True, WINNER_COLOR)
        text_rect = winner_text.get_rect(center=(popup_x + popup_width // 2, popup_y + popup_height // 2))
        screen.blit(winner_text, text_rect)
        pygame.display.flip()
        clock.tick(30)

    # Pause for a moment
    pygame.time.delay(2000)

    # Fade out effect
    for alpha in range(255, 0, -5):  # Fade out
        screen.fill((0, 0, 0))  # Clear the screen
        pygame.draw.rect(screen, (0, 0, 0, alpha), (popup_x, popup_y, popup_width, popup_height))
        winner_text = creative_font.render(f"{winner} is the Winner!", True, WINNER_COLOR)
        text_rect = winner_text.get_rect(center=(popup_x + popup_width // 2, popup_y + popup_height // 2))
        screen.blit(winner_text, text_rect)
        pygame.display.flip()
        clock.tick(30)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # Clear the screen with grey

    # Move agents and check for resource collection
    for agent in agents:
        agent.move(obstacles)
        for resource in resources:
            if agent.x == resource.x and agent.y == resource.y:
                agent.score += 20  # Increase score by 20 when collecting resource
                agent.flash_count = 5  # Flash border for a short period
                resources.remove(resource)  # Remove the collected resource

    # Redraw resources, obstacles, and agents
    for resource in resources:
        resource.draw(screen)
    for obstacle in obstacles:
        obstacle.draw(screen)
    for agent in agents:
        agent.draw(screen)

    # Draw the scoreboard
    draw_scoreboard(screen, agents)

    # Check for winner
    for agent in agents:
        if agent.score >= 100:  # Example winning condition
            display_winner(agent.name)
            running = False  # End the game after declaring a winner

    pygame.display.flip()  # Update the display
    clock.tick(10)  # Limit the framerate to 10 FPS

pygame.quit()
