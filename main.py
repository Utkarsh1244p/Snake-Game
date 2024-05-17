import turtle as t
from snake import Snake 
from food import Food
from score import Score
import time

screen = t.Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width= 600, height= 600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

#These are keybinders which binds specific keys to functions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# total_score = 0
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #To check collision between snake and food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.hideturtle()
        food.refresh()
        food.showturtle()
        #To extend the tail
        snake.extend_snake()

    #To check collision between snake and walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_on = False

    #To check collision between snake head and its tail
    #if head collide with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_on = False 
    #   Trigger game_over function 
        

screen.exitonclick()