import turtle

def tree(branch_len, my_turtle):
    if branch_len > 5:
        my_turtle.forward(branch_len)
        my_turtle.right(20)
        tree(branch_len-15, my_turtle)
        my_turtle.left(40)
        tree(branch_len-10, my_turtle)
        my_turtle.right(20)
        my_turtle.backward(branch_len)

def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(100)
    my_turtle.down()
    my_turtle.color("green")
    tree(100, my_turtle)
    my_win.exitonclick()

if __name__ == "__main__":
    main()