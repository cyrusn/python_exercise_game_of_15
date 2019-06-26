class Game:
    def __init__(self):
        self.reset()
        self.board = [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 1, 2, 0]]
        self.goal = [[i + 4 * j + 1 for i in range(4)] for j in range(4)]
        self.goal[3][3] = 0
        self.counter = 0

    def _swap(self, nx=None, ny=None):
        nx = self.x if nx is None else nx
        ny = self.y if ny is None else ny
        x = self.x
        y = self.y
        self.board[y][x], self.board[ny][nx] = self.board[ny][nx], self.board[y][x]
        self.counter += 1
        self.check_win()

    def move_up(self):
        if self.y < 3:
            self._swap(ny=self.y + 1)
            self.y += 1

    def move_down(self):
        if self.y > 0:
            self._swap(ny=self.y - 1)
            self.y -= 1

    def move_left(self):
        if self.x < 3:
            self._swap(nx=self.x + 1)
            self.x += 1

    def move_right(self):
        if self.x > 0:
            self._swap(nx=self.x - 1)
            self.x -= 1

    def check_win(self):
        if self.board == self.goal:
            self.win = True

    def reset(self):
        self.board = [[15 - 4 * j - i for i in range(4)] for j in range(4)]
        self.board[3][1], self.board[3][2] = self.board[3][2], self.board[3][1]
        self.x = 3
        self.y = 3
        self.counter = 0
        self.win = False

    def printBoard(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    print("    ", end="")
                else:
                    print("{:3d}".format(cell), end=" ")
            print()

    def printStep(self):
        print("\nStep: {:3d}".format(game.counter))


if __name__ == "__main__":
    game = Game()

    while True:
        game.printBoard()
        command = input("Give me direct: ")

        if command == "s":
            game.move_down()
        elif command == "w":
            game.move_up()
        elif command == "d":
            game.move_right()
        elif command == "a":
            game.move_left()
        elif command == "r":
            game.reset()
        elif command == "q":
            exit()

        game.printStep()
        game.check_win()

        if game.win:
            print("You win\n")
            exit()
