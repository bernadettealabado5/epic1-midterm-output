# Bernadette E. Alabado BSCS 1-B
# The Circlemation

import turtle

turtle.title('Alabado - Mandala Pattern Output')

set1 = ['white', 'purple', 'pink', 'blue']
set2 = ['#E9967A', '#7A378B', '#B452CD', 'white']
set3 = ['#CD8C95', '#8B5F65', '#FAFAD2', '#9370DB']

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)

def pattern1():
    for i in range(150):
        t.color(set1[i%4])
        t.forward(10)
        t.left(2)
        t.forward(i*2)
        t.right(130)

def pattern2():
    for i in range(100):
        t.color(set2[i%4])
        t.forward(12)
        t.left(2)
        t.circle(45)
        t.forward(5)
        t.left(2)
        t.circle(20)
        
def pattern3():
    for i in range(70):
        t.color(set3[i%4])
        t.forward(1100)
        t.left(5)
        t.circle(35)
        t.left(2)
        t.circle(25)
        t.forward(4)
        t.circle(40)
        t.forward(2)
        t.right(25)
        t.forward(5)
        t.right(70)
        t.forward(2)
        t.right(45)
        t.forward(2)
        t.circle(25)

pattern1()

t.penup()
t.goto(-200, 115)
t.pendown()
pattern2()

t.penup()
t.goto(147, 578)
t.pendown()
pattern3()

t.hideturtle()
s.exitonclick()