from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 25, 'normal')

user_score = 0
cpu_score = 0


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.user_score = 0
        self.cpu_score = 0
        self.score_update()

    def score_update(self):
        self.write(f'Your Score:{self.user_score}     CPU Score:{self.cpu_score}', align=ALIGNMENT, font=FONT)

    def keep_user_score(self):
        self.user_score += 1
        self.clear()
        self.score_update()

    def keep_cpu_score(self):
        self.cpu_score += 1
        self.clear()
        self.score_update()

    def end_game(self):
        if self.user_score == 5:
            self.goto(x=0, y=0)
            self.write(f'GAME OVER, YOU WIN!', False, align=ALIGNMENT, font=FONT)
        if self.cpu_score == 5:
            self.goto(x=0, y=0)
            self.write(f'GAME OVER, YOU Lose.', False, align=ALIGNMENT, font=FONT)
