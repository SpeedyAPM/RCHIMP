"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

from random import randint
import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.speed(0)
t.goto(0, 0)
s.listen()




def box_draw(pos_x: int, pos_y: int, size: int):
    '''Making a box a 'size' value away in all directions starting from (pos_x, pos_y)'''
    t.penup()
    t.goto(pos_x + size,pos_y)
    t.pendown()
    t.goto(pos_x + size,pos_y + size) # 1
    t.goto(pos_x - size,pos_y + size) # 2
    t.goto(pos_x - size,pos_y - size) # 3
    t.goto(pos_x + size,pos_y - size) # 4
    t.goto(pos_x + size,pos_y)
    t.penup()
    t.goto(pos_x,pos_y)
    t.pendown()

class meshxy:
    xpoint = int
    ypoint = int
    visibp = bool
    clicked = bool

wymiar1 = 12
wymiar2 = 12
superlista = []

for ii in range (0,wymiar1):
    lista = []
    for jj in range (0,wymiar2):
        x = meshxy()
        lista.append(x)
    superlista.append(lista)
  
# for ii in range (0,10):
#     print(superlista[ii])

xx1 = -100
yy1 = -100
rozmiar = 8

for ii in range (0,wymiar1):
    yy1 = yy1 + 20

    for jj in range(0, wymiar2):
        superlista[ii][jj].xpoint = xx1
        superlista[ii][jj].ypoint = yy1
        xx1 = xx1 + 20
        superlista[ii][jj].clicked = False
        superlista[ii][jj].visibp = False
        if (randint(1,3)%3) == 0:
          superlista[ii][jj].visibp = True
        #print(superlista[ii][jj].xpoint , 'Y:' , superlista[ii][jj].ypoint)
    xx1 = -100


# Rysowanie
for ii in range (0,wymiar1):
    for jj in range(0, wymiar2):
        #print(superlista[ii][jj].xpoint , 'Y:' , superlista[ii][jj].ypoint)
        if superlista[ii][jj].visibp == True:
          box_draw(superlista[ii][jj].xpoint, superlista[ii][jj].ypoint , rozmiar)


def fpoint(x, y):
    #t.goto(x, y)
    #t.write(str(x) + "," + str(y))
    for ii in range (0,wymiar1):    
      for jj in range(0, wymiar2):
        xs1 =superlista[ii][jj].xpoint
        ys1 =superlista[ii][jj].ypoint
        if ((x < (xs1 + rozmiar)) and (x > (xs1 - rozmiar) ) and (y < (ys1 + rozmiar)) and (y > (ys1 - rozmiar) )):
            superlista[ii][jj].clicked = True
            t.color('white')
            box_draw(superlista[ii][jj].xpoint, superlista[ii][jj].ypoint , rozmiar)
            t.color('black')



s.onclick(fpoint, "1")