import turtle
import math
turtle.shape('turtle')
i = 3
while i < 10:
    n = 0
    m = i
    x = math.sin(math.pi / m)
    y = (25+5*(i-3)) / (x*math.sqrt(2))
    turtle.penup()
    turtle.goto(-y, 0)
    turtle.pendown()
    turtle.right(90-180/i)
    while n < m:
        turtle.forward(50+10*(i-3))
        turtle.left(360 / m)
        n = n + 1
    turtle.left(90 - 180 / i)
    i = i + 1
input()
