# ============================================================================ #
# MORE CONTAINERS

# ============================================================================ #
# TUPLE : tuple
# For dictionaries the "literal" is regular brackets.
empty_tuple = ()
tuple_with_values = (1, 2, 3)

# Tuples are just like lists, except they are "immutable", which means that once
# a tuple is created it cannot be modified. There are no methods for adding or
# removing values, and the setitem syntax will raise an error.
first = tuple_with_values[0]  # 1 <- Value at the first index
tuple_with_values[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Be careful if trying to create a tuple with only one value. Brackets around a
# single value or operation just tell python to calculate the value first (The
# B in BOMDAS for order of operations). To explicitly make it a tuple, add a
# comma before the last bracket
single_value_tuple = (5,)  # <- Tuple
number_5 = (5)  # <- Just the number 5

# ============================================================================ #
# DICTIONARY : dict
# For dictionaries the "literal" is curly brackets.
empty_dictionary = {}

# Dictionaries are like lists, except instead of using an ordered "index" to
# position values, they can use any "immutable" (more on that later) value such
# as strings, integers, floats, or even custom types. The value used for the
# "position" is called the "key", while the value it finds is called the "value"
# This dictionary uses the string "key" as the key, "mapped" to the string "value"
example_dictionary = {"key": "value"}
multiple_dictionary = {"a": 1, "b": 2, "c": 3}

# getitem and setitem work the same as for a list, but using the "key" instead
# of the "index"
print(example_dictionary["key"])  # "value" <- Looked up the value under "key"
example_dictionary["key"] = "a new value"  # <- changed the value under "key"
print(example_dictionary["key"])  # "a new value"
# Using a "key" that doesn't exist will raise a KeyError and stop the script
print(example_dictionary["cat"])  # KeyError: 'cat'

# With lists there is a guarantee that every index number under it's "length"
# has a value (eg, [1, 2, 3] has length of 3, and indexes 0, 1, 2), but
# dictionaries don't have that because their "keys" can be anything.
# There is a "method" called "get()" which acts like getitem, but will return
# None instead of raising a KeyError if the key doesn't exist.
example_dictionary.get("cat")  # None <- Tried to get key "cat", but didn't exist

# ADDING / REMOVING
# To add a new "key value pair", use the setitem syntax
modify_dictionary = {}
modify_dictionary["python"] = "fun!"  # <- adds key "python" and value "fun!"
print(modify_dictionary)  # {"python": "fun!"}
# Because the key is used for the position, it's not possible to have two of the
# same key - trying to add a duplicate will replace the original. Keys are unique
# To remove a "key value pair", use the "pop()" method with the name of the key,
# which returns the value that the key was mapped to.
modify_dictionary.pop("python")  # "fun!" <- removes the key "python" and returns it's value
print(modify_dictionary)  # {}
# pop() will raise a KeyError if it doesn't exist

# To check whether a dictionary has a key first, use a conditional with the
# keyword "in" as the comparison operator which will compare against all keys
# (but not the values!)
my_dict = {"cat": "dog"}
if "cat" in my_dict:  # True <- The key is in the dictionary
    print(my_dict["cat"])
if "dog" in my_dict:  # False <- The key is not in the dictionary
    print(my_dict["dog"])

# ============================================================================ #
# SET : set
# There is no "literal" for EMPTY sets, they must be created by using their "type"
# Any builtin type can be initialised as a value by "calling" it's type, ie,
# using parentheses after the name of the type - this creates the "non-truthy"
# value of the type. Always use literals where possible as they're much faster.
empty_int = int()  # 0
empty_string = str()  # ""
empty_list = list()  # []
empty_dictionary = dict()  # {}
empty_set = set()  # An empty set

# There IS a literal for sets with values. It reuses the curly brackets, but
# unlike dictionaries, there are only values so the : symbol is not used
set_of_values = {1, 2, 3}

# Sets store only unique values - it's not possible to have the same value twice
# Trying to add a duplicate value does nothing
unique = {1, 1, 1, 1}
print(unique)  # {1} <- The value 1 only appears once, the rest were discarded

# Sets are unordered, meaning they don't have any indexes or keys. It is not
# possible to access individual values in a set, so why do they exist?
# Sets have methods for comparing two sets and returning unique elements, like a
# Venn diagram
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
A.intersection(B)  # {3, 4} <- Overlapping values between A and B
A.difference(B)  # {1, 2} <- Values in A but not in B
A.union(B)  # {1, 2, 3, 4, 5, 6} <- Values in both A and B, unique elements only
A.symmetric_difference(B)  # {1, 2, 5, 6} <- Values in A or B but not both

# ============================================================================ #
# CASTING TYPES

# Just like basic types could be cast between types, eg, int("8") -> 8, so can
# the container types. Here are some examples:
a_list = ["duck", "duck", "goose"]
a_tuple = (True, False, True)
a_dict = {"one": 1, "two": 2, "three": 3}
a_set = {1, 2, 3}

list(a_tuple)  # [True, False, True]  <- same values, but now a "mutable" list
list(a_dict)  # ["one", "two", "three"]  <- Only takes the keys from the dict
list(a_set)  # [1, 2, 3]  <- same values, but now as a list and can be indexed

tuple(a_list)  # ("duck", "duck", "goose")  <- same values, but now "immutable"
tuple(a_dict)  # ("one", "two", "three")  <- Only takes the keys from the dict
tuple(a_set)  # (1, 2, 3)  <- same values, but now as a list and can be indexed

dict(a_list)  # TypeError: cannot convert dictionary update sequence element #0 to a sequence
dict(a_tuple)  # TypeError: cannot convert dictionary update sequence element #0 to a sequence
dict(a_set)  # TypeError: cannot convert dictionary update sequence element #0 to a sequence

set(a_list)  # {"duck", "goose"}  <- converting to a set only keeps unique elements
set(a_tuple)  # {True, False}  <- converting to a set only keeps unique elements
set(a_dict)  # {"one", "two", "three"}  <- Only takes the keys from the dict


# Mutable types include lists, dictionaries, and sets. Tuples are not mutable,
# because they explicitly stop you from modifying them.

# Why does it matter? Only mutable types can be used as keys in dictionaries, or
# in sets. The reason for this is because the values have to be unique - there
# can't be two keys the same in a dictionary, and sets only keep unique values.
# If there were two mutable values in a set/dict, and one was modified so that
# it was the same as the other - the container wouldn't know which to keep!
invalid_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'

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
