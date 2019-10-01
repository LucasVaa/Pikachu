import turtle

def setPosition(x, y):
    turtle.setx(x)
    turtle.sety(y)
    print(x, y)

class Pikachu():

    def __init__(self):
        self.t = turtle.Turtle()
        t = self.t
        t.pensize(3)
        t.speed(0)
        t.ondrag(setPosition)

    def no_trace_goto(self, x, y):
        t = self.t
        t.penup()
        t.goto(x, y)
        t.pendown()

    def left_eye(self, x, y):
        self.no_trace_goto(x, y)
        t = self.t
        t.pensize(0)
        t.setheading(0)
        t.fillcolor("#5E5148")
        t.begin_fill()
        t.circle(25)
        t.end_fill()

        self.no_trace_goto(x + 6, y + 25)
        t.setheading(0)
        t.fillcolor("#F3F3EB")
        t.begin_fill()
        t.circle(11)
        t.end_fill()

        self.no_trace_goto(x + 2, y + 4)
        t.setheading(0)
        t.fillcolor("#F3F3EB")
        t.begin_fill()
        t.circle(6)
        t.end_fill()

        self.no_trace_goto(x - 12, y + 10)
        t.setheading(0)
        t.fillcolor("#F3F3EB")
        t.begin_fill()
        t.circle(4.5)
        t.end_fill()

    def right_eye(self, x, y):
        self.no_trace_goto(x, y)
        t = self.t
        t.setheading(0)
        t.fillcolor("#5D534A")
        t.begin_fill()
        t.circle(25)
        t.end_fill()

        self.no_trace_goto(x - 6, y + 25)
        t.setheading(0)
        t.fillcolor("#F3F3EB")
        t.begin_fill()
        t.circle(11)
        t.end_fill()

        self.no_trace_goto(x - 2, y + 4)
        t.setheading(0)
        t.fillcolor("#F3F3EB")
        t.begin_fill()
        t.circle(6)
        t.end_fill()

        self.no_trace_goto(x + 12, y + 10)
        t.setheading(0)
        t.fillcolor("#F3F3EB")
        t.begin_fill()
        t.circle(4.5)
        t.end_fill()

    def nose(self, x, y):
        self.no_trace_goto(x, y)
        t = self.t
        t.setheading(0)
        t.fillcolor("#5D534A")
        t.begin_fill()
        t.setheading(0)
        t.forward(15)
        t.circle(-4, 135)
        t.circle(-20, 35)
        t.right(16)
        t.circle(-20, 38)
        t.circle(-4, 160)
        t.end_fill()

        t.penup()
        t.goto(x, y - 3)
        t.pendown()
        t.fillcolor("#F3F3EB")
        t.begin_fill()
        t.setheading(0)
        t.forward(5)
        t.circle(-3, 165)
        t.circle(-18, 10)
        t.right(40)
        t.circle(-18, 20)
        t.right(40)
        t.circle(-3, 100)
        t.end_fill()
        t.hideturtle()

    def mouth(self, x, y):
        self.no_trace_goto(x, y)
        t = self.t
        t.setheading(0)
        t.fillcolor("#E58076")
        t.begin_fill()
        t.circle(15, 45)
        t.right(180)
        t.circle(-15, 90)
        t.right(10)
        t.circle(-300, 10)
        t.end_fill()

        t.begin_fill()
        t.right(180)
        t.circle(300, 10)
        t.right(350)
        t.circle(15, 90)
        t.left(10)
        t.circle(300, 10)

        t.setheading(10)
        t.circle(40, 20)
        t.left(180)
        t.circle(-40, 70)
        t.circle(-10, 40)

        t.setheading(261)
        t.circle(-10, 40)
        t.circle(-40, 70)
        t.hideturtle()
        t.end_fill()

    def left_cheek(self, x, y):
        t = self.t
        self.no_trace_goto(x, y)
        t.setheading(300)
        t.fillcolor('#E58076')
        t.begin_fill()
        a = 2.5
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.left(3)
                t.forward(a)
            else:
                a += 0.05
                t.left(3)
                t.forward(a)
        t.end_fill()

    def right_cheek(self, x, y):
        t = self.t
        self.no_trace_goto(x, y)
        t.setheading(60)
        t.fillcolor('#E58076')
        t.begin_fill()
        a = 2.5
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                t.left(3)
                t.forward(a)
            else:
                a += 0.05
                t.left(3)
                t.forward(a)
        t.end_fill()

    def color_left_ear(self, x, y):
        self.no_trace_goto(x, y)
        t = self.t
        t.pensize(0)
        t.fillcolor("#6D5A53")
        t.begin_fill()
        t.setheading(90)
        t.circle(-300, 10)
        t.circle(-70, 11)
        t.setheading(170)
        t.circle(400, 10)
        t.setheading(225)
        t.forward(11)
        t.setheading(309)
        t.circle(300, 19)
        t.end_fill()
        t.pensize(3)

    def color_right_ear(self, x, y):
        self.no_trace_goto(x, y)
        t = self.t
        t.pensize(0)
        t.fillcolor("#6D5A53")
        t.begin_fill()
        t.setheading(45)
        t.circle(200, 10)
        t.circle(100, 30)
        t.circle(40, 20)
        t.setheading(5)
        t.circle(-500, 5)
        t.setheading(270)
        t.forward(18)
        t.setheading(228)
        t.circle(-500, 10.5)
        t.end_fill()
        t.pensize(3)
        t.hideturtle()

    def body(self):
        t = self.t
        t.fillcolor("#FDD55B")
        t.begin_fill()

        # 右腮帮子
        t.penup()
        t.circle(160, 30)
        t.pendown()
        t.circle(100, 30)
        t.circle(50, 60)
        t.circle(-240, 30)
        t.circle(50, 25)

        # 右耳朵
        t.left(180)
        t.circle(-50, 25)
        t.left(100)
        t.circle(300, 40)
        t.circle(30, 50)
        t.left(80)
        t.circle(400, 33)

        # 大脑门
        t.left(110)
        t.circle(100, 10)
        t.left(180)
        t.circle(-100, 10)
        t.left(16)
        t.circle(280, 50)

        # 左耳朵
        t.left(10)
        t.circle(100, 10)
        t.left(180)
        t.circle(-100, 10)
        t.left(100)
        t.circle(300, 40)
        t.circle(30, 50)
        t.left(80)
        t.circle(300, 42)

        # 左腮帮子
        t.left(90)
        t.circle(-50, 20)
        t.left(180)
        t.circle(50, 20)
        t.left(10)
        t.circle(-240, 28)
        t.circle(60, 80)
        t.right(10)
        t.circle(100, 30)

        # 左手手
        t.left(180)
        t.circle(-100, 20)
        t.setheading(175)
        t.circle(500, 18)
        t.setheading(140)
        t.forward(10)
        t.setheading(270)
        t.forward(10)
        t.setheading(190)
        t.forward(12)
        t.setheading(300)
        t.forward(10)
        t.setheading(215)
        t.forward(11)
        t.setheading(330)
        t.forward(11)
        t.setheading(215)
        t.forward(11)
        t.setheading(330)
        t.forward(13)
        t.setheading(225)
        t.forward(10)
        t.setheading(0)
        t.forward(10)
        t.setheading(330)
        t.circle(500, 16)
        t.circle(-20, 95)
        t.circle(-500, 10)

        # 左脚脚
        t.right(120)
        t.left(180)
        t.circle(-500, 6)
        t.left(180)
        t.circle(500, 11)
        t.circle(5, 150)
        t.circle(100, 5)
        t.circle(50, 5)
        t.left(180)
        t.circle(-50, 5)
        t.circle(-100, 5)
        t.circle(-5, 70)
        t.setheading(100)
        t.circle(6, 170)
        t.circle(100, 5)
        t.circle(50, 5)
        t.left(180)
        t.circle(-50, 5)
        t.circle(-100, 5)
        t.circle(-6, 30)
        t.setheading(240)
        t.circle(50, 40)
        t.left(10)
        t.circle(500, 7)
        t.circle(-400, 4)
        t.circle(20, 100)
        t.circle(500, 4)

        # 屁股蛋儿
        t.left(180)
        t.circle(-500, 3)
        t.setheading(350)
        t.circle(300, 23)
        t.circle(-300, 30)
        t.circle(100, 50)

        # 右脚脚
        t.setheading(120)
        t.circle(-120, 6)
        t.left(180)
        t.circle(120, 14)
        t.circle(12, 120)
        t.circle(500, 13)
        t.circle(22, 170)
        t.forward(40)
        t.left(180)
        t.forward(40)
        t.circle(-22, 60)
        t.right(80)
        t.circle(-20, 40)
        t.forward(15)
        t.right(180)
        t.forward(15)
        t.circle(20, 40)
        t.right(100)
        t.circle(-22, 45)
        t.right(40)
        t.circle(-20, 30)
        t.forward(10)
        t.right(180)
        t.forward(10)
        t.circle(20, 30)
        t.right(140)
        t.left(180)
        t.circle(22, 90)

        # 右手手
        t.setheading(100)
        t.circle(-500, 10)
        t.setheading(20)
        t.circle(150, 40)
        t.circle(500, 9)
        t.setheading(45)
        t.forward(10)
        t.setheading(170)
        t.forward(10)
        t.setheading(80)
        t.forward(10)
        t.setheading(180)
        t.forward(10)
        t.setheading(88)
        t.forward(14)
        t.setheading(210)
        t.forward(15)
        t.setheading(115)
        t.forward(10)
        t.setheading(220)
        t.forward(13)
        t.setheading(160)
        t.forward(10)
        t.setheading(260)
        t.forward(10)
        t.setheading(205)
        t.circle(500, 10)

        t.end_fill()

        # 眼睛
        self.left_eye(-140, 160)
        self.right_eye(20, 160)
        self.nose(-70, 160)
        self.mouth(-60, 70)
        self.left_cheek(-208, 80)
        self.right_cheek(80, 80)
        self.color_left_ear(-330, 275)
        self.color_right_ear(186, 265)
    def start(self):
        self.body()

def main():
    print('Painting the Pikachu... ')
    turtle.screensize(800, 600)
    turtle.title('Pikachu')
    pikachu = Pikachu()
    pikachu.start()
    turtle.mainloop()

if __name__ == '__main__':
    main()
