from random import randint
import turtle
import math

def checking(x,y):
    if x.xcor()==y.xcor() and x.ycor()==y.ycor():
        return True
    else:
        return False
number_of_turtles = 15
steps_of_time_number = 300
pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(0)
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.left(randint(0, 360))
for i in range(steps_of_time_number):
    for unit in pool:
        if unit.xcor()>200 or unit.xcor()<-200 or unit.ycor()>200 or unit.ycor()<-200:
            unit.left(180)
        for chert in pool:
            if math.sqrt((chert.xcor()-unit.xcor())**2+(chert.ycor()-unit.ycor())**2)>0 and math.sqrt((chert.xcor()-unit.xcor())**2+(chert.ycor()-unit.ycor())**2) < 25:
                unit.left(180)
                chert.left(180)
        unit.forward(2)
input()