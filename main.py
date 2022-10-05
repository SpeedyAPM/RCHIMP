"""
Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

from random import randint
import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.speed(0)
t.goto(0, 0)
s.listen()

def box_draw(pos_x: int, pos_y: int, size: int, digit: int):
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
    t.goto(pos_x,pos_y - 18)
    t.write(str(digit),True, align='center',font=('Arial',18,'normal'))
    t.penup()

def box_erase(pos_x: int, pos_y: int, size: int, digit: int):
    '''Making a box a 'size' value away in all directions starting from (pos_x, pos_y)'''
    t.penup()
    t.goto(pos_x + size,pos_y)
    t.pendown()
    t.fillcolor ("white")
    t.begin_fill()
    t.goto(pos_x + size,pos_y + size) # 1
    t.goto(pos_x - size,pos_y + size) # 2
    t.goto(pos_x - size,pos_y - size) # 3
    t.goto(pos_x + size,pos_y - size) # 4
    t.goto(pos_x + size,pos_y)
    t.end_fill()
    t.penup()
    t.goto(pos_x,pos_y)
    t.goto(pos_x,pos_y - 18)
    t.write(str(digit),True, align='center',font=('Arial',18,'normal'))
    t.penup()

def box_hide(pos_x: int, pos_y: int, size: int, digit: int):
    '''Making a box a 'size' value away in all directions starting from (pos_x, pos_y)'''
    t.penup()
    t.goto(pos_x + size,pos_y)
    t.pendown()
    t.fillcolor ("black")
    t.begin_fill()
    t.goto(pos_x + size,pos_y + size) # 1
    t.goto(pos_x - size,pos_y + size) # 2
    t.goto(pos_x - size,pos_y - size) # 3
    t.goto(pos_x + size,pos_y - size) # 4
    t.goto(pos_x + size,pos_y)
    t.end_fill()
    t.penup()
    t.goto(pos_x,pos_y)
    t.goto(pos_x,pos_y - 18)
    #t.write(str(digit),True, align='center',font=('Arial',18,'normal'))
    t.penup()

class meshxy:
    xpoint = int
    ypoint = int
    visibp = bool
    clicked = bool
    digit = int

wymiar1 = 10
wymiar2 = 10
superlista = []

for ii in range (0,wymiar1):
    lista = []
    for jj in range (0,wymiar2):
        x = meshxy()
        lista.append(x)
    superlista.append(lista)
  
# for ii in range (0,10):
#     print(superlista[ii])

xx1 = -270
yy1 = -200
rozmiar = 15
skok = 38
how_many_digits = 8
number_tc = 1

for ii in range (0,wymiar1):
    yy1 = yy1 + skok

    for jj in range(0, wymiar2):
        superlista[ii][jj].xpoint = xx1
        superlista[ii][jj].ypoint = yy1
        xx1 = xx1 + skok
        #superlista[ii][jj].digit = randint(1,how_many_digits + 1)
        superlista[ii][jj].clicked = False
        superlista[ii][jj].visibp = False
        #if (randint(1,3)%3) == 0:
         # superlista[ii][jj].visibp = True
        #print(superlista[ii][jj].xpoint , 'Y:' , superlista[ii][jj].ypoint)
    xx1 = -100



def przeszukiwanie(x,y):
  global number_tc
  for ii in range (0,wymiar1):    
    for jj in range(0, wymiar2):
      xs1 =superlista[ii][jj].xpoint
      ys1 =superlista[ii][jj].ypoint
      if ((x < (xs1 + rozmiar)) and (x > (xs1 - rozmiar) ) and (y < (ys1 + rozmiar)) and (y > (ys1 - rozmiar) )):
        if (superlista[ii][jj].digit == number_tc and superlista[ii][jj].clicked == False):
          number_tc += 1
          
          superlista[ii][jj].clicked = True
          superlista[ii][jj].visibp == False
          t.color('white')
          box_erase(superlista[ii][jj].xpoint, superlista[ii][jj].ypoint , rozmiar, superlista[ii][jj].digit)
          przerysowanie()
          t.color('black')

    



# Losowanie cyfr
for digitsall in range (1,how_many_digits):
  while True:
    ii = randint(0, wymiar1 -1)
    jj = randint(0, wymiar2 -1)
    if (superlista[ii][jj].visibp ==False):
      superlista[ii][jj].visibp = True
      superlista[ii][jj].digit = digitsall
    if superlista[ii][jj].visibp == True:
        break

# Rysowanie
for ii in range (0,wymiar1):
    for jj in range(0, wymiar2):
        #print(superlista[ii][jj].xpoint , 'Y:' , superlista[ii][jj].ypoint)
        if superlista[ii][jj].visibp == True:
          box_draw(superlista[ii][jj].xpoint, superlista[ii][jj].ypoint , rozmiar, superlista[ii][jj].digit)

def przerysowanie():
  for ii in range (0,wymiar1):
    for jj in range(0, wymiar2):
        #print(superlista[ii][jj].xpoint , 'Y:' , superlista[ii][jj].ypoint)
        if superlista[ii][jj].visibp == True and superlista[ii][jj].clicked == False:
          box_hide(superlista[ii][jj].xpoint, superlista[ii][jj].ypoint , rozmiar, superlista[ii][jj].digit)

def fpoint(x, y):
    #t.goto(x, y)
    #t.write(str(x) + "," + str(y))
  przeszukiwanie(x,y)

          
s.onclick(fpoint, "1") # lewy przycisk myszki
s.onclick(fpoint, "3") # prawy przycisk myszki

def screen_clear(x, y):
    size = 500
    
    pos_x = 0
    pos_y = 0
    '''Making a box a 'size' value away in all directions starting from (pos_x, pos_y)'''
    t.penup()
    t.goto(pos_x + size,pos_y)
    t.pendown()
    t.fillcolor ("white")
    t.begin_fill()
    t.goto(pos_x + size,pos_y + size) # 1
    t.goto(pos_x - size,pos_y + size) # 2
    t.goto(pos_x - size,pos_y - size) # 3
    t.goto(pos_x + size,pos_y - size) # 4
    t.goto(pos_x + size,pos_y)
    t.end_fill()
    t.penup()
    t.goto(pos_x,pos_y)
    t.pendown()
    t.penup()
    t.goto(pos_x,pos_y - 18)

    t.penup()

s.onclick(screen_clear, "2") # center(wheel) mouse button