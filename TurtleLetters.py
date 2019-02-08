import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	tur.pu()
        tur.fd(10)
        tur.right(90)
        tur.fd(10)
        tur.pd()
        tur.fd(40)
        tur.left(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        tur.fd(10)
        tur.left(90)
        tur.fd(10)
        tur.right(90)
    elif letter == "F":
	 tur.right(90)
        tur.pd()
        tur.left(90)
       
        tur.right(180)
    
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(20)
        tur.pu()
        tur.fd(10)
        tur.left(90)
        tur.fd(10)
        tur.right(90)
    elif letter == "G":
	    pass		
    elif letter == "H":
	tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	tur.pd()
        tur.right(45)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.right(180)
    elif letter == "W":
	tur.pd()
        tur.right(90)
        tur.fd(60)
        tur.left(135)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.left(135)
        tur.fd(60)
    elif letter == "X":
	tur.pd()
        tur.right(45)
        tur.fd(60)
        tur.left(180)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(60)
    elif letter == "Y":
	tur.pd()
        tur.right(45)
        tur.fd(30)
        tur.left(90)
        tur.fd(30)
        tur.right(180)
    elif letter == "Z":
	tur.pd()
        tur.right(360)
        tur.fd(30)
        tur.right(120)
        tur.fd(50)
        tur.left(120)
        tur.fd(30)	

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        turtleLetter("box",tur)
	
2






window = turtle.Screen()
tur = turtle.Turtle()
tur.speed(1)
#turtleLetter("box",tur)
turtleLetter("A",tur)


window.exitonclick()
