# Anything following the # symbol is a comment and does not get executed

# ============================================================================ #
# VARIABLES and ASSIGNMENT

# A variable is a placeholder name used to represent a value store in memory.
# The name must be only letters, numbers, and underscores.
# You "store" / "assign" a value in the variable by using the "assignment
# operator", which is a single = symbol.
# The following line stores the number 1 in a variable called "my_variable".
my_variable = 1  # After this line, the word my_variable means 1

# ============================================================================ #
# DATA TYPES : There are 5 basic datatypes. int, float, bool, string, None

# There are two types of numbers: integers and floats
# int: Integers are whole numbers - they have no decimal places
number = 1
# float: Floats are fractional numbers, they always have a decimal point, even
# if the value after it is 0!
decimal = 1.0

# Booleans only have two values, True or False
boolean = True
another_boolean = False

# Strings are anything between quotes. You can use single ' or double " quotes,
# but you have to be consistent!
sentence = "Strings can be sentences"
word = 'word'

# None is a special value / type by itself. It means there is nothing at all
empty = None

# ============================================================================ #
# CASTING TO ANOTHER DATA TYPE

# Can "convert" / "cast" from one type to another using the python "type"
to_number = int("8")  # 8
to_string = str(123)  # "123"
to_float = float(10)  # 10.0
to_bool = bool(18.0)  # True

# All values have "truthiness", ie, whether there is or is not a value. This is
# the result of "casting" to a boolean
bool(1)  # True - 1 has a value
bool(0)  # False - 0 has no value
bool("Anything")  # True - there are values in the string
bool("")  # False - the string is empty
bool(None)  # False - None is always false

# Warning: Casting only works for valid types.
int("a")  # This will cause an error! "a" is not a valid integer.

# ============================================================================ #
# USEFUL BUILT IN FUNCTIONS

# The print function takes a value and outputs it to the terminal
print("Hello, World!")  # Output: Hello, World!
# It can also take in multiple values separated by commas, and will "implicitly"
# "cast" them to strings, then print them all out with spaces between them
print("The value of number is", number)  # Output: The value of number is 1

# The input function takes text to show on the console, and then waits for the
# user to input some text. When they press the enter/return key, the text they
# entered is "returned" from the function, ie, you can "assign" the result of
# the function to a variable
user_input = input("Enter some text: ")
# Note, the "type" returned by input() is ALWAYS a string, even if they entered
# a number

# ============================================================================ #
# ARITHMETIC OPERATORS : Basic mathematical operators, just like a calculator!

# Simple maths can be done using the symbols + - * /
add = 1 + 2  # 3
sub = 5 - 3  # 2
multiply = 10 * 5  # 50
divide = 10 / 4  # 2.5

x = 5
y = x + 1  # 6  <- The variable "x" is just a placeholder for the value 5
z = y - x  # -1  <- The same as 6 - 5

# Slightly more advanced operations
exponent = 2 ** 4  # 16 <- ie, "2 to the power of 4", (2 * 2 * 2 * 2)
floor_divide = 10 // 4  # 2 <- Discards the remainder to return only the integer
modulo = 10 % 3  # 1 <- The remainder after dividing 3 into 10

# Both floats and integers will work, but the result may be different depending
# on which are used.
# If both values are integers, the result will be an integer (except for divide
#   - in python 3 divide will always return a float)
# If either value (or both) is a float, the result will be a float.

# COMPARISON OPERATORS : Boolean operators will always return a boolean value

# The == operator is used to compare if two values are equal
equal_ints = 1 == 1  # True
equal_nums = 1 == 1.0  # True  <- "type" is different, but value is the same
unequal = 1 == "1"  # False <- text and integers are not the same value

greater_than = 5 > 3  # True <- 5 is greater than 3
less_than = 2 < 10  # True <- 2 is less than 10
greater_equals = 4 >= 4  # True <- 4 is greater than or equal to 4
less_equals = 5 <= 3  # False <- 5 is not less than or equal to 3
not_equals_1 = 3 != 5  # True <- 3 does not equal 5
not_equals_2 = 3 != 3  # False <- 3 is equal to 3

# LOGICAL OPERATORS : Combining booleans
both_true = True and True  # True <- Checks if the left AND the right are True
either_true = True or False  # True <- Checks if the left OR right are True
opposite = not True  # False <- Inverts the boolean, so True becomes False

with_values = (10 > 5) and (3 == 3)  # True <- Both statements evaluate to True

# ============================================================================ #
# CONDITIONALS

# Code runs line by line. It can skip lines by using "conditional" checks to
# determine which lines to run. The "if" keyword must be followed by a boolean
# value and a colon (the : symbol) and then by an "indented block".
# An "indented block" is at least one line of code that has 4 spaces between the
# start of it's text and the line before.
# If the boolean value is True, the "indented block" gets run.
# If the boolean value is False, the "indented block" gets skipped.
if True:
    print("Inside the True block")  # This would print

if False:
    print("This will never get run!")  # This line would be skipped

print("This line always runs")  # <- not indented, so will always run

# Obviously, typing in a boolean value means the same result will happen every
# time the code runs as it will always be the same value.
# However you can use any variables, operators, and types to get a boolean value
number = 5
if number == 5:  # 5 == 5, which is True - the indented code will run
    print("The value is 5!")

# In the example above, we set the variable directly before the conditional, so
# it's basically the same in that it will always be True, but if we had more
# complex code happening we might not know what value was stored in "number"

# We can also add another "indented block" to run if the conditional is False.
# To do this, use the keyword "else" followed by a colon after the "if" block.
number = 10
if number == 5:
    print("Number is 5")  # Runs if the "if" statement is True
else:
    print("Number not 5")  # Runs if the "if" statement is False

# This is called "code flow" - we control which lines of code to run

# With the above examples, we can only check one condition. If there are
# multiple conditions, we can use another keyword "elif" (short for "else if")
# which works just like a regular "if" except it can only be used directly after
# an "if". This makes more sense with an example:
number = 10
if number == 5:
    print("The number is 5")
elif number < 5:
    print("The number is less than 5")
else:
    print("The number is greater than 5")

# The advantage of using "elif" instead of multiple "if" statements is that only
# ONE of the "blocks" above can run, even if multiple conditions are True.
