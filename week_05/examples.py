# ============================================================================ #
# STRING FORMATTING
# It is very common to have to modify strings, either by extracting some values,
# or constructing a new string from other values. This is made a lot easier by
# using various string methods built in to the str type.
a_string = "A sentence, with punctuation!"

# Splits a string into multiple strings by cutting out a given string
a_string.split()  # ['A', 'sentence,', 'with', 'punctuation!']
a_string.split(",")  # ['A sentence', ' with punctuation!']
a_string.split("it")  # ['A sentence, w', 'h punctuation!']

# Removes every instance of a character from the ENDS of the string
a_string.strip("!")  # 'A sentence, with punctuation'
a_string.strip("n")  # 'A sentence, with punctuation!'
"   test  ".strip()  # 'test'

# Replaces every instance of a string with another string
a_string.replace("n", "p")  # 'A septepce, with pupctuatiop!'

# Joins together a list of strings using the source string as a separator
" ".join(["Once", "upon", "a", "time..."])  # 'Once upon a time...'
" = ".join(["one", "1", "1.0"])  # 'one = 1 = 1.0'

# String formatting has it's own special syntax! Curly brackets are replaced using
# arguments given to the method.
# The default behaviour uses positional arguments
"{} {}".format("a", "b")  # 'a b'
# The index of the argument to use can specified inside the brackets
"{1} {0}".format("a", "b")  # 'b a'
"{1} {0} {1}".format("a", "b")  # 'b a b'
# The brackets can be named and take keywords
"{one} {two}".format(one="a", two="b")  # 'a b'
"{one} {two} {one}".format(one="a", two="b")  # 'a b a'
# Formatting automatically casts to string for us
"a = {}".format(1)  # 'a = 1'
# Extra formatting can be done using a : and custom arguments. Here's a common use case:
# 0 = Use the 0 character to pad the value
# 3 = Pad to a minimum of 3 characters
# d = The value is an integer (ie, d for digit)
"{:03d}".format(1)  # 001

# The documentation on string formatting shows a LOT of options in painful detail:
#   https://docs.python.org/2/library/string.html#format-string-syntax
# Here is a much easier to read usage guide that compares the {} syntax against an old
# python formatting style using %. The old style still works, but shouldn't be used as
# it will eventually stop being supported.
#   https://pyformat.info/

# ============================================================================ #
# IMPORTING
# So far we've only written code in one file, but it's possible to write it across
# multiple files, and then use code from one file in another. This is done using
# python's "import" mechanic, which "imports" the code into the file.
import mymodule

# This imported the file "mymodule.py" from the same directory as this examples.py
# Notice that we don't need to give the extension - that's because python can only
# import python files, so the extension is assumed. Providing the extension will
# cause an error. Once the file is imported, we can run code from inside the file
mymodule.myfunction()

# It's as simple as that! However, we need to know how it knew where to find
# "mymodule" just from the import statement above. This is done by using
# "environment variables". This can be a complex topic, so here's the short version:
# 1. Environment variables are like variables that are global to the entire
#    Operating system (eg, Windows) - not just for python!
# 2. Environment variables are like a dictionary that can only map strings to strings
# 3. Your computer sets environment variables when it starts up, and can be modified
# 4. The most common usage is to map a short name to a file/folder on the filesystem.
#    This allows programs to lookup the environment variable value to find resources.
# 5. Multiple values can be stored in one environment variable by separating the values
#    with a particular symbol - which symbol to use is defined by the Operating System.
# 6. A default environment variable is called PATH and is mapped to a lot of folders
# 7. Whenever a command is executed, it searches the folders defined in PATH to find a
#    script with the same name that it can run.
# 8. Python defines another environment variable: PYTHONPATH. This works the same as
#    PATH, but is only used by python. It searches the folders in the variable's value
#    to find modules by the name given to "import".
# 9. "import" will ALSO search the PATH environment variable.

# The example above is able to find "mymodule" because we run this script from the same
# folder, and by default, python adds the current folder to it's list of locations to
# look for scripts (as that's where the current script lives!). If we wanted to import
# from somewhere else, we'd need to make sure the module lived in one of the PYTHONPATH
# or PATH locations

# Python also provides some default locations whenever it starts, which is how we're
# able to find a lot of the "standard libraries"

# ============================================================================ #
# STANDARD LIBRARIES
# Python comes with "batteries included". What this means is, there's a lot of things we
# might want to do but don't want to have to write ourselves, so python provides builtin
# modules for a lot of common operations. So what's provided? A LOT:
#   https://docs.python.org/3/library/
# You're not expected to memorise that at all, standard libraries are something that you
# become familiar with over time, and often discover entirely new ways to solve problems
# with even late into your career. A quick search online for a problem you have will
# generally show you the libraries you can use to help. There are a few common libraries
# however that we'll cover here - this is by no means an exhaustive list though!

# OS
# The os module is short for "Operating System" and provides a lot of useful functions
# for interacting with the rest of the computer's filesystem and other utilities. The
# great thing is that the package automatically detects what filesystem you're on, so
# you can write code that works in many operating systems using one module!
import os

# Gets the filename (or folder name) of a given path
os.path.basename("/this/is/an/example/file.ext")  # file.ext
# Gets the directory path for the given folder/file
os.path.dirname("/this/is/an/example/file.ext")  # /this/is/an/example
# Joins together a path and folder/filename(s) using the OS correct separator
os.path.join("/some/directory", "file.ext")  # /some/directory/file.ext
os.path.join("/some/directory", "folder", "file.ext")  # /some/directory/folder/file.ext
# Checks whether a path exists on the filesystem
os.path.exists("/some/directory")  # False
# Access to all the environment variables as a dictionary
environment_variables = os.environ  # {"PATH": "...", ...}
python_path = os.environ["PYTHONPATH"]  # Whatever value is set in the environment

# MATH
# Provides a lot of common mathematical operations
import math

radians = math.radians(60)  # Converts degrees to radians
math.cos(radians)  # 0.5
math.sqrt(100)  # 10  <- Square root

# RANDOM
# The random module is useful for generating or picking random values
import random

random.randint(1, 10)  # A random number between 1 and 10 (inclusive)
random.random()  # A random float between 0.0 and 1.0
random.choice(["a", "b", "c"])  # Picks a random value from a given list

# SYS
import sys

# Provides the values on the PATH environment variable as a list of paths
path = sys.path
# Provides the extra arguments passed to a script. The first value is always the
# filepath to the script being run.
arguments = sys.argv[1:]
# For example, running "python C:\Users\Matthew\myscript.py 1 two" will result in:
print(sys.argv)  # ['C:\\Users\\Matthew\\myscript.py', '1', 'two']

# See the library argparse for more advanced use of reading command line arguments

# ============================================================================ #
# THIRD PARTY LIBRARIES
# As good as the standard library is, there's always things it doesn't provide, but that
# doesn't mean we have to write it ourselves. Searching online will often find that
# someone has already solved the problem, or at least provided some code that does a lot
# of the work. Using third party libraries is good, as it reduces the amount of work
# required by the developer, and means someone else is maintaining it. It's like getting
# a developer to make and support part of your application for you!

# The easiest way to get third party code is to find a python "package" (which is
# another term for a folder of modules) that is on pypi, the python package index:
#   https://pypi.org/
# This is a communal resource for verified code that will work with python, and is
# really easy to install! Python comes with a builtin tool called "pip", short for
# "Package Installer for Python". You can run this on the command line to automatically
# find packages from pypi and install them for you.
# To demonstrate, you can run the following command to install Fileseq, a common vfx
# package for handling file sequences
#   pip install Fileseq
# Fileseq documentation:
#   https://fileseq.readthedocs.io/en/latest/
import fileseq

sequence = fileseq.FileSequence("/fake/file/sequence.5-100#.png")
sequence.frameRange()  # '5-100'
sequence.frame(32)  # '/fake/file/sequence.0032.png'
sequence.start()  # 5
sequence.basename()  # 'sequence.'
sequence.dirname()  # '/fake/file'

for filepath in sequence:
    print(filepath)

# Installing third party modules using pip will install them in a location relative to
# the current python interpreter (ie, the executable for the version of python you're
# currently running). It's important to make sure you install to the right version of
# python, otherwise the package won't be available to the other ones. If you want to be
# explicit about which version you install to, you can call pip from the python
# executable using the "-m" flag like so:
#   C:\Python27\python.exe -m pip install Fileseq

# ============================================================================ #
# FILE HANDLES
# It's possible to read and write files on the computer using python. This is made
# really easy using the builtin "open" command, which you call by passing it a filepath.
f = open("/path/to/a/file.txt", "w")

# The second argument is the "mode" it opens in, eg, read-only, write-only, read and
# write. There are many modes, but here are the most important:
#   w - read and write
#   r - read only
#   a - append (this is like w, but writing to the file adds on the end instead of
#       replacing the content)
# Read more about file handle modes here: https://stackabuse.com/file-handling-in-python/
# Note: If you open a filepath in write mode, it will create the file if it doesn't exist

# You can read the contents of the file using one of the following methods
line = f.readline()  # Reads one line
contents = f.read()  # Reads the entire contents

# You can write to the file using the write methods
f.write("Writing some text to the file")

# Be careful though, when you open a file it will stay open for the entire duration of
# the python session until you close it again
f.close()

# This can cause problems if you forget to close it, or if an error is raised that
# prevents it from closing. To avoid this, there is another keyword which allows certain
# python objects to run some code when starting an indented block, and ensures it can
# also run some code when the block ends, even if there were errors. This is referred to
# as a "context" and is start using the "with" keyword. The syntax is as follows:
with open("/path/to/a/file.txt") as f:
    data = f.read()

# The "with" keyword takes an object (in this case, the file handle created by open),
# and stores it in a variable "f" using the "as" keyword. We're then able to run any
# code we need with the file handle, and when the block ends, it automatically closes
# the file for us, even if we raise an error! This is the safest way to open files.

# ============================================================================ #
# BEST PRACTICES
# When programming, it's important to try and write carefully to avoid causing bugs, but
# also to make the code easier to read, understand, and maintain. You want to be able to
# come back to code you wrote a year ago and understand what's happening. With that in
# mind, there are some best practices when starting to code.

# 1 Use comments to explain WHY you do something, not WHAT you're doing. The code
#   already says what it's doing, but the reasoning behind it might not be clear,
#   especially to someone who didn't write the code.
# 2 A function should only do one thing, and do it well. If there are two things to be
#   done, make two functions. By separating the problems out, it becomes a lot easier to
#   break down the tasks and handle each separately without having to worry about the
#   rest of the code.
# 3 Keep functions small. If it's a lot of lines of code, it should probably break up
#   into smaller functions.
# 4 Functions should be self contained and rely on very specific data structures, or
#   lots of global variables (or any at all!). For example, don't make a function that
#   takes a single parameter which is a list of [string, integer, boolean] just because
#   you have another function that builds that list. Instead, make a function that takes
#   three parameters - you can still pass the values in correctly, but the function is
#   now much clearer.
# 5 Explicit is better than implicit. Make your code as "strict" as possible, and avoid
#   ANY assumptions. If code has to assume something, it's a bug waiting to happen. It's
#   easy to relax restrictions later if needed, but it's impossible to make it stricter
#   without breaking existing uses.
# 6 Work in stages, and test often. Break up the work into small parts, write the first
#   part, and test it until it works. Repeat until you've solved the problem.
# 7 Don't worry about making it efficient at first. You can tidy up later - the priority
#   is to get it working first.
# 8 Tidy up when you're done! It's tempting to stop writing code once it's working, but
#   it's important to look back over it and make sure the code is tidy, and to simplify
#   where possible. The less code you use, the less you have to maintain. "Every line is
#   a potential bug".
