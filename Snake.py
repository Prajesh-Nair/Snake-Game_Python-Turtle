from turtle import *
import time
class Snake:
    def __init__(self):
        self.snakes = []
        self.create()
        self.head = self.snakes[0]

    def create(self):
        for t in range(1,4):
            x = t * -20
            T = Turtle("square")
            T.color(0,255,0)
            T.pu()
            T.setpos(x,0)
            self.snakes.append(T)

    def move(self):
        l = len(self.snakes)
        for x_num in range(l-1,-1,-1):
            xy = self.snakes[(x_num - 1)].position()
            if x_num == 0:
                self.head.fd(20)
            else:
                self.snakes[x_num].goto(xy)

    def right(self):
        if self.head.heading() == 180:
            return
        else:
            self.head.seth(0)

    def left(self):
        if self.head.heading() == 0:
            return
        else:
            self.head.seth(180)

    def up(self):
        if self.head.heading() == 270:
            return
        else:
            self.head.seth(90)

    def down(self):
        if self.head.heading() == 90:
            return
        else:
            self.head.seth(270)

    def Grow(self):
        poss = self.snakes[-1].position()
        T = Turtle("square")
        T.color(0,255,0)
        T.pu()
        T.setpos(poss)
        self.snakes.append(T)
    
    def reset(self):
        for s in self.snakes:
            s.goto(1000,1000)
        self.snakes.clear()
        self.create()
        self.head = self.snakes[0]