from graphics import *
import random
import tkinter
import PIL.Image, PIL.ImageTk
import os
import webbrowser


# Show introductory title screen

def start():
    window = GraphWin("titleWindow", 700, 646)
    myImage = Image(Point(350, 323), "peopleImages\cornhub_GUI_title.png")
    myImage.draw(window)
    window.getKey()
    window.close()

    window = GraphWin("titleWindow", 700, 646)
    myImage = Image(Point(350, 323), "peopleImages\cornhub_GUI_personA.png")
    myImage.draw(window)
    window.getKey()
    window.close()


# Transition to personB
def middle():
    window = GraphWin("titleWindow", 700, 646)
    myImage = Image(Point(350, 323), "peopleImages\cornhub_GUI_personB.png")
    myImage.draw(window)
    window.getKey()
    window.close()


# Gives a match percentage for two ppl based on their corn ratings
# A and B are arrays of corn picture ratings
# A and B must be equal in size
def compareScores(A, B):
    diff = 0
    for i in range(len(A)):
        diff += abs(A[i] - B[i])
    percentage = int(abs(((diff / 45) * 100) - 100))
    insult(percentage)


# Make Gordan Ramsey insult
def insult(percentage):
    textFile = open("result", "w+")

    insults = ["This is a really tough decision, because you're both crap.\n",
               "Your cooking is so terrible you can't even apply for McDonalds.\n",
               "You both are an idiot cornwhich.\n",
               "The fish is so raw he's still finding nemo.\n",
               "The crab is so undercooked it's singing under the sea.\n",
               "I wish you'd jump in the oven! That would make my life a lot easier!\n",
               "I wouldn't trust you running a bath, let alone a corn restaurant.\n",
               "This lamb is so undercooked, it's following Mary to school.\n",
               "There's enough garlic in here to kill every vampire in Europe.\n",
               "Why did the chicken cross the road? Because you didn't flippin cook it!\n",
               "This pizza is so disgusting, if you take it to Italy you'll get arrested.\n"]

    randomGen = random.randint(0, len(insults) - 1)

    hawaiian = ["He ho'oholo pa'akiki loa keia, no ka mea 'oi oulua 'elua",
                "Eia no ka makou kuke 'ai 'ana ke hiki 'ole ia 'oe ke noi no McDonalds.",
                "'O 'oe 'elua kahi 'apala 'olelo 'ole.",
                "He 'ala ka i'a a ke 'ike 'o ia i ka nemo.",
                "Puka ka lalo, ua mele 'ia ma lalo o ke kai.",
                "Makemake wau e lele i loko o ka umu! E ho'olu'olu 'ia ko'u ola!",
                "'A'ole au e hilina'i ia 'oe e holo ana i ka 'au'au, e waiho 'oe i kahi hale 'ai palaoa.",
                "Hana 'ia keia keikikane e hahai ana ia Mary ma ke kula.",
                "Ua nui kahi keokeo ma ane'i e pepehi i kela me na vampire ma 'Eulopa.",
                "No ke aha i lele ai ke moa i ke ala? No ka mea, 'a'ole 'oe i flippin e kuke ai!",
                "He mea 'ino'ino keia pizza, ina lawe 'oe ia i Italia e hopu 'ia ai 'oe."]

    textFile.write(str(percentage) + " ")

    textFile.write(insults[randomGen])

    textFile.write("Here is your insult in Hawaiian:" + hawaiian[randomGen])

    textFile.close()


def Ranker(personNumber,whichPerson):
    people = [[], []]

    window = tkinter.Toplevel()
    window.title("Cornhub")
    window.geometry("700x646")

    winFrame = tkinter.Frame(window, bg="black")
    winFrame.pack(expand=1, fill=tkinter.BOTH)

    bgImage = PIL.ImageTk.PhotoImage(PIL.Image.open("bg.png"))
    background = tkinter.Label(winFrame, image=bgImage)
    background.place(x=0, y=0, relheight=1.0, relwidth=1.0)

    #widgets
    l = tkinter.Label(winFrame, text="0/5", bg='orange2')
    l.pack(pady=5)

    canvas = tkinter.Canvas(winFrame, width=560, height=433,bg="#FFA500",highlightthickness=0)
    canvas.pack(side=tkinter.TOP,pady=10)

    w = tkinter.Scale(winFrame, from_=0, to=10, orient=tkinter.HORIZONTAL, bg='orange2', activebackground='gold', cursor='circle', length=300, troughcolor='light yellow', width=15)
    w.pack()

    # creates button
    var = tkinter.IntVar()
    button = tkinter.Button(winFrame, activebackground='gold', bg='orange2', height=3, width=8, text="Next", command=lambda: var.set(1))
    button.pack(pady=10)



    # lists all corn in database
    allCorn = []
    dir = r"C:\Users\benja\PycharmProjects\KUHackathon\cornImages"
    for filename in os.listdir(dir):
        fold = filename.replace("corn", "cornImages\corn")
        allCorn.append(fold)

    # lists all corn that will be used in the program
    usedCorn = []
    for i in range(0, 5):
        ranCorn = random.randint(0, len(allCorn) - 1)
        usedCorn.append(allCorn[ranCorn])
        del allCorn[ranCorn]

    # formats corn to be used by tkinter
    canvasPhotos = []
    size = (400, 400)
    for j in usedCorn:
        pilImage = PIL.Image.open(j)
        formatImage = pilImage.thumbnail(size, PIL.Image.ANTIALIAS)
        image = PIL.ImageTk.PhotoImage(pilImage)
        canvasPhotos.append(image)
    if len(whichPerson)==5:
        canvasPhotos=whichPerson

    numCount = 0
    aperson = people[personNumber]

    for k in canvasPhotos:
        canvas.create_rectangle((0, 0, 560, 433), fill="#FFA500")
        imagesprite = canvas.create_image(280, 216, image=k, anchor=tkinter.CENTER)
        aperson.append(w.get())
        button.wait_variable(var)
        numCount += 1
        l.config(text=str(numCount) + "/5")
    return aperson,window,canvasPhotos



def main():
    start()
    # Person A rates 5 images
    personOne=[]
    scoresOne,win,personTwo=Ranker(0,personOne)
    win.destroy()
    middle()
    # Person B rates 5 images
    scoresTwo,stop,noPerson=Ranker(1,personTwo)
    compareScores(scoresOne, scoresTwo)
    stringbuilder ="file:///C:/Users/benja/PycharmProjects/KUHackathonFinished/index.html"

    webbrowser.open(stringbuilder)

main()
