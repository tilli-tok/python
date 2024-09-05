import turtle as t

t.ht()
t.speed(10)
t.pensize(5)

ugol = 3

for r in range(40, 0, -10):
    for i in range(6):
        color_value = min(r * 6, 255)
        t.color(f'#{255:02x}{165:02x}{color_value:02x}')
        t.fillcolor(f'#{162:02x}{color_value:02x}{255:02x}')
        t.begin_fill()
        for i in range(ugol):
            t.forward(r*3)
            t.left(360/ugol)
        t.end_fill()
        t.rt(60)

t.done()