from turtle import Screen
import time
from snake import snake
from food import food
from scoreboard import scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("my snake game")
screen.tracer(0)
snake=snake()
food=food()
scoreboard=scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_is_on=1
while game_is_on:
    time.sleep(0.09)
    screen.update()
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>280 or snake.head.ycor()<-300:
        game_is_on=False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()






















screen.exitonclick()