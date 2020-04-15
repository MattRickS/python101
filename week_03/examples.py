# ============================================================================ #
# LOOPS
# Loops are a more advanced form of "code flow". We already used conditionals to
# make the interpreter skip some lines, but loops allow the interpreter to go
# back UP the code so that it can re-run some lines.
# Loops will run the same block of code multiple times. This is referred to as
# "iterating" over the code. Each time the block runs is called an "iteration".
# This is ideal when working with containers which contain multiple values.
# There are two types of loop: "while" and "for".

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
# FOR
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
num = my_list[0]
print(num)
num = my_list[1]
print(num)
num = my_list[2]
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


# ============================================================================ #
# LOOP KEYWORDS : continue, break
# Loops cause the interpreter to change which line of code it's running on, but
# we actually have more control than just that.

# CONTINUE
# The continue keyword can only be used inside a loop, and causes the
# interpreter to skip the current iteration and move on to the next one
for i in [0, 1, 2, 3, 4]:
    if i == 2:
        continue
    print(i)
# The output of the above is:
#   0
#   1
#   3
#   4
# By using a conditional inside the loop, we can check whether the current value
# being iterated over is equal to 2, and if it is, skip the rest of the lines in
# the block and move on to the next iteration

# BREAK
# The break keyword can only be used inside a loop, and causes the loop to
# immediately end. Any of the remaining values in the loop are skipped.
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
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
# BUILTIN LOOP UTILITIES : range, enumerate, zip

# RANGE
# Sometimes we just want to run the same block of code a certain number of times
# For example, if we wanted to count up to 5 and print out each number. In this
# case, we don't really need a container with the numbers, we just need the
# numbers. There is a builtin function called "range()" which we can use to
# generate a temporary list of numbers by giving it a number to count to.
range(5)  # <- Effectively creates a list of: [0, 1, 2, 3, 4]
# This works really well for "for" loops
for num in range(5):
    print(num)
# This would print out each number from 0-4.

# We don't even have to use the variable from the loop, we can just make some
# code run as many times as the length of our temporary container
for num in range(5):
    print("Hello")
# This would print hello 5 times

# In a way, it's like it's generating a list of numbers for us. Be careful
# though, what it's actually creating is called an "iterator", which is
# something that will work with loops, but doesn't actually store the values.
# It's effectively only calculating each number one at a time whenever the loop
# asks for the next value. This is a bit advanced, so we'll come back to it
# later. For now, you can use range() with "for" loops, or if you want a list of
# numbers, you can cast it like so:
list_of_numbers = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range() can use the same START, STOP, STEP arguments that slicing uses, but
# separates the arguments with a comma instead of a colon. Here's a quick
# refresher:
range(3, 6)  # <- 3, 4, 5    STARTS at 3, STOPS at 6
range(2, 9, 3)  # <- 2, 5, 8   STARTS at 2, STOPS at 9, STEPS 3 values at a time
# Unlike slicing, because we're creating the range from scratch, we can't leave
# any value empty - we have to provide all the ones we need

# ENUMERATE
# "for" loops are useful for quickly using every value in a container without
# having to use it's index to get it. But what if we want to know the index AND
# the value? We could track the index separately and do a lookup, but python
# provides a builtin method to make this easier for us called "enumerate()".
# By calling it on a container it returns both the index and the value, meaning
# we need to use two variable names in our for loop. Note, the index will always
# be the first variable, and the value will be the second.
names = ["Matthew", "Steve", "Laura"]
for index, name in enumerate(names):
    print(index, "=", name)

# This can be very useful if we want to modify the list again. Say we want to
# add 1 to every number in a list - we can modify it easily, but how do we put
# the new value back in the list? We'd need the index!
numbers = [1, 2, 3]
for index, number in enumerate(numbers):
    # Replace the number in the list with a new number
    numbers[index] = number + 1

# ZIP
# Sometimes we have two containers and want to pair off the values inside each,
# for example, if we had a list of students and a list of results from an exam,
# and wanted to pair them together. The builtin "zip()" function takes at least
# two containers (but can take more!) and will return the next value from each
# container together. We'll need a variable for each container we give to zip(),
# and each variable will be filled with the value from the corresponding list,
# ie, in the example below we pass the students container first and then the
# grades container, which means the first variable will be from "students", and
# the second will be from "grades".
students = ["Lucy", "David", "Suzanne", "James"]
grades = [80, 50, 75, 33]
for student, grade in zip(students, grades):
    print(student, "has a score of", grade)


# ============================================================================ #
# NESTED LOOPS
# Now we know that if we want to run a block of code multiple times, we use a
# loop. But what if we want to run the loop multiple times? Use another loop!
# This is quite common with nested containers, an example of which might be an
# image - it's made of pixels organised into rows and columns, which is most
# easily represented by nested containers - this is often referred to as a
# "2D array" ("array" is another term for container that's used a lot in other
# languages). Here's an example of an image, using a single integer for the
# colour of each pixel.
image = [
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
]

# Using a "for" loop on the image will only get each row in the image, ie
for row in image:
    print(row)
# [1, 1, 0]
# [1, 0, 1]
# [0, 1, 1]

# If we wanted to get each pixel, we'd have to use another loop on each row.
for row in image:  # <- Outer loop
    for pixel in row:  # <- Inner loop - runs once for each iteration of the outer loop
        print(pixel)
# Output | Outer Loop | Inner Loop
# 1    <-  First row    First Column
# 1    <-  First row    Second Column
# 0    <-  First row    Third Column
# 1    <-  Second row   First Column
# 0    <-  Second row   Second Column
# 1    <-  Second row   Third Column
# 0    <-  Third row    First Column
# 1    <-  Third row    Second Column
# 1    <-  Third row    Third Column

# Notice how the outer loop (ie, the first one we wrote) stays the same until
# the inner loop has finished running. The Inner loop is also doing the same
# behaviour - a repeated pattern of first, second, and third column. This is
# because it runs through the row until it runs out, and then the outer loop
# gives it the next row to work on.
