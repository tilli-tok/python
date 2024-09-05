import turtle as t

t.ht()
t.pensize(5)
t.speed(0)

for r in range(40, 0, -10):
  for i in range(6):
    col = r*6
    t.pencolor(255 / 255, 165 / 255, col / 255)
    t.fillcolor(162 / 255, col / 255, 255 / 255)
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.rt(60)

t.done()