from model.game import Game
import tkinter as tk


def isNearby(bl, l):
    """
    bl stand for blank tile location
    l stand for location of pressed tile
    """

    def inRow(bl, l):
        if bl[1] == l[1]:
            return True
        return False

    def inColumn(bl, l):
        if bl[0] == l[0]:
            return True
        return False

    if inColumn(bl, l) and bl[1] == l[1] + 1:
        return "above"
    elif inColumn(bl, l) and bl[1] == l[1] - 1:
        return "below"
    elif inRow(bl, l) and bl[0] == l[0] + 1:
        return "left"
    elif inRow(bl, l) and bl[0] == l[0] - 1:
        return "right"
    else:
        return None


class Controller(Game):
    """docstring for Controller"""

    def __init__(self):
        super(Controller, self).__init__()

    def movable(self, l):
        return isNearby(self.blank_loc, l)

    def move(self, old):
        x = old[0]
        y = old[1]
        nx = self.blank_loc[0]
        ny = self.blank_loc[1]
        dummy = self.board[y][x]
        self.board[y][x] = self.board[ny][nx]
        self.board[ny][nx] = dummy

    def move_down(self):
        if self.blank_loc[1] < 3:
            old = self.blank_loc[:]
            self.blank_loc[1] += 1
            self.move(old)
            self.counter += 1

    def move_right(self):
        if self.blank_loc[0] < 3:
            old = self.blank_loc[:]
            self.blank_loc[0] += 1
            self.move(old)
            self.counter += 1

    def move_up(self):
        if self.blank_loc[1] > 0:
            old = self.blank_loc[:]
            self.blank_loc[1] -= 1
            self.move(old)
            self.counter += 1

    def move_left(self):
        if self.blank_loc[0] > 0:
            old = self.blank_loc[:]
            self.blank_loc[0] -= 1
            self.move(old)
            self.counter += 1


if __name__ == "__main__":
    checkers = [{
        "bl": [1, 2],
        "l": [2, 2],
        "ans": "right"
    }, {
        "bl": [3, 2],
        "l": [3, 1],
        "ans": "above"
    }, {
        "bl": [3, 1],
        "l": [2, 1],
        "ans": "left"
    }, {
        "bl": [1, 2],
        "l": [1, 3],
        "ans": "below"
    }, {
        "bl": [1, 2],
        "l": [2, 3],
        "ans": None
    }]

    for c in checkers:
        print(isNearby(c["bl"], c["l"]), c["ans"])
