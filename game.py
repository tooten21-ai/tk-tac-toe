from tkinter import *
from tkinter import ttk, messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.create_ui()
        self.new_game()

    def create_ui(self):
        # Set up main application window
        self.root.title('Tic-Tac-Toe')

        # Create a content frame
        mainframe = ttk.Frame(self.root, padding=(3, 3, 12, 12))

        # Insert the frame into the user interface
        mainframe.grid(column=0, row=0)

        # Create button grid
        self.button_grid = [
            [],
            [],
            []
        ]
        for r in range(3):
            for c in range(3):
                button = ttk.Button(mainframe, command=lambda r=r, c=c: self.make_move(r, c), width=5)
                button.grid(row=r, column=c)
                self.button_grid[r].append(button)
        
        # Add polish
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=10, pady=10)

    def new_game(self):
        self.state = 'playerXturn'
        for r in range(3):
            for c in range(3):
                self.button_grid[r][c].config(text='')

    def make_move(self, row, column):
        if self.state == 'playerXturn' or self.state == 'playerOturn':
            if self.button_grid[row][column].cget('text') == '':
                if self.state == 'playerXturn':
                    btn_text = 'X'
                    self.state = 'playerOturn'
                else:
                    btn_text = 'O'
                    self.state = 'playerXturn'

                self.button_grid[row][column].config(text=btn_text)
                
                if self.check_winner() is not None:
                    self.state = 'game_over'
                    result = self.check_winner() 
                    if result == 'X' or result == 'O':
                        if messagebox.askyesno(message=f'The winner is {result}! Play again?', icon='question', title='Game over'):
                            self.new_game()
                        else: 
                            self.root.destroy()
                    else:
                        if messagebox.askyesno(message=f'Draw! Play again?', icon='question', title='Game over'):
                            self.new_game()
                        else:
                            self.root.destroy()
                    
    
    def check_this_player(self, player):
        win_conditions = [
            # Horizontal
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Vertical
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonal
            [(0, 0), (1, 1), (2, 2)],
            [(2, 0), (1, 1), (0, 2)]
        ]
        
        for win_condition in win_conditions:
            if all(self.button_grid[r][c].cget('text') == player for r, c in win_condition):
                    return player
     
        return None

    def is_board_filled(self):
        for r in range(3):
            for c in range(3):
                if self.button_grid[r][c].cget('text') == '':
                    return False
        
        return True

    def check_winner(self):
        if self.check_this_player('X') is not None:
            return self.check_this_player('X')
        elif self.check_this_player('O') is not None:
            return self.check_this_player('O')
        elif self.is_board_filled():
            return 'draw'
        else:
            return None
        

root = Tk()
TicTacToe(root)
root.mainloop()