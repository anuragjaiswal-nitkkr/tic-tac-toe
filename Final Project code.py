import tkinter as tk

# Define the constants
size_of_board = 640
symbol_size = (size_of_board // 4 - size_of_board // 8) // 2
symbol_thickness = 30
symbol_X_color = 'aqua'
symbol_O_color = 'orchid'
Green_color = 'deepskyblue'
Black_color = 'black'

class Tic_Tac_Toe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Tic-Tac-Toe')

        # Prompt for player names
        self.player_X_name = input("Enter Player 1's name: ")
        self.player_O_name = input("Enter Player 2's name: ")

        self.canvas = tk.Canvas(self.window, width=size_of_board, height=size_of_board, bg=Black_color)
        self.canvas.pack()
        # Input from user in form of clicks
        self.canvas.bind('<Button-1>', self.click)

        self.initialize_board()
        self.player_X_turns = True
        self.board_status = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.player_X_starts = True
        self.reset_board = False
        self.gameover = False
        self.tie = False
        self.X_wins = False
        self.O_wins = False

        self.X_score = 0
        self.O_score = 0
        self.tie_score = 0

    def mainloop(self):
        self.window.mainloop()

    def initialize_board(self):
        for i in range(2):
            self.canvas.create_line((i + 1) * size_of_board // 3, 0, (i + 1) * size_of_board // 3, size_of_board, fill=Green_color)

        for i in range(2):
            self.canvas.create_line(0, (i + 1) * size_of_board // 3, size_of_board, (i + 1) * size_of_board // 3, fill=Green_color)

    def play_again(self):
        self.initialize_board()
        self.player_X_starts = not self.player_X_starts
        self.player_X_turns = self.player_X_starts
        self.board_status = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def draw_O(self, logical_position):
        logical_position = list(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                outline=symbol_O_color)

    def draw_X(self, logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                fill=symbol_X_color)
        self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                fill=symbol_X_color)

    def display_gameover(self):
        if self.X_wins:
            self.X_score += 1
            text = f' Winner: {self.player_X_name} (X)'
            color = symbol_X_color
        elif self.O_wins:
            self.O_score += 1
            text = f' Winner: {self.player_O_name} (O)'
            color = symbol_O_color
        else:
            self.tie_score += 1
            text = 'Its a tie'
            color = 'light green'

        self.canvas.delete("all")
        self.canvas.create_text(size_of_board // 2, size_of_board // 3, font="cmr 60 bold", fill=color, text=text)

        score_text = 'Scores \n'
        self.canvas.create_text(size_of_board // 2, 5 * size_of_board // 8, font="cmr 40 bold", fill=Green_color,
                                text=score_text)

        score_text = f'{self.player_X_name} (X) : {self.X_score}\n'
        score_text += f'{self.player_O_name} (O) : {self.O_score}\n'
        score_text += 'Tie           : ' + str(self.tie_score)
        self.canvas.create_text(size_of_board // 2, 3 * size_of_board // 4, font="cmr 30 bold", fill=Green_color,
                                text=score_text)
        self.reset_board = True

        score_text = 'Click to play again \n'
        self.canvas.create_text(size_of_board // 2, 15 * size_of_board // 16, font="cmr 20 bold", fill="gray",
                                text=score_text)

    def convert_logical_to_grid_position(self, logical_position):
        return [(size_of_board // 3) * logical_position[0] + size_of_board // 6, (size_of_board // 3) * logical_position[1] + size_of_board // 6]

    def convert_grid_to_logical_position(self, grid_position):
        return [grid_position[0] // (size_of_board // 3), grid_position[1] // (size_of_board // 3)]

    def is_grid_occupied(self, logical_position):
        return self.board_status[logical_position[0]][logical_position[1]] != 0

    def is_winner(self, player):
        player = -1 if player == 'X' else 1

        for i in range(3):
            if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                return True
            if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                return True

        if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
            return True

        if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
            return True

        return False

    def is_tie(self):
        r, c = zip(*[(r, c) for r in range(3) for c in range(3) if self.board_status[r][c] == 0])
        return len(r) == 0

    def is_gameover(self):
        self.X_wins = self.is_winner('X')
        if not self.X_wins:
            self.O_wins = self.is_winner('O')

        if not self.O_wins:
            self.tie = self.is_tie()

        return self.X_wins or self.O_wins or self.tie

    def click(self, event):
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if not self.reset_board:
            if self.player_X_turns:
                if not self.is_grid_occupied(logical_position):
                    self.draw_X(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = -1
                    self.player_X_turns = not self.player_X_turns
            else:
                if not self.is_grid_occupied(logical_position):
                    self.draw_O(logical_position)
                    self.board_status[logical_position[0]][logical_position[1]] = 1
                    self.player_X_turns = not self.player_X_turns

            if self.is_gameover():
                self.display_gameover()
        else:  # Play Again
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False

# Main
if __name__ == "__main__":
    game_instance = Tic_Tac_Toe()
    game_instance.mainloop()
