from lib.game import Game
import tkinter as tk

# Use Class instead

# http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html
# class Window(tk.Frame)
root = tk.Tk()

game = Game()

root.title("Game of 15")

messageFrame = tk.Frame(root)
messageFrame.pack()

w = tk.Label(messageFrame, text=game.counter)
w.pack()


boardFrame = tk.Frame(root)
boardFrame.pack(side=tk.BOTTOM)

buttonFrame = tk.Frame(root)
buttonFrame.pack(side=tk.BOTTOM)

board = game.board
labels = [[], [], [], []]
for i, row in enumerate(board):
    for j, v in enumerate(row):
        l = tk.Label(
            boardFrame,
            text="{}".format(v),
            borderwidth=1
        )
        l.grid(row=i, column=j, padx=10)
        labels[j].append(l)


def pressMe():
    game.down()
    for i, row in enumerate(board):
        for j, v in enumerate(row):
            labels[j][i].config(text="{}".format(v),)


button = tk.Button(buttonFrame, width=25, text='down', command=pressMe)
button.pack()


root.lift()
root.attributes('-topmost', True)
root.mainloop()


class TileLabel():
    """
    TileLabel store the value and location of a tile
        - loc is the location of this tile
        - value is the number shown in this tile
        - blank_loc is an array to indicate the location of the blank tile
    """

    def __init__(self, value, loc, blank_loc):
        self.value = value
        self.loc = loc


class ButtonFrame(tk.Frame):
    """
    ButtonFrame is the window frame to show the button in board grid,
    where tile is the tile shown in this button frame
    """

    def __init__(self, tile):
        super(ButtonFrame, self).__init__()
        self.tile = tile
        self.pack()
        self.var = tk.StringVar()
        self.var.set(tile.value)
        self.button = tk.Button(self, textvariable=self.var, command=self.move)
        self.button.pack()

    def move(self):
        self.var.set("new value")
        pass
