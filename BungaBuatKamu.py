<<<<<<< HEAD
#Bunga pertama Buat ayang
import turtle as tur
import colorsys as cs
tur.setup(800,800)
tur.speed(0)
tur.width(2)
tur.bgcolor("black")
for j in range(25):
    for i in range(15):
        tur.color(cs.hls_to_rgb(i/15, j/25, 1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(50,24)
tur.hideturtle()
=======
#Bunga pertama Buat ayang
import turtle as tur
import colorsys as cs
tur.setup(800,800)
tur.speed(0)
tur.width(2)
tur.bgcolor("black")
for j in range(25):
    for i in range(15):
        tur.color(cs.hls_to_rgb(i/15, j/25, 1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(50,24)
tur.hideturtle()
>>>>>>> 562dd54b770c9d89d4337b33c267d1c580ac85cc
tur.done