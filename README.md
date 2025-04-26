# Tic-Tac-Toe  🎮
"Tic-Tac-Toe game developed by our team, led by me, as part of our Python second-semester college project."

This is a Python-based GUI Tic-Tac-Toe game built using the Tkinter library.
Two players can play against each other on the same machine, with live score tracking and an option to replay without restarting the app!

# Key Features ✨

-> Dynamic GUI Board: Smooth and colorful board created with Tkinter Canvas.

-> Player Customization: Players enter their names at the start of the game.

-> Turn-Based Logic: The game manages player turns internally and updates the board accordingly.

-> Automatic Win Detection: Checks rows, columns, and diagonals to determine a winner.

-> Tie Detection: Recognizes tie situations when the board is full with no winner.

-> Scoreboard: Displays the running total of each player’s wins and the number of ties after each game.

-> Replayable: After a win or tie, players can click to start a new round immediately.

# How to Run 🚀

1.Make sure you have Python 3 installed.

2.Enter player names when prompted.

3.Start playing by clicking on the cells!

# Project Structure 🧠

-> Tic_Tac_Toe class: Manages the game window, board drawing, game logic, and user interaction.

-> Canvas and Event Binding: Mouse clicks are captured to detect and register moves.

-> Score Tracking: After each round, scores are displayed with an option to replay.

-> Board Status: Internally represented using a 3x3 matrix where:

0 = Empty

-1 = X's move

1 = O's move

*Main Functions:

-> initialize_board(): Draws the game board lines.

-> click(event): Handles player moves based on mouse click position.

-> draw_X() / draw_O(): Draws the respective symbols.

-> is_winner(), is_tie(), is_gameover(): Logic checks for end-game conditions.

-> display_gameover(): Shows win/tie message and updated scores.

# Highlights 🔥

-> Beautiful color schemes (aqua, orchid, deepskyblue, etc.)

-> Smooth transitions between games

-> Intuitive user experience — no prior setup needed beyond running the script

-> Easy to expand (for example: adding AI or animations)

-> Beautiful color schemes (aqua, orchid, deepskyblue, etc.)

-> Smooth transitions between games

Intuitive user experience — no prior setup needed beyond running the script

Easy to expand (for example: adding AI or animations)
