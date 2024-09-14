import turtle
from turtle import*
#for flag stick
a=turtle.Turtle()
a.speed(3)
a.right(90)
a.pensize(5)
a.pencolor("brown")
a.forward(300)
a.backward(300)
a.left(90)
#for orange&white rectangle
a.color("orange")
a.begin_fill()
a.forward(300)
a.left(90)
a.forward(75)
a.left(90)
a.forward(300)
a.left(90)
a.forward(75)
a.end_fill()
a.color("white")
a.begin_fill()
a.forward(75)
a.left(90)
a.forward(300)
a.left(90)
a.forward(75)
a.backward(75)
a.end_fill()
#for green rectangle
a.pencolor("light green")
a.color("light green")
a.begin_fill()
a.right(180)
a.forward(75)
a.right(90)
a.forward(300)
a.right(90)
a.forward(75)
a.right(90)
a.forward(300)
a.end_fill()
#for middle blue circle
a.backward(150)
a.color("navy")
a.pensize(5)
a.circle(38)
a.left(90)
a.forward(38)
# for 24 spokes of indian flag
for i in range(24):
    a.forward(38)
    a.backward(38)
    a.left(15)




