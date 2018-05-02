import tkinter as tk


class ButtonFrame(tk.Frame):
    """ButtonFrame is the frame of the quit button"""

    def __init__(self, text, command):
        super(ButtonFrame, self).__init__()
        self.pack()
        self.button = tk.Button(self,
                                text=text,
                                command=command)
        self.button.pack(side=tk.BOTTOM)
