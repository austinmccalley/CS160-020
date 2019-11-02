import turtle
import math as Math
from random import randint
"""
Helpful functions:
    turtle.forward(dist)    or turtle.fd(dist)
    turtle.right(deg)       of turtle.rt(deg)
    turtle.left(deg)        or turtle.lt(deg)
Creating a turtle:
    myTurtle = turtle.Turtle()
    #now you can use this instead of 'turtle.'
    myTurtle.fd(20)

docs: https://docs.python.org/3.3/library/turtle.html?highlight=turtle#module-turtle
"""
##### EXAMPLE FUNCTION #####
def crazy_turtle(myTurtle):
    while randint(0,10) != randint(0, 10):
        myTurtle.fd(randint(30, 50))
        myTurtle.rt(randint(-180, 180))

##### DEFINE FUNCTIONS HERE #####
def draw_square(myTurtle):
  for x in range(0,4):
    turtle.fd(15)
    turtle.rt(90)

def calc_angle(sides):
    # ((n-2)/n * 180)
    l = float(sides) - 2.0
    n = l / sides
    iang = n * 180

    eang = 360 / float(sides)
    return iang, eang

def shape_calc(sides, l):
  iang, eang = calc_angle(sides)
  # Internal and external angles
  return eang


def draw_ngon(myTurtle, length, n_sides):
  angle, r = shape_calc(n_sides, length)
  print(angle)
  for x in range(0, n_sides):
    turtle.fd(length)
    turtle.rt(angle)


def draw_star(turtle, size, n, angle):

    for side in range(n):
        turtle.fd(size)
        turtle.rt(angle)
        turtle.fd(size)
        turtle.rt((float(360)/float(n)) - angle)

def main():
    myTurtle = turtle.Turtle()
    #draw_square(myTurtle)

    #draw_ngon(myTurtle, 50, 5)
    draw_star(myTurtle, 50, 8, 75)

    ##### CALL YOUR FUNCTIONS #####


# These lines handle calling main, if main should be called
if __name__ == '__main__':
    main()
else:
  # This would be weird
  pass
