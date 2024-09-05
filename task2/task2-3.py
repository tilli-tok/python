import turtle as t

t.hideturtle()
t.speed(10)
t.pensize(5)
t.colormode(255)

ugol = 3

for r in range(40, 0, -10):
    for i in range(6):
        col = r * 6
        t.pencolor(255, 165, col)
        t.fillcolor(162, col, 255)
        t.begin_fill()
        for j in range(ugol):
            t.forward(r*3)
            t.left(360/ugol)
        t.end_fill()
        t.rt(60)

t.done()