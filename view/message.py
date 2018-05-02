import tkinter as tk


class MessageFrame(tk.Frame):
    """MessageFrame is the frame of the quit button"""

    def __init__(self, stringvar_instance):
        super(MessageFrame, self).__init__()
        self.pack()
        self.var = stringvar_instance
        self.label = tk.Label(self,
                              textvariable=self.var)
        self.label.pack(side=tk.BOTTOM)

    def updateMessage(self, newMessage):
        self.var.set(newMessage)
