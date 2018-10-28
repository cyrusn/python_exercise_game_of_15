class Game:
    def __init__(self):
        self.reset()
        self.goal = [[i + 4 * j + 1 for i in range(4)] for j in range(4)]
        self.goal[3][3] = 0

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
            self._swap(ny=self.y+1)
            self.y += 1

    def move_down(self):
        if self.y > 0:
            self._swap(ny=self.y-1)
            self.y -= 1

    def move_left(self):
        if self.x < 3:
            self._swap(nx=self.x+1)
            self.x += 1

    def move_right(self):
        if self.x > 0:
            self._swap(nx=self.x-1)
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
