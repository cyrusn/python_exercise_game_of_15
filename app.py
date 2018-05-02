import tkinter as tk
from lib.game import Game
from view.quit import QuitFrame
from view.message import MessageFrame
from view.button import ButtonFrame


class App(tk.Frame):

    def __init__(self, master):
        super(App, self).__init__()
        self.pack()

        master.title("Game of 15")
        var = tk.StringVar()
        var.set("hello")
        m = MessageFrame(var)

        ButtonFrame("press me!", lambda: m.updateMessage("world"))
        QuitFrame()

        master.lift()
        master.attributes('-topmost', True)

root = tk.Tk()
app = App(root)
root.mainloop()
