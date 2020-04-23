import random

EMPTY = "~"
SHIP = "^"
HIT = "X"
MISS = "O"

grid = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
]


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


# Calling the function to add a ship to the grid at a random location
add_random_ship(grid)

while True:
    # 1. Make this into a print_grid() function that takes a grid as an argument
    #    and prints it out. It should work with any size of grid.
    for row in grid:
        print(" ".join(row))

    # 2. Make this into a get_user_guess() function that returns a tuple of (row, col).
    row = int(input("Enter a row: ")) - 1
    col = int(input("Enter a column: ")) - 1

    # 3. Make an is_valid_guess() function that takes three arguments, grid, row and
    #    column, and checks for the following conditions:
    #      * The positions are on the grid
    #      * The positions were not already guessed
    #    It should return a boolean for whether or not it's valid, and print out any
    #    error messages. For example, if the position was already guessed it should
    #    print something like "You've already guessed that" and return False.

    # 4. Update the conditional to use the is_valid_guess() function
    if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]):
        print("Your guess is off the grid! Try again")
    elif grid[row][col] == SHIP:
        grid[row][col] = HIT
        print("You sunk my battleship!")
        # 5. Print out the grid again so the user can see the result
        break
    else:
        grid[row][col] = MISS
        print("You missed!")

# 6. Put the while loop inside a function called battleship() and call it to run
#    the game. Is there anywhere that you could use "return" to your advantage?

# Things you can do if you want to learn more (and make it more fun!):
# * Hide the ship when printing the board. To do this, you'd need to loop over
#   each value and check whether it's a SHIP, and if it is, use EMPTY instead.
#   Don't modify the grid though or you'll lose your ship!
# * Try adding multiple ships. You'll need to track how many ships are left and
#   only show the win condition if all of the ships are sunk.
# * Ask the user if they want to play again or quit so they don't have to run
#   the script again if they want another game
# * Make the grid size dynamic. It's currently "hardcoded", but you could write
#   a function generate_grid(rows, columns) which creates a new grid for you
