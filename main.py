"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.speed(0)
t.goto(0, 0)
s.listen()


def fpoint(x, y):
    t.goto(x, y)
    t.write(str(x) + "," + str(y))


s.onclick(fpoint, "1")

t.color('red')
t.left(90)
t.forward(75)
t.left(135)
t.forward(35)
