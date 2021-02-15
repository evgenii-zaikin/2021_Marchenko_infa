from random import *
import turtle

turtle.shape('turtle')

i = 1
while i < 20:
    if random() > 0.5:
        turtle.forward(30*random())
        turtle.left(360*random())
    else:
        turtle.forward(30 * random())
        turtle.right(360 * random())
    i = i + 1
input()
