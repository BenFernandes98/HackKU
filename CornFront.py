from graphics import*

def main():

    
    win=GraphWin("Corn",500,500)
    win.setCoords(0,0,100,100)

    body=Oval(Point(30,3),Point(70,97))
    body.setFill("yellow")
    body.setOutline("black")
    body.draw(win)

    Pants=Oval(Point(42,3.1),Point(57.6,17))
    Pants.setFill("green")
    Pants.draw(win)
    
#Oval(x,y,width,height)
    #leaf1=Oval(Point(30,3),Point(50,64.6))
    #leaf1.draw(win)

    leaf1=Polygon(Point(50,3),Point(75,64.6),Point(83,35
),Point(97,31))
    leaf1.setFill("green")
    leaf1.draw(win)

    leaf12=Polygon(Point(52,3),Point(83,64.6),Point(86,35
),Point(98,31))
    leaf12.setFill("forestgreen")
    leaf12.draw(win)

    leaf2=Polygon(Point(50,3),Point(25,64.6),Point(23,35
),Point(3,31))
    leaf2.setFill("green")
    leaf2.draw(win)

    leaf22=Polygon(Point(48,3),Point(18,64.6),Point(20,35
),Point(2,31))
    leaf22.setFill("forestgreen")
    leaf22.draw(win)

    
    Eye1=Oval(Point(53,65),Point(63,85))
    Eye1.setFill("white")
    Eye1.draw(win)


    Eye2=Eye1.clone()
    Eye2.move(-16,0)
    Eye2.draw(win)

    Inside1=Oval(Point(53,70),Point(59,80))
    Inside1.setFill("lightseagreen")
    Inside1.draw(win)

    Inside2=Inside1.clone()
    Inside2.move(-16,0)
    Inside2.draw(win)

    Line1=Line(Point(45,46),Point(57,46))
    Line1.setWidth(3)
    Line1.draw(win)

    Line2=Line(Point(57,46),Point(67.8,46))
    Line2.setWidth(3)
    Line2.draw(win)

    Line3=Line(Point(45,46),Point(32.5,46))
    Line3.setWidth(3)
    Line3.draw(win)

    Bowtie1=Circle(Point(57,46),5.5)
    Bowtie1.setFill("brown")
    Bowtie1.draw(win)

    Bowtie2=Bowtie1.clone()
    Bowtie2.move(-15,0)           
    Bowtie2.draw(win)

    Mouth=Oval(Point(32,55),Point(68,63))
    Mouth.setWidth(2.5)
    Mouth.setFill("coral")
    Mouth.setOutline("lightcoral")
    Mouth.draw(win)

    Tooth1=Rectangle(Point(43.5,57),Point(49.5,63.04))
    Tooth1.setFill("white")
    Tooth1.setOutline("white")
    Tooth1.draw(win)

    Tooth2=Tooth1.clone()
    Tooth2.move(7.5,0)
    Tooth2.draw(win)

    Skirt=Rectangle(Point(27,16),Point(74,21))
    Skirt.setFill("limegreen")
    Skirt.setOutline("limegreen")
    Skirt.draw(win)

    Skirt1=Rectangle(Point(27,16),Point(29.8,0))
    Skirt1.setFill("limegreen")
    Skirt1.setOutline("limegreen")
    Skirt1.draw(win)

    Skirt2=Skirt1.clone()
    Skirt2.move(4,0)
    Skirt2.draw(win)

    Skirt3=Skirt2.clone()
    Skirt3.move(4,0)
    Skirt3.draw(win)

    Skirt4=Skirt3.clone()
    Skirt4.move(4,0)
    Skirt4.draw(win)

    Skirt5=Skirt3.clone()
    Skirt5.move(4,0)
    Skirt5.draw(win)

    Skirt6=Skirt5.clone()
    Skirt6.move(4,0)
    Skirt6.draw(win)
    
    Skirt7=Skirt6.clone()
    Skirt7.move(4,0)
    Skirt7.draw(win)
    
    Skirt8=Skirt7.clone()
    Skirt8.move(4,0)
    Skirt8.draw(win)

    Skirt9=Skirt8.clone()
    Skirt9.move(4,0)
    Skirt9.draw(win)

    Skirt10=Skirt9.clone()
    Skirt10.move(4,0)
    Skirt10.draw(win)

    Skirt11=Skirt10.clone()
    Skirt11.move(4,0)
    Skirt11.draw(win)

    Skirt12=Skirt11.clone()
    Skirt12.move(4,0)
    Skirt12.draw(win)

    Skirt13=Skirt12.clone()
    Skirt13.move(4,0)
    Skirt13.draw(win)


main()
