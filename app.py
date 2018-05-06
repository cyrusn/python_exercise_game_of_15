import tkinter as tk
from controller.controller import Controller
from view.quit import QuitFrame
from view.message import MessageFrame
from view.button import ButtonFrame
from view.grid import GridFrame


class App(tk.Frame):

    def __init__(self, master):
        super(App, self).__init__()
        self.pack()

        master.title("Game of 15")

        c = Controller()
        counterVar = tk.StringVar()
        MessageFrame(counterVar)
        GridFrame(c, counterVar)
        QuitFrame()

        master.lift()
        master.attributes('-topmost', True)


def center_window(width=240, height=180):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


root = tk.Tk()
center_window()
app = App(root)
root.mainloop()
