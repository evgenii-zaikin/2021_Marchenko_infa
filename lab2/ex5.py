import turtle
turtle.shape('turtle')
m = 10
n = 0
while n < m:
    turtle.goto(0,0)
    turtle.left(360/m)
    turtle.forward(100)
    turtle.stamp()
    n = n + 1
input()
