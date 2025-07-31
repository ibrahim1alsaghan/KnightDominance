# Knight Dominance 🐴

A simple web app that finds the minimum number of knights needed to control every square on a chess board.

## What it does

Places the fewest knights possible on an n×n chess board so that every square is either:
- Occupied by a knight 🐴
- Under attack by a knight

## How to run

1. Install requirements:
```bash
pip install streamlit numpy requests streamlit-lottie
```

2. Run the app:
```bash
streamlit run app.py
```

3. Enter board size and click "Solve"

## Features

- Interactive web interface
- Visual board with knight positions
- Animated horse graphics
- Works with any board size

## Example

For a 4×4 board, you typically need 8 knights to control all squares.

## Tech Stack

- **Streamlit** - Web interface
- **NumPy** - Board calculations  
- **Lottie** - Animations

That's it! Simple chess puzzle solver with a nice UI.
