import turtle
from polygon import arc

smallTurtle = turtle.Turtle()
smallTurtle.shape('turtle')

def petal(t, r, angle):
    """ Draws a petal.
    t: turtle
    r: radius of the arc
    angle: angle (in degrees) of the/that subtends the arc """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t, r, n, angle):
    """ Draws a flower.
    t: turtle
    r: radius of the arc
    n: number of petals
    angle: angle (in degrees) of the/that subtends the arc """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360 / n)

def turtle_positioning(t, length):
    """ Positions/moves the turtle.
    t: turtle
    length: amount to move """
    t.pu()
    t.forward(length)
    t.pd()

turtle_positioning(smallTurtle, -150)
flower(smallTurtle, 100, 7, 45)

turtle_positioning(smallTurtle, 150)
flower(smallTurtle, 75, 10, 60)

turtle_positioning(smallTurtle, 150)
flower(smallTurtle, 250, 20, 15)

smallTurtle.hideturtle()
turtle.mainloop()
