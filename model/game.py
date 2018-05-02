def move(board, old, new):
    x = old[0]
    y = old[1]
    nx = new[0]
    ny = new[1]
    dummy = board[y][x]
    board[y][x] = board[ny][nx]
    board[ny][nx] = dummy


class Game:
    """Game store the basic of the game"""

    def __init__(self):
        self.board = [
            [15, 14, 13, 12],
            [11, 10, 9, 8],
            [7, 6, 5, 4],
            [3, 2, 1, "  "],
        ]
        self.loc = [3, 3]
        self.counter = 0

    def printBoard(self):
        print("Step: {}".format(self.counter))
        for i in self.board:
            for j in i:
                print("{:2} ".format(j), end='')
            print()

    def down(self):
        if self.loc[1] > 0:
            old = self.loc[:]
            self.loc[1] -= 1
            move(self.board, old, self.loc)
            self.counter += 1

    def right(self):
        if self.loc[0] > 0:
            old = self.loc[:]
            self.loc[0] -= 1
            move(self.board, old, self.loc)
            self.counter += 1

    def up(self):
        if self.loc[1] < 3:
            old = self.loc[:]
            self.loc[1] += 1
            move(self.board, old, self.loc)
            self.counter += 1

    def left(self):
        if self.loc[0] < 3:
            old = self.loc[:]
            self.loc[0] += 1
            move(self.board, old, self.loc)
            self.counter += 1
