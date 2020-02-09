
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


def main():
    A=[8,9,5,3,1]
    B=[8,9,5,3,1]
    print(compareScores(A,B))

    isKeyAcceptable=False
    window = GraphWin("gameWindow", 800, 738)
    myImage = Image(Point(400,369), "cornGUI_0.png")
    myImage.draw(window)
    #window.mainloop()
    input_box=Entry(Point(400,680),5)
    input_box.fill="white"
    input_box.setSize(20)
    input_box.draw(window)
    previousEntry=""
    while True:
        key=window.getKey()
        for i in range(10):
            if (key==(str(i))):
                isKeyAcceptable=True
        #if (key==BACKSPACE):
            #isKeyAcceptable=True
        if (isKeyAcceptable==False):
            input_box.setText(previousEntry)
        isKeyAcceptable=False
        previousEntry=""
        previousEntry+=input_box.getText()
        
    

if __name__=="__main__":
          main()
