from turtle import Turtle
ALIGNMENT = "center"
FONT = ('courier','24','normal')

with open("data.txt") as file:
    hi_score = int(file.read())

class Scoreboard(Turtle):
    global hi_score
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = hi_score
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.score))
            self.score = 0
            self.update_scoreboard()        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()    