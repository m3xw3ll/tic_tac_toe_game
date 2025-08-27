# Unbeatable Tic-Tac-Toe

An elegant tic-tac-toe game implemented in Python using Pygame, featuring an unbeatable AI opponent powered by the minimax algorithm with alpha-beta pruning.

## Features

- **Unbeatable AI**: Uses the minimax algorithm with alpha-beta pruning optimization
- **Intuitive Interface**: Clean, modern graphics with smooth gameplay
- **Visual Feedback**: Clear indication of player turns and game status
- **Restart Functionality**: Easy game restart with a single click
- **Responsive Design**: Smooth animations and visual effects

## Screenshots

The game features:
- Blue X's for the human player
- Red O's for the AI player
- Clean grid layout with clear visual separation
- Game status indicators
- End game overlay with restart button

## Installation

1. Clone or download this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

1. Run the game:
```bash
python tic_tac_toe.py
```

2. **Game Rules**:
   - You play as X (blue)
   - AI plays as O (red)
   - Click on any empty cell to make your move
   - The AI will automatically make its move after yours
   - First to get three in a row (horizontal, vertical, or diagonal) wins
   - The game will end in a tie if the board fills up with no winner

3. **Controls**:
   - **Left Click**: Make a move on an empty cell
   - **Left Click on "Play Again"**: Restart the game after it ends

## Game Features

### Minimax Algorithm
The AI uses the minimax algorithm with alpha-beta pruning to evaluate all possible game states and choose the optimal move. This makes the AI truly unbeatable - the best you can do is tie!

### Visual Design
- Clean, modern interface
- Contrasting colors for easy visibility
- Clear game state indicators
- Smooth game flow with AI thinking delay

### Game States
- **Your Turn**: Blue status text indicates it's your move
- **AI Thinking**: Red status text with brief delay for natural feel  
- **Game Over**: Overlay with result and restart option

## Technical Details

- **Language**: Python 3.x
- **Graphics Library**: Pygame 2.5.2
- **AI Algorithm**: Minimax with alpha-beta pruning
- **Game Logic**: Complete state management with win detection
- **Performance**: Optimized with alpha-beta pruning for instant moves

## Code Structure

- `TicTacToe` class: Main game logic and AI implementation
- `minimax()`: AI decision-making algorithm
- `draw_board()`: Rendering and UI management
- `main()`: Game loop and event handling

## Challenge Yourself

Try to beat the AI! The minimax algorithm ensures that:
- If you play perfectly, you'll get a tie
- Any mistake will result in the AI winning
- The AI never makes suboptimal moves

Good luck - you'll need it! 🎮