import turtle

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len-5)

if __name__ == "__main__":
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    line_len = 500
    startX = 0
    startY = 0
    if my_win.window_width() > line_len:
        startX = my_win.window_width() - line_len
    if my_win.window_height() > line_len:
        startY = my_win.window_height() - line_len

    #my_turtle.setpos(startX, startY)
    draw_spiral(my_turtle, line_len)
    my_win.exitonclick()