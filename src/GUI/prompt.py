from tkinter import *
import math
import test

class Promt():
    def __init__(self, master):
        self.master = master
        self.master.title("GUI")
        self.master.geometry("300x80")

        self.counter = 0
        self.currentText = []
        self.history = {}

        self.d = {"test1": 3, "test3": 0.3, "test2": 0.01}

        # https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas
        self.frame = Frame(test.root, width=5000, height=2500)
        self.frame.pack(expand=True, fill=BOTH)
        
        self.textBox = Text(self.frame, width = 35, height = 11)
        self.textBox.place(x=700,y=300)

        self.enter_Button = Button(self.frame, text="Enter", width=4, height=1)
        self.enter_Button.place(x=945, y=455)

        self.close_Button = Button(self.frame, text="Close", width=4, height=1, command=master.quit)
        self.close_Button.place(x=945, y=0)

root = Tk()
gui = Prompt(root)

def thread():
    for i in list:
        gui.updateGUI(i)
        root.update
        time.sleep(3)
t = Thread(target=thread)
t.start()
# start the thread in the background
mainloop()