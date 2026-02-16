from tkinter import *
from tkinter import ttk

# Set up main application window
root = Tk()
root.title("Tic-Tac-Toe")

# Create a content frame
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))

# Insert the frame into the user interface
mainframe.grid(column=0, row=0)

# Create button grid
for i in range(3):
    for j in range(3):
        ttk.Button(mainframe, width=5).grid(row=i, column=j)

# Add polish
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=10, pady=10)


root.mainloop()