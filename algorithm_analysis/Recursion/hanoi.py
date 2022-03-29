
from turtle import *

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1, n*1.5, 2) # square-->rectangle
        self.fillcolor(n/number, 0, 1-n/number)
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"space") # 第一个参数为None，表明将绑定在“space”键上的监听函数解绑
    clear()
    try:
        hanoi(number, t1, t2, t3)
        write("click screen to exit",
              align="center", font=("Courier", 16, "bold"))
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    global t1, t2, t3, number
    ht() #使用了turtle的function，该函数会作用在默认的turtle实例上，以下类同
    penup()
    goto(0, -225)   # 默认的turtle主要用来服务在屏幕上写文字内容
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # 通过对话框的方式获得汉诺塔盘子数量
    # numinput函数是可以接受用户输入数值的一个对话框函数，返回值是float型，需要时要做类型转换
    number = int(numinput("盘子数", "请输入汉诺塔的盘子数量", default=4, minval=1, maxval=10))
    for i in range(number,0,-1):
        t1.push(Disc(i))

    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    # 创建一个键盘敲击事件监听器，第一个参数为执行的函数名（必须是无参），第二个参数是键名（“space”代表空格键，“a”代表字母a键）
    onkey(play, "space")
    listen()
    return "EVENTLOOP"

if __name__=="__main__":
    msg = main()
    exitonclick()
    print(msg)
    mainloop()

