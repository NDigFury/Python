'''
Author: <Nikki Diguardi>
Date: <1.22.2022>
Class: ISTA 130
Section Leader: <Sara Cielaszyk>

Description:
<When I saw the first lecture with turtle and the professor showed drawings
from the last class I knew what I wanted to draw.
I'm going to draw Hogwarts. I have drawn hogwarts using many differt mediums
so I am familar with the source material. I also wanted to achieve the 
bragging rights of having my drawing possibly shared.>
Reflecting back on this after almost a week later I should have just done the shapes.
But, I am so proud of how it turned out. I put it on tik tok.
'''


import turtle
# I also wanted to time myself on how long I could code for fun. 11.50 
# that was a terrible idea because I restarted from teh beggining so many times.
# I don't know how to run the code and edit at the point if I paused the run line.

def bridge(neville):
    # For the bridge there four archways, which can be made into a function
    # since the function will be used multiple times.
    neville.pencolor('#8b4513')
    neville.pendown()
    neville.left(90)
    neville.fd(20)
    neville.circle(-10,180)
    neville.fd(20)
    neville.left(90)
    neville.penup()

def buttress(neville):
# The great hall has flying butresses, in total 5 in sequence. Therefore, the 
# turtle will end each to start the next.
    neville.color('#e0ffff')
    neville.pencolor('#b0c4de')
    neville.pendown()
    neville.fd(20)
    neville.left(90)
    neville.back(20)
    neville.fd(42)
    neville.stamp()
    neville.back(22)
    neville.right(90)
    neville.penup()

def long_roof(neville):
# There are 5 triangle roofs that can replicated into a function for repeatability.
    neville.pencolor('#20b2aa')
    neville.pendown()
    neville.back(20)
    neville.right(80)
    neville.fd(50)
    neville.left(155)
    neville.fd(50)
    neville.right(75)
    neville.penup()    


def short_roof(neville):
# There are four short roofs for this repeated function
    neville.pencolor('#8fbc8f')
    neville.pendown()
    neville.fd(20)
    neville.left(120)
    neville.fd(20)
    neville.left(120)
    neville.fd(20)#
    neville.left(120)
    neville.penup()




def tower(neville):
# There are five repeated towers that can use this function most are in the
# foreground so they will have a lighter shade
    neville.pencolor('#d3d3d3')
    neville.pendown()
    neville.right(90)
    neville.fd(40)
    neville.right(90)
    neville.fd(20)
    neville.right(90)
    neville.fd(40)
    neville.left(90)
    neville.penup()


#==========================================================
def main():
    '''
    From the starting position I wanted to do the drawing in two halves
    I used graph paper to design the basic outline of Hogwarts. I then
    split my drawing into 4 equal sections. I highlighted any like 
    characteristics that can be reproduced via function. Each function will end
    facing right to ensure the pen will always face the same way.
    '''
    luna = turtle.Turtle()

    turtle.bgcolor('navy')
#change the background color to have a contrast.
    luna.color('#ffefd5')
    luna.pensize(3)
    luna.speed(0)
    luna.pencolor('#778899')
    luna.left(180)
    luna.penup()
    luna.fd(5)
    luna.pendown()
    luna.left(90)
    luna.fd(25)
    luna.back(25)
    luna.right(90)
    luna.fd(15)
    luna.right(90)
    luna.back(25)
    luna.fd(35)
    luna.right(30)
    luna.fd(10)
    luna.left(50)
    luna.pencolor('#20b2aa')
#change color for roof
    luna.fd(40)
    luna.left(135) #? I put notes here to try and do math
    luna.fd(40)
    luna.left(115)
    luna.fd(30)
    luna.back(30)
#change color for walls
    luna.pencolor('#778899')
    luna.right(55)
    luna.fd(10)
    luna.right(35) 
    luna.fd(35) #should be alighen with the other side but shorter
    luna.back(10)
    luna.right(90)
    luna.fd(20)
    luna.right(90)
    luna.back(10)
    luna.fd(80)
    luna.right(90)
    luna.fd(10)
    luna.left(90)
    luna.fd(5)
    luna.left(20)
    luna.pencolor('#20b2aa')
#change color for roof
    luna.fd(120)
    luna.left(140)
    luna.fd(115) #? if too long i.e.-5
    luna.back(50)
#change color to tower color
    luna.pencolor('#778899')
    luna.right(120)
    luna.fd(20)
    luna.right(40)
    luna.fd(25)
    luna.right(90)
#first short roof changed the function to suit this first roof.
    short_roof(luna)

    luna.fd(20)
    luna.right(90)
    luna.pencolor('#778899')
    luna.pendown()
    luna.fd(15)
    luna.penup()
    luna.right(90)
    luna.fd(20)
    luna.right(60)
    luna.pendown()
    luna.fd(15)
    luna.penup()
    luna.fd(30)
    luna.right(120)
    luna.fd(20)
    luna.left(90)
    luna.back(15)
    luna.color('#20b2aa')
# Add a roof to Dumbledore's study.
    luna.stamp()
    luna.back(100)
    luna.left(90)
    luna.back(75)
    luna.pencolor('#778899')
    luna.pendown()
    luna.fd(100)
    luna.penup()
    luna.fd(20)
    luna.left(90)
    luna.fd(15)
    luna.right(90)

    tower(luna)
# This is the tower over the great hall, I think this is where divination is.
    luna.right(180)
    luna.fd(20)
    luna.right(90)
    luna.fd(40)
    luna.left(90)

    long_roof(luna)
# This is the first long roof I altered the function to suit this roof,
# At first I also made the drawing to short for a long roof.
    luna.left(90)
    luna.fd(30)
    luna.right(90)
    luna.pendown()
    luna.color('#778899')
    luna.fd(20)
    luna.right(90)
    luna.fd(10)
    luna.left(90)
    luna.penup()
    luna.fd(20)

    long_roof(luna)

    luna.back(20)
    luna.left(90)
    luna.fd(10)
    luna.right(50)
    luna.color('#778899')  
    luna.pendown()
    luna.fd(45)
    luna.back(18)
    luna.right(130)
    luna.fd(26)
    luna.right(90)
    luna.penup()
    luna.back(15)
    luna.right(90)
    luna.fd(37)
    luna.pendown()
    luna.fd(60)
    luna.left(180)
    luna.fd(25)
    luna.right(90)
    luna.fd(2)
# Spam flying buttresses along the great hall
    buttress(luna)
    buttress(luna)
    buttress(luna)
    buttress(luna)
    buttress(luna)
    
    luna.pendown()
    luna.fd(20)
    luna.left(90)
    luna.back(20)
    luna.color('#778899')
    luna.left(90)
    luna.fd(120)
    luna.back(120)
#The great hall needs a base
    luna.right(90)
    luna.fd(55)
    luna.right(40)
    luna.fd(40)
    luna.penup()
    luna.right(140)
    luna.fd(40)
    luna.pendown()
    luna.color('#20b2aa')
    luna.right(20)
    luna.fd(30)
    luna.back(30)
    luna.left(40)
    luna.fd(30)
    luna.right(110)
    luna.fd(20)
    luna.left(90)
    luna.color('#778899')
    luna.fd(50)
    luna.back(50)
    luna.left(90)
    luna.penup()
    luna.fd(20)
    luna.pendown()
    luna.right(90)
    luna.fd(50)
    luna.back(10)
    luna.left(90)
    luna.color('green')
# In the books the whomping willow is seen in this courtyard.
    luna.circle(-80, 40)
    luna.left(40)
    luna.color('#778899')
    luna.back(50)
    luna.fd(140)
    luna.right(180)
    luna.fd(20)
    luna.penup()
    luna.left(90)
    luna.fd(10)
    luna.right(90)
    luna.pendown()
    luna.fd(100)
    luna.penup()
    luna.left(90)
    luna.fd(45)
    luna.left(90)
# The start of the bridge where Harry talked to Reamus
    bridge(luna)
    
    luna.right(90)
    luna.pendown()
    luna.fd(20)
    luna.left(90)
    luna.penup()
    luna.fd(10)
    luna.left(90)
    luna.pendown()
    luna.back(10)
    luna.fd(30)
    luna.right(90)

    bridge(luna)
# The bridge during the battle of hagwarts that Neville blew up
    luna.pendown()
    luna.right(90)
    luna.fd(20)
    luna.back(10)
    luna.left(90)
    luna.penup()
    luna.fd(10)
    luna.left(90)  
    luna.pendown()
    luna.fd(10)
    luna.right(90)

    bridge(luna)
  
    luna.fd(10)

    bridge(luna)
# I wanted the bridge to trail off like it was going behind cliffs
    luna.home()
    luna.right(90)
    luna.fd(50)
    luna.left(90)
    luna.fd(20)


    bridge(luna)
# this is more like an archway than a bridge but I was happy to use the function again
    luna.home()
    luna.pencolor('#778899')
    luna.left(180)
    luna.fd(5)
    luna.left(90)
    luna.fd(10)
    luna.left(90)
    luna.pendown()
    luna.fd(60)
    luna.right(90)
    luna.fd(10)
    luna.right(90)

    tower(luna)

    luna.right(90)
    luna.fd(20)
    luna.right(90)
# This side is less iconic than the great hall
    tower(luna)

    luna.fd(20)
    luna.left(90)
    luna.pendown()
    luna.back(20)
    luna.fd(20)
    luna.left(90)

    tower(luna)
# This is was easier to code because it was more functions
    luna.left(90)
    luna.fd(20)
    luna.right(90)
    luna.color('#778899')
    luna.pendown()
    luna.fd(30)
    luna.left(90)
    luna.back(10)
    luna.fd(40)
    luna.right(90)
    luna.fd(20)
    luna.right(90)
    luna.fd(20)
    luna.back(20)
    luna.left(90) 
    luna.back(20)
    luna.left(180)

    long_roof(luna)

    luna.left(90)
    luna.fd(10)
    luna.right(90)
    luna.fd(48)

    long_roof(luna)
# There are many towers and roofs on this side
    luna.fd(38)
    luna.left(180)

    short_roof(luna)

    luna.left(90)
    luna.fd(17)
    luna.left(90)
    luna.fd(20)
    luna.left(180)

    short_roof(luna)

    luna.fd(30)
    luna.left(90)
    luna.color('#778899')
    luna.pendown()
    luna.fd(35)
    luna.left(40)
    luna.fd(10)
    luna.right(40)
    luna.fd(15)
    luna.right(30)
    luna.fd(35)
    luna.right(60)
    
    short_roof(luna)
# The hardest part was trying to change the pen color before drawing
    luna.fd(20)
    luna.pendown()
    luna.color('#20b2aa')
    luna.fd(10)
    luna.right(120)
    luna.fd(35)
    luna.right(60)
    luna.fd(30)
    luna.back(30)
    luna.left(90)
    luna.fd(15)
    luna.penup()
    luna.back(43)
    luna.left(90)
    luna.fd(17)
    luna.right(90)
    luna.color('#778899')
    luna.pendown()
    luna.fd(55)
    luna.penup()
    luna.fd(50)
    luna.left(90)
    luna.fd(20)
    luna.pendown()
    luna.right(90)
    luna.fd(20)
    luna.back(20)
    luna.left(90)

    short_roof(luna)

    luna.home()
    luna.right(90)
    luna.fd(50)
    luna.left(90)
    luna.fd(10)


    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
''' Looking back on this code. It took way to long to do. I think if I was doign this 
project on my own time, I would have added cliffs. Yet, thinking about doing
those angles is a hard pass. I know this means it almost doesn't look done.
I think it looks like a tattoo and that's what I wanted. '''