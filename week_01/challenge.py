# "import" is a special keyword that brings in code from somewhere else. This
# adds a "Module" called random, which has "functions" for picking random values
import random

# This will generate a random value between 1 and 10 (inclusive)
answer = random.randrange(1, 10)

# TODO: Ask the user for some input, then check if the user's value matches the
# answer. If they guessed correctly, print out "Correct!". If they guessed too
# high, print out "Too high". If they guessed too low, print out "Too low".
# Whatever the result, always finish by printing out "The answer was X"
# (replacing X with the answer).
# Hints:
# * Remember that the "type" returned by user input is always str
# * You can temporarily replace the randomly generated number with a fixed value
#   if you need to test if something is working, eg, answer = 4
# * Test your code by running "python challenge.py" (without quotes) in the
#   terminal from the same directory as this file. Your IDE might also have
#   other ways of running the code.
