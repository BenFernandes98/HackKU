
from tkinter import *

def main():
    master = Tk()

    #Slider
    w = Scale(master, from_=0, to=10, orient=HORIZONTAL)
    w.configure(bg='orange2', activebackground='gold', cursor='circle', length=300, troughcolor='light yellow', width=15)
    w.pack()

    #Button
    w = Button(master, text="Next")
    w.configure(activebackground='gold', bg='orange2', height=3, width=8)
    w.pack()

main()
