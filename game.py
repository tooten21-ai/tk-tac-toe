from tkinter import *
from tkinter import ttk

class TicTacToe:
    def __init__(self, root):
        # Set up main application window
        root.title("Tic-Tac-Toe")

        # Create a content frame
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))

        # Insert the frame into the user interface
        mainframe.grid(column=0, row=0)

        # Create button grid
        button_grid = [
            [],
            [],
            []
        ]
        for r in range(3):
            for c in range(3):
                button = ttk.Button(mainframe, width=5)
                button.grid(row=r, column=c)
                button_grid[r].append(button)

        # Add polish
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=10, pady=10)
    
    def make_move(self):
        pass


root = Tk()
TicTacToe(root)
root.mainloop()