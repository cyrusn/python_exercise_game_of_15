class Game:
    """Game store the basic of the game"""

    def __init__(self):
        self.board = [[15 - 4 * j - i for i in range(4)] for j in range(4)]
        self.board[3][3] = ''
        self.board[3][1] = 1
        self.board[3][2] = 2
        self.blank_loc = [3, 3]
        self.counter = 0
        self.goal = [[i + 4 * j + 1 for i in range(4)] for j in range(4)]
        self.goal[3][3] = ''
