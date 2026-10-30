import turtle

t = turtle.Turtle()
t.speed(0)

def draw_star(x, y, size, color, filled):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)

    if filled:
        t.begin_fill()

    for i in range(5):
        t.forward(size)
        t.right(144)

    if filled:
        t.end_fill()


for row in range(4):
    for col in range(4):

        x = col * 110 - 150
        y = 150 - row * 110

        if row % 2 == 0:
            if col % 2 == 0:
                draw_star(x, y, 18, "olive", False)
            else:
                draw_star(x, y, 35, "purple", True)
        else:
            if col % 2 == 0:
                draw_star(x, y, 35, "purple", True)
            else:
                draw_star(x, y, 18, "olive", False)

turtle.done()