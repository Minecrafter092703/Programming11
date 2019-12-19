from tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="GO PEE THE BED", fg="red", command =frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="PRESS HERE IF YOU HAVEN'T WET THE BED IN DAYS", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("WHAT'S COOKING, GOOD LOOKING!")

root = Tk()

app = App(root)

root.mainloop()
root.destroy()
