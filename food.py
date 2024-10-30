from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        self.shift()

    def shift(self):
        random_x = r.randint(-280,280)
        random_y = r.randint(-280,280)
        self.goto(random_x,random_y)
