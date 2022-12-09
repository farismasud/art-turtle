<<<<<<< HEAD
import turtle as t 

t = t.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
t.backward(200)
t.speed(100000000)
t.shape('turtle')

def pohon(mi):
    if mi < 10:
        return
    else:
        t.forward(mi)
        t.color('gold')
        t.circle(2)
        t.color('brown')
        t.left(30)
        pohon(4*mi/5)
        t.right(60)
        pohon(4*mi/5)
        t.left(30)
        t.backward(mi)

pohon(100)
=======
import turtle as t 

t = t.Turtle()
t.screen.bgcolor('black')
t.pensize(2)
t.color('green')
t.left(90)
t.backward(200)
t.speed(100000000)
t.shape('turtle')

def pohon(mi):
    if mi < 10:
        return
    else:
        t.forward(mi)
        t.color('gold')
        t.circle(2)
        t.color('brown')
        t.left(30)
        pohon(4*mi/5)
        t.right(60)
        pohon(4*mi/5)
        t.left(30)
        t.backward(mi)

pohon(100)
>>>>>>> 562dd54b770c9d89d4337b33c267d1c580ac85cc
t.done()