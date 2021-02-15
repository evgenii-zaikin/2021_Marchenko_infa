import turtle

turtle.shape('turtle')
i = 1
while i < 6:
    n = 1
    while n < 360:
        turtle.forward(1)
        turtle.left(1)
        n = n + 1
    turtle.left(60)
    i = i + 1
input()