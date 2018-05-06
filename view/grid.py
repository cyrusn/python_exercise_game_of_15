from view.button import ButtonFrame
import tkinter as tk
import tkinter.font as font


class GridFrame(tk.Frame):
    """docstring for GridFrame"""

    def __init__(self, controller, counterVar):
        super(GridFrame, self).__init__()
        self.controller = controller
        self.counterVar = counterVar
        self.blank_loc = self.controller.blank_loc

        self.board = self.controller.board
        self.pack()
        self.vars = [[tk.StringVar() for _ in range(4)] for _ in range(4)]

        self.UpdateCounterValue()
        self.UpdateBoardTileValues()

        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):

                b = tk.Button(self,
                              textvariable=self.vars[j][i],
                              justify="center",
                              font=('helvetica', 16),
                              # padx=2, pady=2,
                              command=lambda l=[j, i]: self.move(l))
                b.grid(
                    row=i, column=j,
                )

    def move(self, l):
        v = self.controller.movable(l)
        if v == None:
            return

        if v == "above":
            self.controller.move_up()
        elif v == "below":
            self.controller.move_down()
        elif v == "right":
            self.controller.move_right()
        elif v == "left":
            self.controller.move_left()

        self.UpdateBoardTileValues()
        self.UpdateCounterValue()

    def UpdateCounterValue(self):
        self.counterVar.set('Step: {:d}'.format(self.controller.counter))

    def UpdateBoardTileValues(self):
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                self.vars[j][i].set("{:2}".format(tile))
