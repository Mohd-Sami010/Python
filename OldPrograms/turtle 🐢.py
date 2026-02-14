from turtle import *
color('black', 'cyan')
begin_fill()
while True:
    forward(200) 
    left(256)
    backward(100)
    if abs(pos()) < 1:
        break
end_fill()
done()