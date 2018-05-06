class Game:
    """Game store the basic of the game"""

    def __init__(self):
        self.board = [
            [15, 14, 13, 12],
            [11, 10, 9, 8],
            [7, 6, 5, 4],
            [3, 1, 2, "  "],
        ]
        self.blank_loc = [3, 3]
        self.counter = 0
