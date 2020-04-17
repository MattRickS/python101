EMPTY = "~"
SHIP = "^"
HIT = "X"
MISS = "O"

grid = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, SHIP, EMPTY],
]

# 1.
# Print out each ROW of the grid

# 2.
# Ask the user to input a ROW number (integer)
# Ask the user to input a COLUMN number (integer)

# 3.
# Check if value at the guessed ROW and COLUMN is the ship value.
# If it is, replace the value with the HIT symbol. Print "You sunk my battleship!"
# If it isn't, replace the value with the MISS symbol. Print "You missed!"

# 4.
# Put the code inside a loop so the user can have multiple guesses. Make sure
# the loop ends if they guess correctly!

# Hints:
# * Don't forget that user input is always a string!
# * What happens if the user makes a guess that's not on the grid? How could you
#   easily make them guess again?
# * Users will think of rows and columns that start counting from 1 - how would
#   you handle that?
# * BONUS: Can you print the row as a string and not a list? Hint: a string
#   method will help...
