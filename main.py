"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
from draw import *
from random import randint
import turtle

t = turtle.Turtle()
s = turtle.Screen()
board(5,200,200)

struct siatka [10,10]
{ int x
int y
}

for (i = -50 , i < 50 ,i+10)
  for (j = -50 , j < 50 ,j+10)
    siatka.x = i
    siatky.y = j


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

