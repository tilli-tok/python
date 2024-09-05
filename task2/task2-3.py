import turtle as t

t.hideturtle()
t.speed(10)
t.pensize(5)

ugol = 3
col_del = 255 / 255
col_del2 = 165 / 255

for r in range(40, 0, -10):
    for i in range(6):
        col = min(r * 6 / 255, 1)
        t.pencolor(col_del, col_del2, col)
        t.fillcolor(col_del2, col, col_del)
        t.begin_fill()
        for j in range(ugol):
            t.forward(r*3)
            t.left(360/ugol)
        t.end_fill()
        t.rt(60)

t.done()