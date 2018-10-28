#!/usr/local/bin/python3

from tkinter import Tk, Frame, Label, CENTER, font
from game import Game


class App:
    # LABEL_WIDTH and LABEL_HEIGHT is in characters (not in pixels)
    LABEL_WIDTH = 4
    LABEL_HEIGHT = 2
    GRID_LEN = 4
    GRID_PADDING = 8
    FONT_SIZE = 40
    FONT = ("Verdana", FONT_SIZE, "bold")

    BACKGROUND_COLOR_GAME = "#91959B"
    BACKGROUND_COLOR_CELL = "#FFFFFF"
    FONT_COLOR = "#282C34"

    KEY_QUIT = "q"
    KEY_RESET = "r"
    KEY_UP = "Up"
    KEY_DOWN = "Down"
    KEY_RIGHT = "Right"
    KEY_LEFT = "Left"

    def __init__(self, font=FONT):
        super(App, self).__init__()
        self.font = font
        self.Tk = Tk()
        self.game = Game()
        self.commands = {
            App.KEY_QUIT: self.Tk.quit,
            App.KEY_RESET: self.game.reset,
            App.KEY_UP: self.game.move_up,
            App.KEY_DOWN: self.game.move_down,
            App.KEY_RIGHT: self.game.move_right,
            App.KEY_LEFT: self.game.move_left,
        }
        self.grid_cells = []
        self.init_grid()
        self.init_counter_label()
        self.update_grid()

        self.window_appearance_setting()
        self.register_key_event()

    def run(self):
        self.Tk.mainloop()

    def register_key_event(self):
        self.Tk.bind("<Key>", self.handle_key)

    def handle_key(self, e):
        if e.char in self.commands:
            self.commands[e.char]()

        if not self.game.win and e.keysym in self.commands:
            self.commands[e.keysym]()
            self.update_grid()

    def init_counter_label(self):
        label_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.label = Label(master=self.Tk, font=label_font)
        self.label.grid()

    def init_grid(self):
        background = Frame(master=self.Tk, bg=App.BACKGROUND_COLOR_GAME)
        background.grid()

        for row in range(App.GRID_LEN):
            row_cells = []
            for col in range(App.GRID_LEN):
                cell = Label(
                    master=background,
                    text="",
                    bg=App.BACKGROUND_COLOR_CELL,
                    justify=CENTER,
                    font=self.font,
                    width=App.LABEL_WIDTH,
                    height=App.LABEL_HEIGHT,
                )
                cell.grid(
                    column=col, row=row, padx=App.GRID_PADDING, pady=App.GRID_PADDING
                )

                row_cells.append(cell)
            self.grid_cells.append(row_cells)

    def update_grid(self):
        for i in range(App.GRID_LEN):
            for j in range(App.GRID_LEN):
                cell_value = self.game.board[j][i]
                self.grid_cells[j][i].configure(
                    text="{}".format(cell_value if cell_value != 0 else ""),
                    fg=App.FONT_COLOR,
                )
        if self.game.win:
            self.label.configure(
                text="You win, total steps: {}".format(self.game.counter)
            )
        else:
            self.label.configure(text="Step: {}".format(self.game.counter))

    def window_appearance_setting(self):
        self.Tk.title("Game of 15")
        self.Tk.lift()
        self.Tk.attributes("-topmost", True)


if __name__ == "__main__":
    App().run()
