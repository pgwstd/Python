from turtle import *
color('red','blue')
begin_fill()
while True:
    forward(300)
    right(150)
    if abs(pos()) < 1:
        break
end_fill() 
