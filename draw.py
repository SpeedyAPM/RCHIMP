from random import randint
import turtle

# turtle.setundobuffer(15)
turtle.pensize(3)
turtle.speed(1000)
t = turtle.Screen()

def change_position(x,y):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    # print(x,y)

def box_draw(pos_x: int, pos_y: int, size: int):
    '''Making a box a 'size' value away in all directions starting from (pos_x, pos_y)'''
    change_position(pos_x + size,pos_y)
    turtle.goto(pos_x + size,pos_y + size) # 1
    marker_1 = turtle.position()
    turtle.goto(pos_x - size,pos_y + size) # 2
    marker_2 = turtle.position()
    turtle.goto(pos_x - size,pos_y - size) # 3
    marker_3 = turtle.position()
    turtle.goto(pos_x + size,pos_y - size) # 4
    marker_4 = turtle.position()
    turtle.goto(pos_x + size,pos_y)
    change_position(pos_x,pos_y)

    box_markers = (marker_1, marker_2, marker_3, marker_4)
    return box_markers

def is_free(pos_x, pos_y):
    pass

def board(how_many:int, size_x:int, size_y:int):
    '''Making a (2*size_x : 2*size_y) board with 'how_many' items on it'''
    for i in range(1,how_many + 1):
        x = randint(-size_x + 30,size_x - 30)  # +- 30 for making all of the boxes fully visible on the screen
        y = randint(-size_y + 30,size_y - 30)
        is_free(x,y) # ultimately is to select coordinates
        box_draw(x,y,25)
        change_position(x, y - 25)
        turtle.write(str(i),True, align='center',font=('Arial',30,'normal'))

t.mainloop()
