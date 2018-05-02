import tkinter as tk

defaultMessage = "Hello, World"


class MessageFrame(tk.Frame):
    """MessageFrame is the frame to show the message content"""

    def __init__(self, stringvar):
        super(MessageFrame, self).__init__()
        self.pack()
        self.stringvar = stringvar
        self.label = tk.Label(
            self, textvariable=stringvar, width=20)
        self.label.pack(side=tk.BOTTOM)


class ToggleButton(tk.Frame):
    """ToggleButton is the frame of the button to toggle the message content"""

    def __init__(self, var):
        super(ToggleButton, self).__init__()
        self.pack()
        self.var = var
        self.button = tk.Button(self, text="try me!", command=self.press)
        self.button.pack(side=tk.LEFT)

    def press(self):
        if self.var.get() == defaultMessage:
            self.var.set("Hi, you pressed the button!")
        else:
            self.var.set(defaultMessage)


class QuitFrame(tk.Frame):
    """QuitFrame is the frame of the quit button"""

    def __init__(self):
        super(QuitFrame, self).__init__()
        self.pack()
        self.button = tk.Button(self,
                                text="Quit", fg="red",
                                command=self.quit)
        self.button.pack(side=tk.BOTTOM)


class App(tk.Frame):
    """App is the main window for ths example"""

    def __init__(self, master):
        super(App, self).__init__()
        self.pack()

        # Change the application title
        master.title("Tkinter Example")

        # create variable for toggling message
        var = tk.StringVar()
        var.set(defaultMessage)

        # Draw the 3 frames for application
        self.message = MessageFrame(var)
        self.button = ToggleButton(var)
        self.quitButton = QuitFrame()

        # Bring the application window to front
        master.lift()
        master.attributes('-topmost', True)


root = tk.Tk()
app = App(root)
root.mainloop()
