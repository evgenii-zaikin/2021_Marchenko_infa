import turtle

turtle.shape('turtle')
turtle.fillcolor('#FFFF00')
turtle.begin_fill()
n = 1
while n < 360:
    turtle.forward(2)
    turtle.left(1)
    n = n + 1
turtle.end_fill()
turtle.penup()
turtle.goto( 60 , 120)
turtle.pendown()
turtle.fillcolor('#0000FF')
turtle.begin_fill()
n = 1
while n < 360:
    turtle.forward(0.5)
    turtle.left(1)
    n = n + 1
turtle.end_fill()
turtle.penup()
turtle.goto( -60 , 120)
turtle.pendown()
turtle.fillcolor('#0000FF')
turtle.begin_fill()
n = 1
while n < 360:
    turtle.forward(0.5)
    turtle.left(1)
    n = n + 1
turtle.end_fill()
turtle.pencolor('red')
turtle.pensize(5)
turtle.penup()
turtle.goto( -45 , 60)
turtle.pendown()
n = 1
turtle.right(90)
while n < 180:
    turtle.forward(0.75)
    turtle.left(1)
    n = n + 1

input()