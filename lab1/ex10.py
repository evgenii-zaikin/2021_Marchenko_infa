import turtle
turtle.speed(10)
turtle.shape('turtle')
i = 1
while i < 3:
    n = 1
    while n < 180:
        turtle.forward(0.5+0.5*(i-1))
        turtle.left(2)
        n = n + 1
    n = 1
    while n < 180:
        turtle.forward(0.5+0.5*(i-1))
        turtle.right(2)
        n = n + 1
    i = i + 1
input()