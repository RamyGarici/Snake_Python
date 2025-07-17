from turtle import Turtle
ALIGNEMENT="Center"
FONT=("Courier", 24, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        self.highscore=0
        with open("Jour20_21_Snake/highscore.txt") as file:
            try:
                self.highscore=int(file.read())
            except:
                self.highscore=0
           
                
        
       
        self.goto(0,268)
        self.write(f"Score: {self.score}, High Score: {self.highscore}",align=ALIGNEMENT,font=FONT)
    def update_score(self):
 
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}",align=ALIGNEMENT,font=FONT)
    
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("Jour20_21_Snake/highscore.txt",mode="w") as file:
                file.write(f"{str(self.highscore)}")
                
                
        self.score=0
        self.update_score()
    def increase_score(self):
        self.score+=1
        self.update_score()
       
        