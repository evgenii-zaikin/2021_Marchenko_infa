import turtle

turtle.shape('turtle')
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
n = 1
while n < 9:
    turtle.penup()
    turtle.goto(-10*n, -10*n)
    turtle.pendown()
    turtle.forward(10+20*n)
    turtle.left(90)
    turtle.forward(10+20*n)
    turtle.left(90)
    turtle.forward(10+20*n)
    turtle.left(90)
    turtle.forward(10+20*n)
    turtle.left(90)
    n = n + 1
input()
