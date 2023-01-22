from tkinter import *
import math


class GUI:

    def __init__(self, master):
        self.master = master
        self.master.title("GUI")
        self.master.geometry("1000x500")

        self.counter = 0
        self.currentText = []
        self.history = {}

        self.d = {"test1": 3, "test3": 0.3, "test2": 0.01}

        # https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas
        self.frame = Frame(root, width=5000, height=2500)
        self.frame.pack(expand=True, fill=BOTH)
        self.canvas = Canvas(self.frame, bg='#FFFFFF', width=5000, height=2500, scrollregion=(0, 0, 5000, 2500))
        hbar = Scrollbar(self.frame, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)
        vbar = Scrollbar(self.frame, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(width=1000, height=500)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
        self.arrow_button = Button(self.frame, text="Arrow", width=4, height=1, command=lambda: self.updateGUI(self.d))

        self.arrow_button.place(x=0, y=0)

        self.close_button = Button(self.frame, text="Close", width=4, height=1, command=master.quit)
        self.close_button.place(x=40, y=0)

    def updateGUI(self, d):
        x1 = 50 + self.counter * 200
        y1 = 70
        x2 = 250 + self.counter * 200
        set = list(d.keys())  # keyset = topics

        for i in range(0, len(set)):
            if set[i] in self.history.keys():
                a = self.history[set[i]]
                a.num += 1
                self.canvas.coords(a.line, a.x1, a.y1, a.x2 + 200 * a.num, a.y2)

            else:

                distance = i * 50
                line = self.canvas.create_line(x1 + self.counter * 200, y1 + distance + 10, x2 + self.counter * 200,
                                               y1 + distance + 10, arrow=LAST)
                l = myLine(x1 + self.counter * 200, y1 + distance + 10, x2 + self.counter * 200, y1 + distance + 10,
                           set[i], line)

                self.history[set[i]] = l
                self.canvas.create_text(x1 + 100 + self.counter * 200, y1 + distance, text=set[i])

        self.counter += 1


class myLine:

    def __init__(self, x1, y1, x2, y2, name, line):
        self.num = 0
        self.x1 = x1
        self.x2 = x2
        self.y2 = y2
        self.y1 = y1
        self.name = name
        self.line = line


root = Tk()
gui = GUI(root)
root.mainloop()
