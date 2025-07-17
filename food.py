from turtle import Turtle,Screen
import random
screenn=Screen()
screenn.register_shape("Jour20_21_snake/apple.gif")
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("Jour20_21_snake/apple.gif")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.change_pos()
        
    def change_pos(self):
            random_x=random.randint(-280,280)
            random_y=random.randint(-280,280)
            self.goto(random_x,random_y)
       
        
        