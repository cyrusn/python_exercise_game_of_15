import tkinter as tk


class QuitFrame(tk.Frame):
    """QuitFrame is the frame of the quit button"""

    def __init__(self):
        super(QuitFrame, self).__init__()
        self.pack()
        self.button = tk.Button(self,
                                text="Quit", fg="red",
                                command=self.quit)
        self.button.pack(side=tk.BOTTOM)
