
from graphics import *

#Gives a match percentage for two ppl based on their corn ratings
#A and B are arrays of corn picture ratings
#A and B must be equal in size
def compareScores(A,B):
    diff=0
    for i in range(len(A)):
        diff+=abs(A[i]-B[i])
    percentage=abs(((diff/45)*100)-100)
    msg="Both responses were a "+str(percentage)+"% match. "
    if (percentage<50):
        msg+="You two are not compatible."
    else:
        msg+="You two were meant to be."
    return msg


#Builds a separate window with the GUI graphic
#Must have the GUI graphic saved in the same folder as this script
def buildGUI():
    isKeyAcceptable=False
    window = GraphWin("gameWindow", 800, 738)
    myImage = Image(Point(400,369), "cornGUI_0.png")
    myImage.draw(window)


def main():
    A=[8,9,5,3,1]
    B=[8,9,5,3,1]
    print(compareScores(A,B))
    buildGUI()
    

if __name__=="__main__":
          main()
