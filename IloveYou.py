import turtle
tur = turtle.Turtle()
turtle.Screen().bgcolor("black")

tur.penup()
tur.goto(-230,175)
tur.pendown()

#I
tur.pencolor("white")
tur.pensize(16)
tur.forward(100)
tur.backward(50)
tur.right(90)
tur.forward(170)
tur.right(90)
tur.forward(50)
tur.backward(100)

tur.penup()
tur.goto(0,0)
tur.pendown()

#LOVE
tur.color("red")
tur.begin_fill()
tur.right(130)
tur.forward(130)
tur.circle(50,200)
tur.right(140)
tur.circle(50,200)
tur.forward(133)
tur.end_fill()

tur.penup()
tur.goto(140,175)
tur.pendown()

#YOU
tur.pencolor("white")
tur.right(40)
tur.forward(120)
tur.circle(60,180)
tur.forward(120)

#AYANGNYA AKU
tur.penup()
tur.goto(-300,-150)
tur.pendown()
tur.write("Reva Amelia Rosana", font=("Arial", 50, "bold"))

tur.hideturtle()
turtle.done()