from turtle import Turtle

bar = Turtle()


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=6, stretch_len=2)
        self.move_y = 25
        self.goto(positions)

    def user_move_up(self):
        y = self.ycor()
        y += 40
        self.sety(y)

    def user_move_down(self):
        y = self.ycor()
        y -= 40
        self.sety(y)
