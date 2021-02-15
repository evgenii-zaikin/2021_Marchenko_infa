import turtle

turtle.shape('turtle')
n = 1
x = 0.01
while n < 360*5:
    turtle.forward(1+x)
    turtle.left(1)
    n = n + 1
    x = x +0.01
input()