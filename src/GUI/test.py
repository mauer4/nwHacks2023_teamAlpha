from tkinter import *
from main import *
import time
from threading import Thread

root = Tk()
gui = GUI(root)

a = {"test4": 3, "test3": 0.3, "test2": 0.01}
b = {"te": 1, "test4": 0.3, "c": 0.01, "d": 0.01}
c = {"aa": 3, "test4": 0.3, "ca": 0.01}
list = [c,b,a]

def thread():
    for i in list:
        gui.updateGUI(i)
        root.update
        time.sleep(3)
t = Thread(target=thread)
t.start()
# start the thread in the background
mainloop()







