from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Score import ScoreBoard
import time


screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)
score_board = ScoreBoard()


left_paddle = Paddle((-400, 0))
right_paddle = Paddle((400, 0))
right_paddle.shapesize(stretch_wid=10, stretch_len=2)

game = True

ball = Ball()

screen.listen()
screen.onkey(fun=left_paddle.user_move_up, key='Up')
screen.onkey(fun=left_paddle.user_move_down, key='Down')


while game:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Cpu paddle movement
    right_paddle.sety(right_paddle.ycor() + right_paddle.move_y)
    if right_paddle.ycor() >= 240 or right_paddle.ycor() <= -240:
        right_paddle.move_y *= -1

    # Ball collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.move_y *= -1

    # Keep score/Collision
    if ball.xcor() > 500:
        ball.reset_position()
        score_board.keep_user_score()
    if ball.xcor() < -500:
        ball.reset_position()
        score_board.keep_cpu_score()

    # Ball and Paddle collision
    if ball.distance(right_paddle) < 50 and ball.xcor() > 360 or ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    if score_board.user_score == 5:
        game = False
        score_board.end_game()
    if score_board.cpu_score == 5:
        game = False
        score_board.end_game()

screen.exitonclick()


# TODO 1. Create the screen
# TODO 2. Create a Bar/Paddle
# TODO 3. Create another Bar
# TODO 4. Create the Ball and make it move
# TODO 5. Detect collision with wall and bounce
# TODO 6. End game after 10 points
# TODO 7. Ask to play again if yes restart if no end
