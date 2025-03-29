# Resource Hunters: A Fun and Engaging Game 🎮

Welcome to **Resource Hunters**, a thrilling game where agents compete to collect resources while avoiding obstacles. This game allows one player to control an agent while others are controlled by the computer. Collect resources to increase your score and aim to be the first to reach the target score to win!

## Game Features 📋

- **Full-Screen Gameplay**: Enjoy an immersive experience in full-screen mode.
- **Agent Control**: Control an agent yourself or watch the AI agents navigate the playing field.
- **Obstacles and Resources**: Navigate through obstacles and gather resources to rack up points.
- **Scoring System**: The score can be increased by collecting resources, and reduced by hitting obstacles.
- **Victory Condition**: Reach a specified score to become the winner!
- **Custom Graphics**: Utilize custom images for agents, resources, and obstacles.

## 🎩 Watch the Gameplay Trailer

<video src="https://github.com/Deviprasad333/Resource-Hunters/edit/main/rss.mp4" controls width="600"></video>

## 🎩 How to Play

1. **Objective**: Collect resources worth 20 points each, while avoiding obstacles and competing against other agents. 
2. **Winning Condition**: The first agent to reach a score of 100 wins the game! 🏆
3. **Controls for Human Agent**:
   - ⬅️ Left Arrow: Move left
   - ➡️ Right Arrow: Move right
   - ⬆️ Up Arrow: Move up
   - ⬇️ Down Arrow: Move down
4. **Avoid Obstacles**: Colliding with obstacles will reduce your score by 2 points! 🛇

## 🖥️ Game Setup

- The game runs in **full-screen mode**.
- Agents are represented with unique images (placeholders for now). 🎨
- Resources and obstacles appear randomly on the grid.

## 🧩 Classes Overview

- **Agent**: Represents the player or AI agent with attributes such as position, score, and control type (human/AI).
- **Resource**: Items that agents collect to increase their score.
- **Obstacle**: Objects that agents need to avoid.

## 🏟️ Features

- **Scoreboard**: A live-updating scoreboard at the bottom displays the agents' scores.
- **Flash Effect**: The scoreboard cell flashes when an agent scores.
- **Winning Popup**: A fading effect announces the winner.

## Setup and Running the Game 🚀

1. Ensure you have **Python** and **Pygame** installed on your machine.
   - Install Pygame using: `pip install pygame`

2. Clone the repository or download the project files.

3. Ensure the following image files are located in the project directory:
   - `agent-1.png`, `agent-2.png`, ..., `agent-5.png` for agent images.
   - `resource.png` for the resource image.
   - `obstacle.png` for the obstacle image.

4. Run the game using the command:
   ```bash
   python resource_hunters.py
   ```

## Acknowledgements 🙏

- Developed by: **Deviprasad N Shetty**
- Thanks to the Pygame community for providing an excellent library for game development.

## Additional Notes 🗒️

- Customize the game by using different images or adjusting numbers of agents, resources, and obstacles in the code.
- The game's current resolution is set for standard screens; modify `WIDTH` and `HEIGHT` as needed for different screen setups.

Have fun playing **Resource Hunters**! May the best agent win! 🏆

---

Feel free to enhance the game, add new features, or improve the graphics according to your creativity.
