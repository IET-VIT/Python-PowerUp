### Design -1 Circle Spiro graph

import turtle  
# Creating turtle  
t = turtle.Turtle()  
  
turtle.bgcolor("black")  
turtle.pensize(2)  
turtle.speed(0)  
  
while (True):  
    for i in range(6):  
        for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:  
            turtle.color(colors)  
            turtle.circle(100)  
            turtle.left(10)  
  
  
turtle.hideturtle()  
turtle.mainloop()

### Design - 2: Python Vibrate Circle

import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("black")  
t.pencolor("red")  
  
a = 0  
b = 0  
t.speed(0)  
t.penup()  
t.goto(0,200)  
t.pendown()  
while(True):  
    t.forward(a)  
    t.right(b)  
    a+=3  
    b+=1  
    if b == 210:  
        break  
    t.hideturtle()  
  
turtle.done()

### Design - 3: Love Shape

import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("black")  
  
turtle.pensize(2)  
  
# To design curve  
def curve():  
    for i in range(200):  
        t.right(1)  
        t.forward(1)  
  
t. speed(3)  
t.color("red", "pink")  
  
t.begin_fill()  
t.left(140)  
t.forward(111.65)  
curve()  
  
t.left(120)  
curve()  
t.forward(111.65)  
t.end_fill()  
t.hideturtle()  
  
turtle.mainloop()  
