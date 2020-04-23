# ============================================================================ #
# FUNCTIONS
# Functions are re-usable blocks of code that are assigned names, and can be
# "called" from anywhere. "Calling" a function makes the interpreter jump from
# to the start of the function, run til it's finished, and then jump back to
# where it was. This is the best way to control "code flow" as you can redirect
# it however you need!


# ============================================================================ #
# SYNTAX
# Functions are "defined" using the keyword "def", followed by the name you want
# to call the function. This name works just like a variable, and has to be
# unique! The name is followed by a pair of regular braces and a colon. As always,
# a colon must be followed by an indented block, and all the indented code
# belongs to the function (ie, it's what will get run).
def my_function():
    print("Inside my function!")


# One important difference is that the code inside a function doesn't get run
# when it's "defined". This means if we ran just the function code above,
# nothing would happen!
# To make the code actually run, we need to "call" the function. This is done by
# using the variable name followed by a pair of regular braces.
my_function()  # <- runs the code in the function - will print "Inside my function!"

# What's great, is that you can now call it as many times as you want! This will
# print the text out three times
my_function()
my_function()
my_function()

# It's important to use the right terms. The line with "def" is where we "define"
# the function, but whenever it's used afterwards it's "calling" the function.


# ============================================================================ #
# RETURN VALUES
# Functions not only run the code, but can "return" a value, meaning, they can
# send a value back to wherever called the function. To do this, we use the
# "return" keyword
def make_number():
    return 1


# Whenever a function is called, it will result in a value that can then be used
# like normal - use it in an expression or store it in a variable
number = make_number()  # <- The same as: number = 1


# You may be wondering what happened in the first example function that didn't
# have a return - what value does that give back? The answer is "None". If we
# don't specify a return, it will provide a default value of None for us. The
# same thing happens if we use the return keyword without any value after it.
def no_return():
    print("I don't return anything")

def also_no_return():
    return

result1 = no_return()  # <- None
result2 = also_no_return()  # <- None


# Because return gives a value back to wherever it was called, that means it has
# to finish running the function. If there is any more code after the return, it
# won't get run. This is similar to "break" inside a loop.
def bad_function():
    return 1
    print("This will never get run!")


# You can also have multiple "return" statements in a function. The function
# will end as soon as it hits any return, but you can use code flow to pick the
# return statement to use
def multiple_return():
    if 1 < 5:
        return 1  # <- This will get run first, so the function returns 1
    return 5


# It's also possible to have a default return and an explicit return. In the
# example below, we loop over some values and return the first value that's
# greater than 10. However, we only iterate over values lower than 10, so the
# return state6ment will never be reached. In this case, the code runs out, so
# the function will use the default return of "None"
def default_return():
    for i in range(10):
        if i > 10:
            return i


# ============================================================================ #
# PARAMETERS

# ---------------------------------------------------------------------------- #
# POSITIONAL
# Getting values OUT of a function is good, but it could be better. We could also
# pass values IN to the function. This is possible using "parameters", and is a
# decision we have to make when writing the function. We do this by putting
# variables in the brackets on the line of the function definition.
def some_function(variable):
    print(variable)


# This might raise a few questions: where did that variable come from? We haven't
# defined it yet, so what value does it have? The answer is that it doesn't have
# a value yet, it's part of the function definition, which if you recall, doesn't
# actually run until we call it. That means the variable doesn't have a value
# until we call it, and we provide the value when calling.
some_function(1)  # <- sets variable=1

# Some boring terminology:
# * The variables in the function definition are "parameters"
# * The values we pass to the function are "arguments"

# It's possible to define many parameters in a function:
def add(one, two):
    return one + two

result = add(5, 3)  # <- 8

# The parameters above are "positional", meaning it maps the values we give to
# the variables based on their position, ie, the order that they're given. In
# the example above, we called add() with 5 and 3 in that order, and the
# parameters are defined as "one" and "two", so it maps one=5 and two=3.

# If we don't provide enough values (or provide too many) when calling a
# function, we'll get a TypeError explaining the mistake.
add(1)  # <- TypeError: add() missing 1 required positional argument: 'two'
add(1, 2, 3)  # <- TypeError: add() takes 2 positional arguments but 3 were given

# This makes functions very powerful because we can change the input to get
# different output, but always using the same block of code.

# ---------------------------------------------------------------------------- #
# KEYWORD
# We can also provide parameters with default values by using the assignment
# operator during the function definition. This means we don't have to pass the
# value when calling the function, because if we don't, the variable already has
# a default value. These parameters are referred to as "optional" or "keyword"
# parameters
def keyword_function(default=1):
    print(default)

keyword_function()  # <- prints 1 - we didn't provide a value so it used the default
keyword_function(2)  # <- prints 2 - we provided a value for it to use

# There is a restriction though, keyword parameters have to go AFTER the
# positional parameters. This makes sense if you think about it - all parameters
# have to have a value, and the only way to give a positional value is to give
# it in order. If there was a positional after a keyword, we'd have to provide a
# value for the keyword in order to set the positional
def invalid_function(keyword=1, positional):
    print("This will never work!")

def valid_function(positional, keyword=1):
    print("Positional is:", positional)
    print("Keyword is:", keyword)


# If you have multiple keyword parameters, but want to provide a value for only
# one of them, you can explicitly use the parameter name when calling the function
def many_keywords(one=1, two=2, three=3):
    return one + two + three

# "one" and "two" use their default values, "three" is explicitly set to 10
many_keywords(three=10)

# In case you're wondering, giving a value to a keyword parameter never changes
# the default, it's only used for the time that it's running.
def example_keywords(default=1):
    print(default)

example_keywords(default=5)  # <- Prints 5 as requested
example_keywords()  # <- Prints 1, the default is unchanged despite previous call

# It is possible however to modify a default value if it's mutable. If you recall,
# basic types (int, float, str, bool, None) are immutable, as are tuples, but
# most other types such as containers are mutable. If we use a list as a default,
# and the list is modified, the default value is changed.
def dangerous_function(default=[]):
    default.append(1)
    print(default)

dangerous_function()  # <- prints [1] as we expect
dangerous_function()  # <- prints [1, 1] - the previous call has modified the default!

# Best Practice: Never use a mutable type as a default value!

# ============================================================================ #
# SCOPE
# Every variable we create inside a function belongs to that function, and gets
# cleaned up when the function ends. This works because of "scope". "Scope"
# controls what variables and functions are available at any point in the code.
# There are three levels of scope:
# * builtin: Values that come with python, such as print(), len(), etc...
# * global: Values defined in a module that are available anywhere in the module
# * local: Values defined in a function and are only available in the function

GLOBAL_VARIABLE = 1

def func():
    local_variable = 2
    print("Global variable:", GLOBAL_VARIABLE)
    print("Local variable:", local_variable)

func()
print("Global variable:", GLOBAL_VARIABLE)
print("Local variable:", local_variable)
# The output of the code above is:
# 1
# 2
# 1
# Traceback (most recent call last):
#   File "scope.py", line 10, in <module>
#     print(local_variable)
# NameError: name 'local_variable' is not defined

# The global variable is available everywhere we use it, but the local variable
# only exists inside the function, so when we try to call it outside the function
# we get a NameError.
# Also, notice the convention to use all capital letters for global variables.
# This is to make it easy to know where a variable came from when you see it
# used, and to help avoid "shadowing"

# Best Practice: Use capitals for global variable names

# ---------------------------------------------------------------------------- #
# Shadowing
# Shadowing is when we create a variable in one scope with the same name as a
# variable in a "parent" scope (eg, a local variable matching a global/builtin
# name). When this happens in the same scope, the previous value is completely
# removed, but in a child scope, the previous value is just temporarily hidden
# until the child scope is finished. An example will help explain this:

variable = 10

def shadow_example():
    variable = 20
    print(variable)

shadow_example()
print(variable)
# Output:
# 20
# 10

# Normally, you'd have expected the variable's value to have changed after the
# function, but because the function has it's own scope, a new variable of the
# same name was created inside the function's scope. This means it's impossible
# to access the global variable as it's "hidden" by the local variable.

# Best Practice: Don't re-use variable names.

# ---------------------------------------------------------------------------- #
# Nested Scope / Stack Frames
# Whenever you call a function, the interpreter pauses executing the current
# block of code to run the function. As mentioned, this enters a new "scope",
# and python keeps track of each time a scope is entered by storing a "frame"
# on the "stack". A "frame" is where the scope and all it's variables are stored,
# along with the line number it's running. As each function is called, a frame
# is created and stacked on top of the previous frame, and when the function
# finishes, the interpreter returns to the previous frame (which knows the line
# to continue executing from). This means we can call functions inside functions
# safely, the scope's are kept separate, and the code will always return to where
# it was.

variable = 0

def three():
    variable = 3
    print("Function", variable)

def two():
    variable = 2
    print("Function", variable)
    three()
    print("Function", variable, "finished")

def one():
    variable = 1
    print("Function", variable)
    two()
    print("Function", variable, "finished")

one()
# Output:
# Function 1
# Function 2
# Function 3
# Function 2 finished
# Function 1 finished


# ============================================================================ #
# EXCEPTIONS and TRACEBACKS
# Exceptions are the errors we've seen so far, such as ValueError, TypeError, etc...
# So far, they've always ended our program, but how does that work inside functions?
# Whenever an exception is raised, the current "frame" immediately ends, and the
# error continues up to the previous "frame". This keeps happening until the
# exception reaches the top and python crashes. However, python's able to track
# the "frame" where the exception occurred and all the "frames" that it caused to
# stop. With this information, it's able to produce a traceback, which is a list
# of filepaths, function names, and line numbers that point to the exact location
# where the error happened.

def raises_exception():
    raise ValueError("This is how to raise an exception")

def calls_error():
    raises_exception()

calls_error()
# Traceback (most recent call last):
#   File "D:/Programming/python101/week_04/examples.py", line 315, in <module>
#     calls_error()
#   File "D:/Programming/python101/week_04/examples.py", line 313, in calls_error
#     raises_exception()
#   File "D:/Programming/python101/week_04/examples.py", line 310, in raises_exception
#     raise ValueError("This is how to raise an exception")
# ValueError: This is how to raise an exception

# This is very useful for finding the source of the problem, and if there's one
# thing you learn about programming, it should be: Always include the traceback
# when reporting an error!

# It's possible to stop an exception however. Sometimes this is useful when we
# want to call something but know it might break. The syntax is like this:
try:
    raise ValueError("Some value error")
except:
    print("Caught the value error!")
# This would raise an error, and then immediately catch it so it doesn't cause
# python to crash. However, it's bad practice to let it catch ANY error. Instead,
# we can specify what type of error we want to catch like this:
try:
    raise ValueError("Some value error")
except ValueError:
    print("Caught the value error!")
# This is better because we only expected a ValueError. If a different type of
# error happened, we don't want to ignore it because it means something
# unexpected happened, and code should never do anything unexpected.
try:
    raise IndexError("Unexpected index error")
except ValueError:
    print("Caught the value error!")
# This would still raise an IndexError because we didn't try to catch it.

# One final trick with exceptions is that we can catch the exception (and it's
# error message) using as the "as" keyword and storing it in a variable like so:
try:
    raise ValueError("This is an error message")
except ValueError as exc:
    print(exc)
# Output:
# This is an error message
