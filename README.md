# 🎮 Resource Hunters

**Resource Hunters** is a fun, grid-based game where agents compete to collect resources while avoiding obstacles. The game features one human-controlled agent and other AI-driven agents that navigate the map. First agent to collect 100 points wins! 

Developed by: **Deviprasad N Shetty** 🚀

## 🕹️ How to Play

1. **Objective**: Collect resources worth 20 points each, while avoiding obstacles and competing against other agents. 
2. **Winning Condition**: The first agent to reach a score of 100 wins the game! 🏆
3. **Controls for Human Agent**:
   - ⬅️ Left Arrow: Move left
   - ➡️ Right Arrow: Move right
   - ⬆️ Up Arrow: Move up
   - ⬇️ Down Arrow: Move down
4. **Avoid Obstacles**: Colliding with obstacles will reduce your score by 2 points! 🚧

## 🖥️ Game Setup

- The game runs in **full-screen mode**.
- Agents are represented with unique images (placeholders for now). 🎨
- Resources and obstacles appear randomly on the grid.

## 🧩 Classes Overview

- **Agent**: Represents the player or AI agent with attributes such as position, score, and control type (human/AI).
- **Resource**: Items that agents collect to increase their score.
- **Obstacle**: Objects that agents need to avoid.

## 🏗️ Features

- **Scoreboard**: A live-updating scoreboard at the bottom displays the agents' scores.
- **Flash Effect**: The scoreboard cell flashes when an agent scores.
- **Winning Popup**: A fading effect announces the winner.

## 🛠️ Installation

1. Install Pygame:
   ```bash
   pip install pygame
