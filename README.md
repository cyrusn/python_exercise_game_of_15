# Game of 15

An exercise of Python frontend application


# Goal

Write a traditional game call "Game of 15" in python.

# Programming Style
- In order to keep the code clean and readable, oop style and MVC folder stucture will be used.
- The code should be run in python3


# Tools
- [TkInter - Python Wiki](https://wiki.python.org/moin/TkInter)

# Reminder

To update value in button or label, you have to use textvariable option and use `tk.StrinVar()` or `tk.IntVar()`

``` python
# example
from tkinter import *

root = Tk()
var = StringVar()
var.set('hello')

l = Label(root, textvariable = var)
l.pack()

t = Entry(root, textvariable = var)
t.pack()

root.mainloop() # the window is now displayed
```
