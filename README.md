# Python 101

Welcome to python! Python is a powerful language that's much easier to learn than many "low level" languages like C++ or Java. This repository provides a quick and simple introduction to all the different concepts needed to get started with programming in python, no previous knowledge required!

### File Layout

This repository is broken up into different weeks. Each week has the following structure:
* **examples.py** : Contains the topics being covered this week with examples of how to use them, and comments explaining what's happening. This file is unlikely to be able to run directly, it is only for examples.
* **exercises.py** : A number of exercises to test what you've learned. Try to answer without checking the examples.py file if you can.
* **challenge.py** : A more complete exercise that combines the different things you've learned this week to achieve a goal.

### How to run python
Firstly, make sure that you've downloaded and installed python. If you don't have it, you can download it from [here](https://www.python.org/downloads/). It's recommended to pick the newest version, which at the time of writing this is 3.8.2 (nearly all the code in this repo will work with any version > 3.0.0)


### Python Interpreter
Once you have python installed, open your `terminal`. How to access this will depend on your operating system:
* Windows:
  1. On the keyboard, press "WindowsKey + R" to open the "Run" dialog
  2. Enter "cmd" and press enter
* Ubuntu (Linux):
  1. On the keyboard, press "Ctrl + Alt + T"
* Mac:
  1. On the keyboard, press "Command + Space" to open the search
  2. Enter "Terminal" and press enter or double click "Terminal" from the UI

In the terminal, type in "python" (without quotes, all lowercase) and press enter. You should see some text saying the version number of python and then a new line starting with ">>>". This is called the python interpreter. You can type python here line by line, and it will run each line as you enter it. Try typing "2 + 2" (without quotes) and pressing enter. You should see the number 4 appear on a new line, and then it returns to ">>>", meaning it's waiting for a new line to run.

To exit the interpreter, type "exit()" (without quotes) and press enter, or using the keyboard press "Ctrl + D". Either of these will return you to the regular terminal

#### Python Scripts
It's much more common to write python inside of a file and then run the file. Files with code are often referred to as "scripts". You can write code inside of any text editor (even Notepad), however, it's much better to use what's called an IDE (short for Integrated Development Environment), which is basically a text editor specifically for writing code. These provide extra tools which can make it a lot easier to find and fix mistakes in the code. There are many IDEs out there, but here are a few common ones:

* [Pycharm](https://www.jetbrains.com/pycharm/download) : Pycharm is a python specific IDE, meaning it can do a lot more with python than others can. It can be a little daunting with so many options though. It has a free Community edition which can do more than enough while you're learning the language.
* [VSCode](https://code.visualstudio.com/download) : VSCode is a simple and clean editor which can be used for any language. Easy to use, it does require a little bit of setup if you want to get all the benefits for writing in a specific language (like python). They have good documentation for [getting started with python in vscode](https://code.visualstudio.com/docs/languages/python).
* [Sublime Text](https://www.sublimetext.com/3) : Sublime text is another relatively simple editor that does a lot out of the box. It can also be heavily customised similar to VSCode. Unlike the others, it can be evaluated for free, but requires a license to continue using.

Once you've chosen an editor, you can start by writing some code in a new file. To get started, copy the following into a file:
```python
print("Hello, World!")
```
Save the file somewhere you can find it (If you're in an IDE, save it as part of the current project). When saving a python file, use the extension ".py", eg, "myfile.py". Next, open a terminal. If you're using an IDE, it almost certainly has a terminal inside the UI. Check the bottom of the window for terminal, or the Menu options at the top.

> :warning: **On windows**: If saving the file from a regular text editor, make sure "Hide known extensions" is disabled, otherwise the file might be saved with the extension ".py.txt" which will cause problems).

In the terminal, type "python" followed by the path to the file (In an IDE, you can right click the file and copy the path if you need to). For example:
```bash
python myfile.py
```
This will tell python to run the file you just saved using python. If the file can be found, you should see the output message! If you're getting an error "No such file or directory", make sure you're using the full path to the file.

### Week overview

#### Week 01
Week 1 covers variables, basic data types, operators, conditionals, and a couple of builtin functions for inputting and outputting text.
