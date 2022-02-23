#kochsnow.py
import turtle as t
def koch(size,n):
    if n==0:
        t.fd(size)
    else:
        for angel in [0,60,-120,60]:
            t.left(angel)
        #    t.fd(size)
            koch(size/3,n-1)
def main():
    t.setup(800,600)
    t.penup()
    t.goto(-300,100)
    t.pendown()
    t.pensize(5)
    t.pencolor("blue")
    level=3
    for i in range(0,3):
       koch(400,level)
       t.right(120)   
    t.hideturtle()
    t.done()
main()
