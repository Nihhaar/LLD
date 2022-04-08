class Connect4Game:
    PIECES = ['X', 'Y']
    WINNING_MOVES = 4

    def __init__(self, w, h, next_player=0) -> None:
        self.w = w
        self.h = h
        self.board = [["O" for _ in range(w)] for _ in range(h)]
        self.next_player = next_player
        self.moves = 0
        self.last_move = None
        self.winning_player = None
        self.show_board()

    def show_board(self, won=False):
        print("Move number: ", self.moves)
        if not won:
            print("Player to make a move: Player", self.next_player + 1)
        else:
            print(f"Player {self.winning_player + 1} won!!!")
        print("------------------")
        for row in self.board:
            print("  ".join(row))
        print("------------------")
        print()

    @property
    def is_full(self):
        return self.moves >= self.w * self.h

    def make_move(self, col):
        piece = self.PIECES[self.next_player]
        if col <= 0 or col > w:
            raise ValueError(f"Invalid col: ({col})")

        for i in range(self.h-1, -1, -1):
            if self.board[i][col-1] == 'O':
                self.board[i][col-1] = piece
                self.last_move = (i, col-1)
                break
        else:
            if self.is_full:
                self.show_board()
                print("Draw")
                exit()
            raise ValueError(f"Column is already filled: ({col})")

        won = self.is_winning_move()
        if won:
            self.winning_player = self.next_player
            self.show_board(True)
            exit()
        else:
            self.next_player = (self.next_player + 1) % 2
            self.moves += 1
            self.show_board()

    def __check_vertical(self):
        count, row, col = 0, self.last_move[0], self.last_move[1]
        curr_piece = self.board[row][col]
        while row < self.h and self.board[row][col] == curr_piece:
            count += 1
            row += 1
        return count >= self.WINNING_MOVES

    def __check_horizontal(self):
        row, col = self.last_move[0], self.last_move[1]
        curr_piece = self.board[row][col]

        count = -1
        for direction in [1, -1]:
            icol = col
            while icol >= 0 and icol < self.w and self.board[row][icol] == curr_piece:
                count += 1
                icol += direction

        return count >= self.WINNING_MOVES

    def __check_diagonal(self):
        count, row, col = 0, self.last_move[0], self.last_move[1]
        curr_piece = self.board[row][col]

        for slope in [1, -1]:
            count = -1
            for direction in [1, -1]:
                irow = row
                icol = col
                while irow >= 0 and irow < self.h and icol >= 0 and icol < self.w and self.board[irow][icol] == curr_piece:
                    count += 1
                    icol += direction * slope
                    irow -= direction * slope
            if count >= self.WINNING_MOVES:
                return True

        return False

    def is_winning_move(self):
        if not self.last_move:
            return False

        return self.__check_vertical() or self.__check_horizontal() or self.__check_diagonal()

    def get_next_player(self):
        return self.next_player + 1


def play_ai(width):
    from random import randrange
    while True:
        try:
            col = randrange(width) + 1
            connect4.make_move(col)
        except Exception as e:
            print(e)
            connect4.show_board()
            print("Invalid column, please try again...")
            continue


def play_manual():
    while True:
        col = input(f"Player {connect4.get_next_player()} move (column): ")
        try:
            col = int(col)
            connect4.make_move(col)
        except Exception as e:
            print(e)
            print("Invalid column, please try again...")
            continue


if __name__ == "__main__":
    w, h = 6, 8
    connect4 = Connect4Game(w, h)
    play_manual()

