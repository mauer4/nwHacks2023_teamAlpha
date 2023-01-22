from tkinter import *
import math
import classify_text

class graphics:

    def __init__(self, master):
        self.master = master
        self.master.title("GUI")
        self.master.geometry("1000x500")

        self.counter = 0
        self.currentText = []
        self.history = {}

        self.d = {"test1": 3, "test3": 0.3, "test2": 0.01}

        # https://stackoverflow.com/questions/7727804/tkinter-using-scrollbars-on-a-canvas
        self.frame = Frame(master, width=5000, height=2500)
        self.frame.pack(expand=True, fill=BOTH)
        self.canvas = Canvas(self.frame, bg='#89CFF0', width=5000, height=2500, scrollregion=(0, 0, 50000, 2500))
        hbar = Scrollbar(self.frame, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)
        vbar = Scrollbar(self.frame, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(width=1000, height=500)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)

        
    

        self.close_Button = Button(self.frame, text="Close", width=4, height=1, command=master.quit)
        self.close_Button.place(x=945, y=0)

    def updateGUI(self, d):
        x1 = 50 + self.counter * 200
        y1 = 175
        x2 = 200 + self.counter * 200
        set = list(d.keys())  # keyset = topics

        for i in range(0, len(set)):
            distance = i * 50
            if set[i] in self.history.keys():
                self.canvas.delete(self.history[set[i]][5])
                #self.canvas.coords(self.history[set[i]][4], self.history[set[i]][0], self.history[set[i]][1], self.history[set[i]][2] + 200
                #, self.history[set[i]][3])
                l2 = self.canvas.create_line(self.history[set[i]][0], self.history[set[i]][1], self.history[set[i]][2], self.history[set[i]][3])
                self.canvas.create_line(self.history[set[i]][2], self.history[set[i]][3], x1, y1 + distance + 10)
                l4 = self.canvas.create_line(x1, y1 + distance + 10, x2, y1 + distance + 10, arrow=LAST)
                self.history[set[i]] = (x1, y1 + distance + 10,  x2, y1 + distance + 10, set[i], l4)
                self.canvas.create_text(x1 + 50, y1 + distance, text=set[i])
                #l2 = myLine(x1 + self.counter * 200, y1 + distance + 10, x2 + self.counter * 200, y1 + distance + 10,
                #           set[i], a.line)

            else:
                line = self.canvas.create_line(x1, y1 + distance + 10, x2,
                                               y1 + distance + 10, arrow=LAST)
                
                self.history[set[i]] = (x1, y1 + distance + 10, x2, y1 + distance + 10,
                           set[i], line)
                self.canvas.create_text(x1 + 50, y1 + distance, text=set[i])

        self.counter += 1



#root = Tk()
#gui = GUI(root)
#a = {"test4": 3, "test3": 0.3, "test2": 0.01}
#b = {"a": 3, "b": 0.3, "c": 0.01, "d": 0.01}
#c = {"aa": 3, "ba": 0.3, "ca": 0.01}
#gui.updateGUI(a)
#gui.updateGUI(b)
#gui.updateGUI(c)
#root.mainloop()
