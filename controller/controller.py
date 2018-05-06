from model.game import Game
from tkinter import messagebox
from .isNearBy import *


class Controller(Game):

    def __init__(self):
        super(Controller, self).__init__()
        self.win = False

    def movable(self, l):
        if self.win != True:
            return isNearBy(self.blank_loc, l)

    def move(self, old):
        x = old[0]
        y = old[1]
        nx = self.blank_loc[0]
        ny = self.blank_loc[1]
        dummy = self.board[y][x]
        self.board[y][x] = self.board[ny][nx]
        self.board[ny][nx] = dummy

        if self.board == self.goal:
            self.win = True

            messagebox.showinfo(
                "Congratulation!",
                "You finished the puzzle with {} steps".format(self.counter)
            )

    def move_down(self):
        if self.blank_loc[1] < 3:
            old = self.blank_loc[:]
            self.blank_loc[1] += 1
            self.counter += 1
            self.move(old)

    def move_right(self):
        if self.blank_loc[0] < 3:
            old = self.blank_loc[:]
            self.blank_loc[0] += 1
            self.counter += 1
            self.move(old)

    def move_up(self):
        if self.blank_loc[1] > 0:
            old = self.blank_loc[:]
            self.blank_loc[1] -= 1
            self.counter += 1
            self.move(old)

    def move_left(self):
        if self.blank_loc[0] > 0:
            old = self.blank_loc[:]
            self.blank_loc[0] -= 1
            self.counter += 1
            self.move(old)
