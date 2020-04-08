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
len(list_of_ints)  # 3 <- There are 3 values in the list

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

# Mutable types include lists, dictionaries, and sets. Tuples are not mutable,
# because they explicitly stop you from modifying them.

# Why does it matter? Only mutable types can be used as keys in dictionaries, or
# in sets. The reason for this is because the values have to be unique - there
# can't be two keys the same in a dictionary, and sets only keep unique values.
# If there were two mutable values in a set/dict, and one was modified so that
# it was the same as the other - the container wouldn't know which to keep!
invalid_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'
