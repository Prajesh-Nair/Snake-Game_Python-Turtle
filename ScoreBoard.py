from turtle import Turtle

class ScoreB(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.hideturtle()
        self.goto(0,275)
        self.score = 0
        with open("Snake Game (D-20)\data.txt", mode="r") as file:
            self.highScore = int(file.read())
        self.write(f"Score: {self.score} HighScore: {self.highScore}",False,align="center",font=('Subway', 16, 'bold'))

    def score_inc(self):
        self.goto(0,275)
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highScore}",False,align="center",font=('Subway', 16, 'bold'))

    def reset(self):
        self.clear()
        if self.score > self.highScore:
            self.highScore = self.score
            with open("Snake Game (D-20)\data.txt" , mode="w") as file:
                file.write(str(self.highScore))
        self.score = 0
        self.write(f"Score: {self.score} HighScore: {self.highScore}",False,align="center",font=('Subway', 16, 'bold'))