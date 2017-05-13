colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import *
speed(-1)

penup()
setposition(-200, 0)
pendown()

for i in range (3,8):
    for n in range(i):
        color (colors[i-3])
        forward (100)
        left (360/i)
penup()
setposition(50, 100)
pendown()

for i in range (5):
    color (colors[i])
    begin_fill()
    for n in range (2):
        forward (50)
        left (90)
        forward (100)
        left (90)
    forward (50)
    end_fill()
