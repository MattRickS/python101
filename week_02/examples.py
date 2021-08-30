# ============================================================================ #
# LOOPS
# Loops are a more advanced form of "code flow". We already used conditionals to
# make the interpreter skip some lines, but loops allow the interpreter to go
# back UP the code so that it can re-run some lines.
# Loops will run the same block of code multiple times. This is referred to as
# "iterating" over the code. Each time the block runs is called an "iteration".
# This is ideal when working with containers which contain multiple values.

# ============================================================================ #
# WHILE
# The "while" loop runs as long as a given condition evaluates to True. In fact,
# the syntax for a while is the same as an "if", but using the keyword "while".
# Here's an example and we'll break it down afterwards
value = 3
while value > 0:
    print(value)
    value -= 1

print("Blastoff!")
# The while keyword is followed by any statement that resolves to a boolean,
# just like the conditional statements from week 01. It also ends with a colon,
# and must be followed by an indented block. The difference between this and a
# regular conditional statement is that the block of code will keep running
# until the condition is False. The code runs line by line until it reaches the
# end of the indented block, then it goes back and checks the condition. If the
# condition is still True, it runs from the start of the while block again. If
# the condition is False, it starts running the code from the line after the
# while block.
# If you run the example above, it will print
#   3   <- (3 > 0) is True, so it prints the value and reduces value by 1
#   2   <- (2 > 0) is True, so it prints the value and reduces value by 1
#   1   <- (1 > 0) is True, so it prints the value and reduces value by 1
#   Blastoff!  <- (0 > 0) is False. The block is finished so it leaves the block

# Because it runs every time the condition is True, we have to be careful to
# modify the condition inside the loop, otherwise it will run forever! The
# following is an example of an infinite while loop - the condition is always
# True. If this was run, the script would never finish. Never do this!
while True:
    print("Infinite while loop!")

# ============================================================================ #
# LOOP KEYWORDS : continue, break
# Loops cause the interpreter to change which line of code it's running on, but
# we actually have more control than just that.

# CONTINUE
# The continue keyword can only be used inside a loop, and causes the
# interpreter to skip the current iteration and move on to the next one
i = 5
while i > 0:
    print(i)
    if i == 3:
        i -= 2
        continue
    i -= 1
# The output of the above is:
#   5
#   4
#   3
#   1
# By using a conditional inside the loop, we can check whether the current value
# being iterated over is equal to 3, and if it is, reduce the value by 2 (instead
# of the normal 1) and skip the rest of the lines in the block and move on to the
# next iteration

# BREAK
# The break keyword can only be used inside a loop, and causes the loop to
# immediately end. Any of the remaining values in the loop are skipped.
i = 0
while i < 10:
    i += 1
    if i == 3:
        break
    print(i)
# The output of the above is:
#   0
#   1
#   2
# By using the conditional inside the loop, we can check for some condition and
# finish the loop early. This can be useful if we've found something we're
# looking for and don't want to waste time running code on the rest of the values.


# ============================================================================ #
# CONTAINERS
# Containers are types which can hold multiple values, for example, a list of
# strings.

# ============================================================================ #
# LIST: list
# The number 3 means an integer with a value of 3 - it is a "literal", ie, the
# numeric symbol is explicitly linked with it's type and value. For lists, the
# "literal" symbol is square brackets, one to "open" and one to "close" the list
empty_list = []
# To put values into the list, put them inside the brackets, separated by commas
list_of_ints = [1, 2, 3]
# In python, lists can have any mix of values inside them
mixed_list = [1, "text", 0.0, None, True]
# To find the number of items in a list, use the builtin function len() on the
# list variable
length = len(list_of_ints)  # 3 <- There are 3 values in the list

# INDEXING
# Lists are "ordered", meaning they keep track of each value's position in the
# list. The position of a value is called it's "index", and is the number of it's
# position. However, in programming, counting starts from 0, so the first "index"
# is 0 (not 1!).
# Index:      0  1  2
list_index = [1, 2, 3]
# To get the value at a particular index, use the "getitem" syntax, which is
# done using square brackets after the list, with the index that you want.
first_item = list_index[0]  # 1 <- 0 is the first index, and the first value is 1
third_item = list_index[2]  # 3
# It's also possible to use negative indexes to go backwards, where -1 is the
# last index in a list
last_item = list_index[-1]  # 3 <- -1 is the last index, and the last value is 3
second_last_item = list_index[-2]  # 2
# Using an index that doesn't exist will raise an IndexError and stop the script
nothing = list_index[100]  # IndexError: list index out of range
# If you're unsure whether an index exists, compare against the length
index_we_want = 10
if index_we_want < len(list_index):
    print(list_index[index_we_want])

# To change the value in the list, use the "setitem" syntax, which is the same
# as "getitem" but followed by the assignment operator
list_index[0] = 5  # <- Sets the first index (0) to the value 5
print(list_index)  # [5, 2, 3]  <- The list has been modified
# As before, negative indexes also work
list_index[-1] = 6
print(list_index)  # [5, 2, 6]

# ADDING / REMOVING VALUES
# To add a new value after a list is created, use "methods". Methods are
# functions (like len() above) which are part of the "object", ie, the value.
# "Methods" are accessed using a "." symbol between the value and the method.
# One such method is "append()" which adds a value to the end of the list
short_list = [6, 7]
print(short_list)  # [6, 7]
short_list.append(8)  # <- Adds the value 8 to the end of the list
print(short_list)  # [6, 7, 8]

# To add a new value somewhere else in the list, use the "insert()" method. This
# takes two values, the first value is the index to add into, the second is the
# value to add. Notice how all the values afterwards have moved up one index
short_list.insert(0, 5)
print(short_list)  # [5, 6, 7, 8]

# There are two ways to remove a value
# 1. Remove by index - this also returns the value it removed
short_list.pop(0)  # 5 <- The value at the first index was removed, which was 5
print(short_list)  # [6, 7, 8]
# Using an in index that doesn't exist will raise an IndexError just like getitem
# 2. Remove by value - this will only remove the first instance of the value
short_list.remove(8)
print(short_list)  # [6, 7]
# If using "remove()" but the value to be removed isn't in the list, this will
# raise a ValueError that breaks the program
short_list.remove(100)  # ValueError: list.remove(x): x not in list

# There are many more methods on lists that are very useful. Try some out!

# ============================================================================ #
# STRINGS

# You may not have realised it, but strings are containers too! They represent a
# container of individual characters. Because of this, you can use the getitem
# operator on strings too
string = "hello"
print(string[0])  # "h"

# setitem is not allowed because strings are "immutable"

# ============================================================================ #
# SLICING

# Slicing is taking a series of values from a container in one go using the
# getitem operator. To do this, you define a "range" of indexes to take.
string = "Hello, World!"
print(string[0])  # "H" <- Regular getitem only gets one value
print(string[0:5])  # "Hello" <- START:END indexes separated by a colon
# Note, the range of indexes does not include the END index, it stops 1 before

# If you don't define the start index, it will take from the beginning of the
# container
print(string[:5])  # "Hello"

# If you don't define the end index, it will take until the end of the container
print(string[7:])  # "World!"

# If you don't define either, it will take every value in the container - which
# is one way to copy the list. This is a good way to avoid "mutability" errors
print(string[:])  # "Hello, World!"

# Slicing will work on any container that uses indexes, such as list, tuple, string
full_list = [10, 20, 30, 40, 50, 60]
sliced_list = full_list[2:4]  # [30, 40]

# It's also possible to only take every Nth item in a container using the format
# [START:END:STEP] where STEP is how many indexes to skip between items
# For example, to take every second item in a list, we can skip the start index
# so that it starts at the first item, and skip the end index so that it goes to
# the end, but add an extra step of 2
print(full_list[::2])  # [10, 30, 50]

# ============================================================================ #
# MUTABILITY

# Mutability refers to whether or not a value can be modified after it's created
# For example, none of the basic types can be modified
a = 1
a = 2
# It may look like we've modified it, but we've only changed which value the
# variable "a" points to - The value 1 still means 1.

# Some containers can be edited though, because we're changing PART of the value
mutable = [1, 2, 3]
mutable[0] = 10
print(mutable)  # [10, 2, 3]
# The variable "mutable" is still pointing to the same list, but the list has
# changed (or "mutated", hence the name).

# ============================================================================ #
# SHARED REFERENCES

# When an object is mutable, it's possible for editing one variable to affect
# another. For example, if we point a variable to a list that's in another
# variable, they both point to the same list. Modifying either one will mean
# both are being modified.
my_list = [1, 2, 3]
another_list = my_list
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
print(another_list)  # [1, 2, 3, 4]

# If we want to take a copy of the list, we must use either a full slice or
# copy method, eg:
list_a = my_list[:]  # Slice of every value
list_b = my_list.copy()  # Copy of the list


# ============================================================================ #
# FOR LOOP

# The "for" loop runs once for every item in a container. It also sets a variable
# to the value of the current container item each time the loop runs, ie, the
# first time it runs it sets the variable to the first value in the container,
# the second time it runs it sets the variable to the second value, etc...
# The syntax for the "for" loop is:
#   for {variable} in {container}:
#       {block of code}
# You can use any variable name for {variable}, it is created and assigned as
# part of the loop, ie, you don't need the assignment operator (=) at all.
numbers = [1, 2, 3]
for num in numbers:
    print(num)

# The "for" loop above is effectively the same as running the following:
num = numbers[0]
print(num)
num = numbers[1]
print(num)
num = numbers[2]
print(num)

# The difference is that the "for" loop will work on every value, no matter how
# big the list is! This is great when you have a list but don't know how many
# values are in it.

# The "for" loop will work on all containers. Lists and tuples will work as you
# would expect, taking each value in order.
a_list = [1, 2, 3]
for i in a_list:
    print(i)

# Sets however are unordered, meaning the order of the values you get back might
# not be the same as the order they were put in - if order is expected, it
# should be cast to a list and sorted first
a_set = {1, 2, 3}
for i in a_set:  # Could be any order
    print(i)
for i in sorted(a_set):  # Reliable sorted order!
    print(i)

# By default, using a "for" loop on a dictionary will loop over the keys. Just
# like sets, the order is not guaranteed!
a_dict = {"a": 1, "b": 2, "c": 3}
for key in a_dict:  # Some order of "a", "b", "c"
    print(key)
# To loop over the values, use the .values() method. This is also unordered.
for value in a_dict.values():  # Some order of 1, 2, 3
    print(value)
# To loop over both together, use the .items() method. This requires defining
# two variables are part of the loop, one for the key and one for the value.
for key, value in a_dict.items():  # Some order of "a"=1, "b"=2, "c"=3
    print(key, "=", value)
