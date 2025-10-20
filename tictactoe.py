class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        print("\n  0   1   2")
        for i, row in enumerate(self.grid):
            print(f"{i} " + " | ".join(row))
            if i < 2:
                print("  ---------")

    def update(self, row, col, symbol):
        if self.grid[row][col] == ' ':
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self, symbol):
        # Rows, columns, diagonals
        for i in range(3):
            if all(self.grid[i][j] == symbol for j in range(3)) or \
               all(self.grid[j][i] == symbol for j in range(3)):
                return True
        if all(self.grid[i][i] == symbol for i in range(3)) or \
           all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.grid for cell in row)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [
            Player(input("Enter name for Player 1 (X): "), 'X'),
            Player(input("Enter name for Player 2 (O): "), 'O')
        ]
        self.current = 0

    def switch_turn(self):
        self.current = 1 - self.current

    def play(self):
        print("\n🎮 Starting Tic Tac Toe!")
        self.board.display()

        while True:
            player = self.players[self.current]
            print(f"\n{player.name}'s turn ({player.symbol})")
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
            except ValueError:
                print("Invalid input. Try again.")
                continue

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Out of bounds. Try again.")
                continue

            if self.board.update(row, col, player.symbol):
                self.board.display()
                if self.board.check_winner(player.symbol):
                    print(f"\n🏆 {player.name} wins!")
                    break
                elif self.board.is_full():
                    print("\n🤝 It's a draw!")
                    break
                else:
                    self.switch_turn()
            else:
                print("Cell already taken. Try again.")


if __name__ == "__main__":
    Game().play()
