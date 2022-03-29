import turtle # Python的一个标准模块，是一个入门级绘制图形（绘制过程可以动态演示，所以在教学中使用较多）

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len) #forward函数的作用就是沿着乌龟头的方向向前走line_len个像素单位长度
        my_turtle.right(90) #right函数为让乌龟头向右旋转90度
        draw_spiral(my_turtle, line_len-5)

if __name__ == "__main__":
    my_turtle = turtle.Turtle() #创建一个可以绘制图形的乌龟对象
    my_win = turtle.Screen() #创建乌龟绘制图像所需要的窗口
    line_len = 300
    if my_win.window_width() > line_len: #window_width函数获得窗口的宽度（单位为像素）
        startX = -line_len // 2
    else:
        startX = -my_win.window_width()//2
    if my_win.window_height() > line_len:
        startY = line_len // 2
    else:
        startY = my_win.window_height()//2
    my_turtle.up() #让乌龟悬空，意味着调用了这个方法之后前进等操作时将不会在屏幕上留下痕迹
    my_turtle.setpos(startX, startY) #让乌龟从现有的位置以直线的方式直接定位到屏幕坐标位置(startX, startY)处
    my_turtle.down() #让乌龟落地，意味着调用了这个方法之后再进行前进等操作时将会在屏幕上留下痕迹
    draw_spiral(my_turtle, line_len)
    my_win.exitonclick() #设置程序结束的方式，点击窗口即退出