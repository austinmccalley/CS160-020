import turtle
import math as Math
from random import randint

def getCords(turtle):
  return turtle.xcor(), turtle.ycor()

def a(turtle, u=False):
  if u:
    # Init pos
    turtle.seth(0)
    sxcord = turtle.xcor()

    # Outside of letter A
    turtle.pendown()
    turtle.lt(75)
    turtle.fd(100.8414)
    turtle.seth(0)
    turtle.rt(75)
    turtle.fd(100.8414)

    # Get finish position
    fxcord = turtle.xcor()
    fycord = turtle.ycor()

    # Draw across line
    turtle.penup()
    turtle.setx(sxcord)
    turtle.seth(0)
    turtle.lt(75)
    turtle.pendown()
    turtle.fd(100.8414/2.0)
    turtle.seth(0)
    turtle.fd(25)

    # Put in ending spot
    turtle.penup()
    turtle.setx(fxcord)
    turtle.sety(fycord)

  else:
    # Init turtle
    turtle.penup()
    turtle.seth(0)
    turtle.fd(25)
    turtle.pendown()

    turtle.circle(25)
    turtle.penup()
    turtle.seth(90)
    turtle.fd(25)
    turtle.seth(0)
    turtle.fd(25)
    turtle.pendown()
    turtle.seth(-65)
    turtle.fd(30)

def b(turtle, u=False):
  if u:
    # Init pos
    turtle.penup()
    turtle.seth(0)
    sxcord = turtle.xcor()
    sycord = turtle.ycor()

    # Draw backbone
    turtle.pendown()
    turtle.seth(90)
    turtle.fd(100)
    turtle.seth(-90)
    turtle.penup()
    turtle.fd(100)
    turtle.seth(0)

    # Draw Loops
    turtle.pendown()
    turtle.circle(25, 180)
    turtle.penup()
    turtle.seth(0)
    turtle.pendown()
    turtle.circle(25,180)

    # Return to endpoint
    turtle.penup()
    turtle.setx(sxcord)
    turtle.sety(sycord)
    turtle.seth(0)
    turtle.fd(26)

  else:
    # Init pos
    turtle.seth(0)
    sxcord = turtle.xcor()
    sycord = turtle.ycor()

    # Circle for bottom part
    turtle.penup()
    turtle.fd(25)
    turtle.pendown()
    turtle.circle(25)
    turtle.penup()

    # Go to start
    turtle.setx(sxcord)
    turtle.sety(sycord)
    turtle.seth(90)

    # Draw line
    turtle.pendown()
    turtle.fd(100)

    # Go to end of letter
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(100)
    turtle.seth(0)
    turtle.fd(50)

def d(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw semi-circle
    turtle.pendown()
    turtle.circle(50, 180)

    # Draw backbone
    turtle.seth(-90)
    turtle.fd(101)

    # Go to end
    turtle.seth(0)
    turtle.penup()
    turtle.fd(50)


  else:
    # Init turtle
    turtle.penup()
    sxcord,sycord = getCords(turtle)

    # Draw backbone
    turtle.seth(0)
    turtle.fd(50)
    turtle.pendown()
    turtle.seth(90)
    turtle.fd(100)
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(100)

    # Draw loop
    turtle.seth(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(25)
    turtle.pendown()
    turtle.circle(25)
    turtle.penup()

    # Go to end
    turtle.seth(0)
    turtle.fd(25)
    turtle.seth(-90)
    turtle.fd(50)

def e(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw bottom line
    turtle.penup()
    turtle.fd(50)
    turtle.seth(180)
    turtle.pendown()
    turtle.fd(50)

    # Draw 1/2 of backbone with mid-line
    turtle.seth(90)
    turtle.fd(50)
    turtle.seth(0)
    turtle.fd(50)
    turtle.penup()
    turtle.seth(180)
    turtle.fd(50)

    # Draw top half
    turtle.pendown()
    turtle.seth(90)
    turtle.fd(50)
    turtle.seth(0)
    turtle.fd(50)

    # Go to end of word
    turtle.penup()
    turtle.setx(sxcord + 50)
    turtle.sety(sycord)

  else:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.penup()
    turtle.seth(0)

    # Draw lower part of e
    turtle.fd(50)
    turtle.seth(90)
    turtle.fd(25)
    turtle.seth(-90)
    turtle.pendown()
    turtle.circle(-25, 180)
    turtle.fd(10)

    # Draw top part of e
    turtle.seth(0)
    turtle.fd(50)
    turtle.seth(-90)
    turtle.circle(-25, -180)

    # Go to end of word
    turtle.penup()
    turtle.seth(0)
    turtle.fd(50)
    turtle.seth(-90)
    turtle.fd(35)
    turtle.sety(sycord)

def h(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)
    turtle.pendown()

    # Draw First Vertical line
    turtle.seth(90)
    turtle.fd(100)

    # Draw Horizontal Line
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(50)
    turtle.seth(0)
    turtle.pendown()
    turtle.fd(50)

    # Draw Last Vertical Line
    turtle.penup()
    turtle.seth(90)
    turtle.fd(50)
    turtle.seth(-90)
    turtle.pendown()
    turtle.fd(100)
  else:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw backbone
    turtle.pendown()
    turtle.seth(90)
    turtle.fd(100)
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(100)

    # Draw hump
    turtle.seth(90)
    turtle.fd(20)
    turtle.pendown()
    turtle.circle(-25,180)
    turtle.fd(20)

def i(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw first horizontal line
    turtle.penup()
    turtle.fd(50)
    turtle.seth(180)
    turtle.pendown()
    turtle.fd(50)

    # Draw Vertical Line
    turtle.penup()
    turtle.seth(0)
    turtle.fd(25)
    turtle.seth(90)
    turtle.pendown()
    turtle.fd(100)

    # Draw second horizontal line
    turtle.penup()
    turtle.seth(0)
    turtle.fd(25)
    turtle.seth(180)
    turtle.pendown()
    turtle.fd(50)

    # GO to end of shape
    turtle.penup()
    turtle.setx(sxcord + 50)
    turtle.sety(sycord)

  else:
    # Init Turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw Vertical Line
    turtle.seth(90)
    turtle.pendown()
    turtle.fd(50)

    # Draw circle
    turtle.penup()
    turtle.fd(15)
    turtle.seth(0)
    turtle.pendown()
    turtle.circle(5)

    # Go to end of shape
    turtle.seth(-90)
    turtle.penup()
    turtle.fd(65)
    turtle.seth(0)
    turtle.fd(5)
    turtle.sety(sycord)

def l(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw bottom line
    turtle.penup()
    turtle.fd(50)
    turtle.seth(180)
    turtle.pendown()
    turtle.fd(50)

    # Draw backbone
    turtle.seth(90)
    turtle.fd(100)

    # Go to end of shape
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(100)
    turtle.seth(0)
    turtle.fd(50)
  else:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw just a straight line
    turtle.seth(90)
    turtle.pendown()
    turtle.fd(100)

    # Go to end of shape
    turtle.penup()
    turtle.seth(-90)
    turtle.fd(100)
    turtle.seth(0)
    turtle.fd(5)

def m(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)
    turtle.penup()

    # Draw First Line
    turtle.pendown()
    turtle.seth(80)
    turtle.fd(101.54)

    # Draw second line
    turtle.seth(-70)
    turtle.fd(25)

    # Draw third line
    turtle.seth(70)
    turtle.fd(25)

    # Draw fourth line
    turtle.seth(-80)
    turtle.fd(101.54)

  else:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.penup()

    # Draw First Line
    turtle.pendown()
    turtle.seth(80)
    turtle.fd(101.54/2.0)

    # Draw second line
    turtle.seth(-70)
    turtle.fd(25/2.0)

    # Draw third line
    turtle.seth(70)
    turtle.fd(25/2.0)

    # Draw fourth line
    turtle.seth(-80)
    turtle.fd(101.54/2.0)


def o(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw A big circle
    turtle.penup()
    turtle.fd(50)
    turtle.pendown()
    turtle.circle(50)

    # GO to end of shape
    turtle.penup()
    turtle.fd(50)
  else:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw a smaller circle
    turtle.penup()
    turtle.fd(65.0/2.0)
    turtle.pendown()
    turtle.circle(65.0/2.0)

    # Go to end of shape
    turtle.penup()
    turtle.fd(65.0/2.0)

def p(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw the backbone
    turtle.pendown()
    turtle.seth(90)
    turtle.fd(100)
    turtle.seth(0)

    # Draw the semi-circle
    turtle.circle(-25, 180)
    turtle.penup()

    # Return to end of the shape
    turtle.sety(sycord)
    turtle.setx(sxcord + 26)
    turtle.seth(0)
  else:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)

    # Draw the backbone
    turtle.pendown()
    turtle.seth(90)
    turtle.fd(20)
    turtle.seth(-90)
    turtle.fd(80)

    # Draw the half circle
    turtle.penup()
    turtle.seth(90)
    turtle.fd(80)
    turtle.seth(0)
    turtle.pendown()
    turtle.circle(-15,180)

    # Go to end of shape
    turtle.penup()
    turtle.seth(0)
    turtle.setx(sxcord + 25)
    turtle.sety(sycord)

def r(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)
    turtle.penup()

    # Draw backbone
    turtle.seth(90)
    turtle.pendown()
    turtle.fd(100)
    turtle.penup()

    # Draw Loops
    turtle.seth(0)
    turtle.pendown()
    turtle.circle(-25,180)
    turtle.seth(270+33)
    turtle.fd(58.253)

    # End of shape
    turtle.seth(0)
    turtle.penup()
    turtle.sety(sycord)
    turtle.setx(sxcord + 30)

  else:
    # Init Turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)
    turtle.penup()

    # Draw backbone
    turtle.seth(90)
    turtle.pendown()
    turtle.fd(100.0/3.0 + 5)
    turtle.penup()

    # Draw arch
    turtle.seth(-90)
    turtle.fd(15)
    turtle.pendown()
    turtle.seth(90)
    turtle.circle(-15,160)

    # End of shape
    turtle.penup()
    turtle.setx(sxcord + 25)
    turtle.sety(sycord)
    turtle.seth(0)

def s(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)
    turtle.penup()

    # Draw bottom arch
    turtle.pendown()
    turtle.circle(25, 180)
    turtle.seth(180)

    # Draw top arch
    turtle.circle(-25, 270-45)

    # End of shape
    turtle.penup()
    turtle.seth(0)
    turtle.setx(sxcord+50)
    turtle.sety(sycord)
  else:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)
    turtle.penup()

    # Draw bottom arch
    turtle.pendown()
    turtle.circle(25.0/2.0, 180)
    turtle.seth(180)

    # Draw top arch
    turtle.circle(-25.0/2.0, 270-45)

    # End of shape
    turtle.penup()
    turtle.seth(0)
    turtle.setx(sxcord+25)
    turtle.sety(sycord)

def t(turtle, u=False):
  if u:
    # Init shape
    sxcord, sycord = getCords(turtle)
    turtle.penup()
    turtle.seth(0)

    # Draw middle line
    turtle.fd(27)
    turtle.seth(90)
    turtle.pendown()
    turtle.fd(100)

    # Drop top line
    turtle.penup()
    turtle.seth(0)
    turtle.fd(25)
    turtle.seth(180)
    turtle.pendown()
    turtle.fd(50)

    # End of shape
    turtle.penup()
    turtle.sety(sycord)
    turtle.setx(sxcord + 54)
    turtle.seth(0)
  else:
    # Init shape
    sxcord, sycord = getCords(turtle)
    turtle.penup()
    turtle.seth(0)

    # Draw middle line
    turtle.fd(17)
    turtle.seth(90)
    turtle.pendown()
    turtle.fd(50)

    # Draw middle line t
    turtle.penup()
    turtle.seth(270)
    turtle.fd(10)
    turtle.seth(0)
    turtle.fd(35.0/2.0)
    turtle.seth(180)
    turtle.pendown()
    turtle.fd(35)

    # ENd of shape
    turtle.penup()
    turtle.sety(sycord)
    turtle.setx(sxcord + 36)
    turtle.seth(0)

def ul(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.penup()
    turtle.seth(0)

    # Draw First horizontal line
    turtle.seth(90)
    turtle.fd(100)
    turtle.seth(270)
    turtle.pendown()
    turtle.fd(75)

    # Draw bottom arch
    turtle.circle(25, 180)

    # Draw second horizontal line
    turtle.seth(90)
    turtle.fd(75)

    # End of shape
    turtle.penup()
    turtle.sety(sycord)
    turtle.setx(sxcord + 50)
    turtle.seth(0)


  else:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.penup()
    turtle.seth(0)


    # Draw First horizontal line
    turtle.seth(90)
    turtle.fd(50)
    turtle.seth(270)
    turtle.pendown()
    turtle.fd(50-15)

    # Draw bottom arch
    turtle.circle(15, 180)

    # Draw second horizontal line
    turtle.seth(90)
    turtle.fd(50-15)

    # End of shape
    turtle.penup()
    turtle.sety(sycord)
    turtle.setx(sxcord + 30)
    turtle.seth(0)

def w(turtle, u=False):
  if u:
    # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.penup()
    turtle.seth(0)

    # Draw first line downwards
    turtle.sety(sycord + 100)
    turtle.seth(-80)
    turtle.pendown()
    turtle.fd(101.54)

    # Draw second line upwards
    turtle.seth(65)
    turtle.fd(100.0/3.0)

    # Draw third line downwards
    turtle.seth(-65)
    turtle.fd(100.0/3.0)

    # Draw fourth line upwards
    turtle.seth(80)
    turtle.fd(101.54)

    # End of shape
    turtle.penup()
    turtle.seth(0)
    turtle.sety(sycord)
    turtle.setx(sxcord + 65)

  else:
        # Init turtle
    sxcord, sycord = getCords(turtle)
    turtle.penup()
    turtle.seth(0)

    # Draw first line downwards
    turtle.sety(sycord + 50)
    turtle.seth(-80)
    turtle.pendown()
    turtle.fd(50.771)

    # Draw second line upwards
    turtle.seth(65)
    turtle.fd(50.0/3.0)

    # Draw third line downwards
    turtle.seth(-65)
    turtle.fd(50.0/3.0)

    # Draw fourth line upwards
    turtle.seth(80)
    turtle.fd(50.771)

    # End of shape
    turtle.penup()
    turtle.seth(0)
    turtle.sety(sycord)
    turtle.setx(sxcord + (65.0/2.0))

def y(turtle, u=False):
  if u:
    # Init shape
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)
    turtle.penup()

    # Draw middle
    turtle.fd(25)
    turtle.seth(90)
    turtle.pendown()
    turtle.fd(75)

    # Draw left line
    turtle.seth(90+(105.0/2.0))
    turtle.fd(35.867)

    # Draw right line
    turtle.seth(-37.5)
    turtle.fd(35.867)
    turtle.seth(90-(105.0/2.0))
    turtle.fd(35.867)

    # End of shape
    turtle.penup()
    turtle.seth(0)
    turtle.sety(sycord)
    turtle.setx(sxcord + 66.5)

  else:
    # Init shape
    sxcord, sycord = getCords(turtle)
    turtle.seth(0)
    turtle.penup()

    # Draw middle
    turtle.fd(25.0/2.0)
    turtle.seth(90)
    turtle.pendown()
    turtle.fd(75.0/2.0)

    # Draw left line
    turtle.seth((90+(105.0/2.0)))
    turtle.fd(35.867/2.0)

    # Draw right line
    turtle.seth(-37.5)
    turtle.fd(35.867/2.0)
    turtle.seth(90-(105.0/2.0))
    turtle.fd(35.867/2.0)

    # End of shape
    turtle.penup()
    turtle.seth(0)
    turtle.sety(sycord)
    turtle.setx(sxcord + 67.0/2.0)

def word_space(turtle):
  sxcord, sycord = getCords(turtle)
  turtle.penup()
  turtle.sety(sycord)
  turtle.setx(sxcord+10)

def space(turtle):
  sxcord, sycord = getCords(turtle)
  turtle.penup()
  turtle.sety(sycord)
  turtle.setx(sxcord + 35)

def next_line(turtle):
  sxcord, sycord = getCords(turtle)
  turtle.penup()
  turtle.setx(sxcord)
  turtle.sety(sycord - 150)

def is_int(s):
   negative = True if s[:1] == '-' else False
   if negative:
       if len(s) == 1:
           return False
       s = s[1:]
       for c in s:
           if not (c>='0' and c<='9'):
               return False
       return True
   else:
       for c in s:
           if not(c>='0' and c<='9'):
               return False
       return True

def getRWords():
  rwords = []
  words = ['atm','rush','tray','poor','duty','able','ally','what', 'blameworthy', 'whiteboards', 'yawp', 'whom', 'aero']
  try:
    num_words = input('How many words would you like to generate? ')
    if not is_int(num_words):
      print('Please enter an integer!')
      return getRWords()
    num_words = int(num_words)
    if num_words > 4 or num_words <= 0:
      print('Please pick a number from 1 to 4')
      return getRWords()
    else:
      for i in range(num_words):
        ri = randint(0,len(words)-1)
        if words[ri] not in rwords:
          rwords.append(words[ri])
        else:
          ri = randint(0, len(words)-1)
          rwords.append(words[ri])
      return rwords
  except Exception as e:
      print('We got an error: \n%s' % e)
      return getRWords()

def is_tf(s):
  if s.lower() not in ['t','f', 'true', 'false']:
    return False
  return True

def s_tf(s):
  if is_tf(s):
    if s.lower() == 't' or s.lower() == 'true':
      return True
    else:
      return False
  else:
    return 'Error'


def main():
  myTurtle = turtle.Turtle()

  randomWords = getRWords()

  uppercase_s = input('Do you want the letters to be uppercase(T,F)? ')
  u = s_tf(uppercase_s)
  if not u == 'Error':
    wcount = 0
    for word in randomWords:
      print('Writing to screen %s' % word)
      if (wcount % 2) == 0 and not wcount == 0 or len(word) > 6:
        sy = myTurtle.ycor()
        myTurtle.penup()
        myTurtle.sety(sy - 150)
        myTurtle.setx(0)
      space(myTurtle)
      for ch in word:
          ch = ch.lower()
          word_space(myTurtle)
          if ch == 'a':
            a(myTurtle, u)
          elif ch == 'b':
            b(myTurtle, u)
          elif ch == 'd':
            d(myTurtle, u)
          elif ch == 'e':
            e(myTurtle, u)
          elif ch == 'h':
            h(myTurtle, u)
          elif ch == 'i':
            i(myTurtle, u)
          elif ch == 'l':
            l(myTurtle, u)
          elif ch == 'm':
            m(myTurtle, u)
          elif ch == 'o':
            o(myTurtle, u)
          elif ch == 'p':
            p(myTurtle, u)
          elif ch == 'r':
            r(myTurtle, u)
          elif ch == 's':
            s(myTurtle, u)
          elif ch == 't':
            t(myTurtle, u)
          elif ch == 'u':
            ul(myTurtle, u)
          elif ch == 'w':
            w(myTurtle, u)
          elif ch == 'y':
            y(myTurtle, u)
      space(myTurtle)
      wcount += 1

  else:
    print('Please pick either True(t) or False(f) for the letters of the words to be uppercase!')
    main()





# These lines handle calling main, if main should be called
if __name__ == '__main__':
    main()
else:
  # This would be weird
  pass
