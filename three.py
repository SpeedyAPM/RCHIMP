"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
t.speed(1)
t.getscreen().delay(0)


t.penup()                #don't draw when turtle moves
t.goto(0, -100)       #move the turtle to a location
t.showturtle()           #make the turtle visible
t.pendown()              #draw when the turtle moves

t.color('red')
t.circle(50,180)
t.right(180)
t.forward(10)
t.circle(40,200)
