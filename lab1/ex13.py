import turtle

turtle.shape('turtle')
n = 1
m = 9
while n < m + 1:
    turtle.forward(90)
    turtle.left(180-180/m)
    n = n + 1
input()