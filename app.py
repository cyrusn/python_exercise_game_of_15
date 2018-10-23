from tkinter import Tk, Frame, Label, CENTER, font
from game import Game

SIZE = 500
GRID_LEN = 4
GRID_PADDING = 10
BACKGROUND_COLOR_GAME = "#91959B"
BACKGROUND_COLOR_CELL = "#FFFFFF"
FONT_COLOR = '#282C34'
FONT = ("Verdana", 40, "bold")

KEY_QUIT = 'q'
KEY_RESET = 'r'
KEY_UP = 'Up'
KEY_DOWN = 'Down'
KEY_RIGHT = 'Right'
KEY_LEFT = 'Left'


class App(Frame):

    def __init__(self, master):
        super(App, self).__init__()
        self.pack()
        self.master = master
        self.game = Game()
        self.commands = {
            KEY_QUIT: self.quit,
            KEY_RESET: self.game.reset,
            KEY_UP: self.game.move_up,
            KEY_DOWN: self.game.move_down,
            KEY_RIGHT: self.game.move_right,
            KEY_LEFT: self.game.move_left
        }
        self.grid_cells = []
        self.init_grid()
        self.init_counter_label()
        self.update_grid()

        self.window_appearence_setting()
        self.create_key_event()

    def create_key_event(self):
        self.master.bind("<Key>", self.listen_key)

    def listen_key(self, e):
        if e.char in self.commands:
            self.commands[e.char]()

        if not self.game.win and e.keysym in self.commands:
            self.commands[e.keysym]()
            self.update_grid()

    def init_counter_label(self):
        label_font = font.Font(family='Helvetica', size=24, weight='bold')
        self.label = Label(
            self,
            font=label_font
        )
        self.label.grid()

    def init_grid(self):
        background = Frame(
            self,
            bg=BACKGROUND_COLOR_GAME,
            width=SIZE,
            height=SIZE
        )
        background.grid()

        for row in range(GRID_LEN):
            row_cells = []
            for col in range(GRID_LEN):
                cell = Label(
                    master=background,
                    width=SIZE//GRID_LEN,
                    height=SIZE//GRID_LEN
                )
                cell.grid(
                    column=col,
                    row=row,
                    padx=GRID_PADDING,
                    pady=GRID_PADDING
                )
                t = Label(
                    master=cell,
                    text='',
                    bg=BACKGROUND_COLOR_CELL,
                    justify=CENTER,
                    font=FONT,
                    width=4, height=2
                )
                t.grid()
                row_cells.append(t)
            self.grid_cells.append(row_cells)

    def update_grid(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                cell_value = self.game.board[j][i]
                self.grid_cells[j][i].configure(
                    text="{}".format(
                        cell_value if cell_value != 0 else ''
                    ),
                    fg=FONT_COLOR
                )
        if self.game.win:
            self.label.configure(
                text='You win, total steps: {}'.format(self.game.counter))
        else:
            self.label.configure(text='Step: {}'.format(self.game.counter))

    def window_appearence_setting(self):
        self.master.title("Game of 15")
        self.master.lift()
        self.master.attributes('-topmost', True)


root = Tk()
app = App(root)
root.mainloop()
