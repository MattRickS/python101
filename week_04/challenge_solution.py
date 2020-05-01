import random

EMPTY = "~"
SHIP = "^"
HIT = "X"
MISS = "O"


def add_random_ship(board):
    # Collect all positions that are empty - use the index of the row and column
    choices = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                choices.append((i, j))

    # If there are no empty positions, there's nothing we can do!
    if not choices:
        return False

    # Use random to pick one of the positions for us. Because we used a tuple of
    # two values, we know we can unpack into two variables
    row, col = random.choice(choices)
    board[row][col] = SHIP
    return True


def print_grid(board):
    for row in board:
        # LIST COMPREHENSION would be simpler
        hidden_row = []
        for value in row:
            if value == SHIP:
                hidden_row.append(EMPTY)
            else:
                hidden_row.append(value)
        print(" ".join(hidden_row))


def get_user_guess():
    row = int(input("Enter a row: ")) - 1
    col = int(input("Enter a column: ")) - 1
    return row, col


def is_valid_guess(board, row, col):
    if not 0 <= row < len(board) or not 0 <= col < len(board[0]):
        print("Your guess is off the grid! Try again")
        return False

    value = board[row][col]
    if value == HIT or value == MISS:
        print("You've already guessed that")
        return False

    return True


def generate_grid(rows, columns):
    # LIST COMPREHENSION would be simpler
    grid = []
    for row in range(rows):
        row_values = []
        for col in range(columns):
            row_values.append(EMPTY)
        grid.append(row_values)
    return grid


def battleship(num_ships=2, rows=3, columns=3):
    grid = generate_grid(rows, columns)

    # Calling the function to add a ship to the grid at a random location
    for i in range(num_ships):
        add_random_ship(grid)

    while True:
        print_grid(grid)
        row, col = get_user_guess()

        if not is_valid_guess(grid, row, col):
            continue
        elif grid[row][col] == SHIP:
            grid[row][col] = HIT
            num_ships -= 1
            if num_ships <= 0:
                print_grid(grid)
                print("You won!")
                break
            else:
                print("You sunk my battleship! {} ship(s) remain".format(num_ships))
        else:
            grid[row][col] = MISS
            print("You missed!")


def run():
    while True:
        battleship()

        response = input("Play again? y/n")
        if response != "y":
            break


if __name__ == '__main__':
    run()
