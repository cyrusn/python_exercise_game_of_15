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

Another method to update a label by using .configure on label instance.

``` python
# example on textvariable
from tkinter import *
from time import sleep

root = Tk()
var = StringVar()
var.set('Hello World')

l = Label(root, textvariable = var)
l.pack()

sleep(2)

var.set('Hello! World.')

root.mainloop() # the window is now displayed
```


``` python
# example on using configure method
from tkinter import *
from time import sleep

root = Tk()

l = Label(root, text='Hello World')
l.grid()

sleep(2)

l.configure(text='hello! World.')
t.grid()

root.mainloop() # the window is now displayed



```