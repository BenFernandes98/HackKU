
from graphics import *
import random
import math


#Show introductory title screen
def start():
    window=GraphWin("titleWindow",700, 646)
    myImage=Image(Point(350,323), "cornhub_GUI_title.png")
    myImage.draw(window)
    window.getKey()
    window.close()

    window=GraphWin("titleWindow",700, 646)
    myImage=Image(Point(350,323), "cornhub_GUI_personA.png")
    myImage.draw(window)
    window.getKey()
    window.close()




#Transition to personB
def middle():
    window=GraphWin("titleWindow",700, 646)
    myImage=Image(Point(350,323), "cornhub_GUI_personB.png")
    myImage.draw(window)
    window.getKey()
    window.close()




#Gives a match percentage for two ppl based on their corn ratings
#A and B are arrays of corn picture ratings
#A and B must be equal in size
def compareScores(A,B):
    diff=0
    for i in range(len(A)):
        diff+=abs(A[i]-B[i])
    percentage=int(abs(((diff/45)*100)-100))
    insult(percentage)




#Make Gordan Ramsey insult
def insult(percentage):
    textFile=open("result", "w+")

    insults=["This is a really tough decision, because you're both crap.\n",
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
   
    randomGen=random.randint(0,len(insults)-1)
    

    hawaiian=["He ho'oholo pa'akiki loa keia, no ka mea 'oi oulua 'elua",
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

    textFile.write(str(percentage)+" ")
              
    textFile.write(insults[randomGen])

    textFile.write("Here is your insult in Hawaiian:" + hawaiian[randomGen])

    textFile.close()


def main():
    A=[8,9,5,3,1]
    B=[8,9,5,3,1]
    start()
    #Person A rates 5 images
    middle()
    #Person B rates 5 images
    compareScores(A,B)
    #open GO
    

main()
