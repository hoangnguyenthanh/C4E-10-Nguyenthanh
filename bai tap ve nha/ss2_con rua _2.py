from turtle import *
shape("circle")
speed(-1)
for n in range (6,2,-1):
    if n%2 == 0:
        color("red","white")
    else:
        color("blue","white")
    begin_fill()
    for m in range (n):
        forward(100)
        left(360/n)
    end_fill()
        
       
