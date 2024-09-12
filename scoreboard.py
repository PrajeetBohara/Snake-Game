from turtle import Turtle

SCORE_ALIGN = "center"
SCORE_FONT = ["Arial", 20,"normal"] #creating constants to prevent the hardcode in line 12 and 18 and it makes code more reusable
OVER_FONT = ["Arial" , 30, "bold"]
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", align=SCORE_ALIGN, font=SCORE_FONT)
        self.hideturtle()

    def update_score(self):
        self.score += 1 #update score
        self.clear() #clear the score point so that it dont overwrite over existing text
        self.write(f"Score : {self.score}", align=SCORE_ALIGN, font=SCORE_FONT)

    def end_game(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=SCORE_ALIGN, font=OVER_FONT)




