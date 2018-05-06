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
        # ButtonFrame("press me!", lambda: m.updateMessage("world"))
        QuitFrame()

        master.lift()
        master.attributes('-topmost', True)

root = tk.Tk()
app = App(root)
root.mainloop()
