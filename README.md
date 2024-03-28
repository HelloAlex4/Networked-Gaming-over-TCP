# Networked Snake Game

This project enables playing the classic snake game across two computers on the same network. One computer runs the game server and displays the game, while the other sends control commands (up, down, left, right) to steer the snake.

## How It Works

- The **server** hosts the snake game using Pygame and listens for control commands over a TCP connection.
- The **client** sends control commands based on keyboard inputs to the server.

## Setup

### Requirements

- Python 3.x
- Pygame (for the server)
- A network connection between the two computers

### Installation

1. **Install Pygame on the Server**: Run `pip install pygame` to install Pygame for Python.

2. **Download the Scripts**: Download `server.py` and `client.py` to the respective computers.

### Running the Game

1. **Server**:
   - Execute `python server.py` to start the game server.
   - The game window will open, and the server will start listening for control commands.

2. **Client**:
   - Modify `client.py` to set the server's IP address.
   - Run `python client.py` to start sending control commands.
   - Use the keys `W` (up), `A` (left), `S` (down), and `D` (right) to control the snake.

## Code Overview

### Server (`server.py`)

- Initializes a Pygame window and starts a game loop for the snake game.
- Listens for incoming TCP connections on a separate thread.
- Parses received messages to change the snake's direction.

### Client (`client.py`)

- Captures keypress events.
- Sends corresponding direction commands (`UP`, `DOWN`, `LEFT`, `RIGHT`) to the server.

## Contributions

Feel free to fork this project, submit issues, or send pull requests for improvements!
