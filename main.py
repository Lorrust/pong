from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()
        
    # if ball.xcor() > 370 or ball.xcor() < -380:
    #     ball.bounce_x()
    
    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.75
        
    #Detect collision with walls
    #Right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    #Left paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()