# Resource Hunters

**Resource Hunters** is a fun, grid-based resource collection game where multiple agents (including a human-controlled agent) navigate a grid to collect resources while avoiding obstacles. The game is displayed in fullscreen mode with a scoreboard tracking the agents' scores.

## Features

- **Human-controlled Agent**: Use arrow keys to move the human-controlled agent.
- **AI-controlled Agents**: The other agents move randomly.
- **Resource Collection**: Agents earn points by collecting resources on the grid.
- **Obstacles**: Agents lose points if they hit an obstacle.
- **Scoreboard**: A scoreboard tracks agent scores, flashing when an agent collects a resource.
- **Winner Declaration**: The game ends when an agent reaches a score of 100, displaying a pop-up with the winner's name.

## Game Instructions

- Move the human-controlled agent using the arrow keys.
- Collect resources by navigating to them on the grid.
- Avoid obstacles, as hitting them will deduct points.
- The game continues until one of the agents reaches a score of 100, at which point the game will declare a winner.

## Installation

1. Install Python 3.x if you haven't already: [Python Downloads](https://www.python.org/downloads/).
2. Install `pygame`:
    ```bash
    pip install pygame
    ```
3. Download the game assets:
    - `agent-1.png`, `agent-2.png`, ..., `agent-5.png` for the agent images.
    - `resource.png` for the resource image.
    - `obstacle.png` for the obstacle image.
4. Place the assets in the same directory as the Python script.

## Running the Game

1. Run the Python script:
    ```bash
    python resource_hunters.py
    ```
2. The game will launch in fullscreen mode. You can use the arrow keys to control the first agent. Other agents move randomly. The goal is to collect resources, avoid obstacles, and reach a score of 100 to win.

## Controls

- **Arrow Keys**: Move the human-controlled agent (Agent 1).
- **Escape (ESC)**: Exit fullscreen mode (pressing ESC during the game will quit).

## Customization

You can customize several parameters in the game code, such as:
- `NUM_AGENTS`: Number of agents in the game (default is 5).
- `NUM_RESOURCES`: Number of resources to collect (default is 20).
- `NUM_OBSTACLES`: Number of obstacles on the grid (default is 10).
- `GRID_SIZE`: The size of each grid cell (default is 32x32 pixels).

## Libraries Used

- **Pygame**: The game engine used for rendering, handling input, and controlling the game loop.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.

## Credits

- **Developed by**: [Your Name] (Replace with your name)
- **Inspiration**: A creative grid-based resource collection game idea.
