# project_AI_tictactoe_game
## Tic-Tac-Toe with AI

This project is a graphical Tic-Tac-Toe game implemented in Python using the Pygame library. Players can choose to play as **X** or **O** against a computer opponent powered by the **Minimax algorithm**, ensuring an optimal AI strategy.

## Features
- **Interactive GUI**: A clean and responsive interface built with Pygame for an enjoyable gaming experience.
- **Play as X or O**: Players can select their preferred symbol at the start of the game.
- **Smart AI Opponent**: The AI uses the Minimax algorithm to play optimally, ensuring challenging gameplay.
- **Game States**: The game tracks wins, losses, draws, and offers an option to restart after a match.

## How It Works
1. The user selects to play as **X** or **O**.
2. The game alternates turns between the user and the AI.
3. The AI makes decisions using the Minimax algorithm, ensuring it never loses.
4. The game ends with a win, loss, or draw, and the player can choose to restart.

## Technologies Used
- **Python**: For the core logic and game structure.
- **Pygame**: For creating the graphical interface and handling user interaction.
- **Minimax Algorithm**: For the AI decision-making process.

## Installation and Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-ai.git
   cd tic-tac-toe-ai
   ```
2. Install the required libraries:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python ruuner.py
   ```

## Folder Structure
- **`runner.py`**: The main script to run the game.
- **`tictactoe.py`**: Contains the core logic for game mechanics, including the Minimax algorithm.
- **Assets**: Fonts and other resources for the game.

## Future Enhancements
- Add multiplayer mode (local or online).
- Enhance the UI with animations and sound effects.
- Keep track of user scores across multiple games.
- Add difficulty levels for the AI.
