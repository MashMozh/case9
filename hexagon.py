import turtle

turtle.setup(500, 500)
def draw_hexagon(x, y, color, side_len):
    turtle.up()
    turtle.goto(x,y)
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.down()
    for _ in range(6):
        turtle.forward(side_len)
        turtle.right(60)
    turtle.end_fill()

    turtle.done()

draw_hexagon(0,0,'red', 100)
