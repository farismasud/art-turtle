import turtle

a = turtle.Turtle()
b = turtle.Screen()

b.bgcolor('black')
a.pencolor('white')
a.speed(100)
warna = ('red', 'yellow', 'green', 'blue', 'light blue', 'purple', 'olive', 'magenta', 'beige', 'spring green')

for mi in range(10):
    for me in range(8):
        a.speed(me+10)
        for my in range(2):
            a.pensize(2)
            a.circle(80+mi*20, 90)
            a.lt(90)
        a.lt(45)
    a.pencolor(warna[mi%10])
b.exitonclick()