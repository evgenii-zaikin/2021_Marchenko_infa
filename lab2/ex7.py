import turtle

turtle.shape('turtle')
turtle.forward(10)
turtle.left(90)
n = 0
while n < 10:
    turtle.forward(10+n*10)
    turtle.left(90)
    n = n + 1

input()
