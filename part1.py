import turtle
import time
wn = turtle.Screen()
wn.bgcolor("Black")
wn.setup(width=600 , height=600)
wn.title("Clock Watch Program Muits help")



#Creating Our Drawing

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw(h , m , s , pen):
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)


    # Drawing Clock line - lesson 2
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)


    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
   
draw(pen)








wn.mainloop()