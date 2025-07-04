from turtle import *
from math import *
screensize(0.8,0.8)
setup(width=0.5, height=0.5, startx=1, starty=None)
hideturtle()
tracer(0)
up()
scale = 50
accuracy = 0.001
start = 1
end = 10000
for i in range(start, end):
    x = i*accuracy
    y = log(x, e)
    goto(x*scale,y*scale)
    down()
update()
done()