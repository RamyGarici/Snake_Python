from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=ScoreBoard()
screen.bgpic("./snake.gif")
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")

    
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
# collision snake nourriture:
    if snake.head.distance(food)<15:
        food.change_pos()
        snake.extend()
        scoreboard.increase_score()
        
#collision mur
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        snake.reset()
        
        scoreboard.reset()
#collision queue:
    for segment in snake.segments[1:]:
     
        if snake.head.distance(segment)<10:
            snake.reset()
            
            scoreboard.reset()
    



    
        

   
        




screen.exitonclick()