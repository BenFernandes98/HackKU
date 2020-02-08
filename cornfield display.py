# change default python in cmd
# Open CMD: python --version
# Type "env" in search bar at bottom of windows
# Select Environment Variables...
# Under System Variables, select PATH
# Type C:\Users\benja\Python\Python38-32
# Type C:\Users\benja\Python\Python38-32\Scripts\

# pip install Pillow

import tkinter
import PIL.Image, PIL.ImageTk
import os
import random

people = [[],[]]

#creates window and canvas
window=tkinter.Tk()
window.geometry("800x600")
winFrame=tkinter.Frame(window, bg="black")
winFrame.pack(expand=1, fill=tkinter.BOTH)
canvas = tkinter.Canvas(winFrame,width=400,height=400)
canvas.pack()

#creates button
var=tkinter.IntVar()
button=tkinter.Button(winFrame, text="Next", command=lambda:var.set(1))
button.pack()

w = tkinter.Scale(winFrame, from_=0, to=10, orient=tkinter.HORIZONTAL, length=200)
w.pack()


#lists all corn in database
allCorn=[]
dir=r"C:\Users\benja\PycharmProjects\KUHackathon\cornImages"
for filename in os.listdir(dir):
    fold=filename.replace("corn","cornImages\corn")
    allCorn.append(fold)

#lists all corn that will be used in the program
usedCorn=[]
for i in range(0,5):
    ranCorn=random.randint(0,len(allCorn)-1)
    usedCorn.append(allCorn[ranCorn])
    del allCorn[ranCorn]

#formats corn to be used by tkinter
canvasPhotos = []
size=(400,400)
for j in usedCorn:
    pilImage = PIL.Image.open(j)
    formatImage=pilImage.thumbnail(size, PIL.Image.ANTIALIAS)
    image = PIL.ImageTk.PhotoImage(pilImage)
    canvasPhotos.append(image)

#button action
for aperson in people:
    for k in canvasPhotos:
        canvas.create_rectangle((0,0,400,400), fill = "black")
        imagesprite = canvas.create_image(200,200,image=k,anchor=tkinter.CENTER)
        aperson.append(w.get())
        button.wait_variable(var)

###################################################logic
###################################################output to go

window.mainloop()


