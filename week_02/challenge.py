# Loads the "to do" list from a file
filename = "mytodo.txt"
try:
    with open(filename, "r") as f:
        data = f.read()
except FileNotFoundError:
    data = ""

if data:
    todos = data.split("\n")
else:
    todos = []

# ---------------------------------------------------------------------------
# TODO: Write a loop that allows the user to pick from the following options:
# - Add a new todo item to the list
# - List all todo items
# - Save (Use the code snippet below)
# - Quit
# It is up to you how you want the user to select options, some suggestions are
# - Add a number to each option when printing it out, eg, "1. Add a new item" and ask the user to enter a number
# - Use a special letter for each option, identified by adding brackets around it, eg, "[A]dd an item" would use "a"
# The loop should repeat until the user selects "Quit", when the script should end.
# You can add any other options you like.

# Use the following code to save the todos when the user selects the "Save" option:
with open(filename, "w") as f:
    f.write("\n".join(todos))
