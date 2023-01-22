from tkinter import *
from main import *

root = Tk()
gui = GUI(root)

a = {"test1": 3, "test3": 0.3, "test2": 0.01}
b = {"a": 3, "b": 0.3, "c": 0.01, "d": 0.01}
c = {"aa": 3, "ba": 0.3, "ca": 0.01}
gui.updateGUI(gui, a)
gui.updateGUI(gui, b)
gui.updateGUI(gui, c)
print("hello")

root.mainloop()





