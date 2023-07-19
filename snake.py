from turtle import Turtle

POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DIASTANCE = 20

class Snake:

    def __int__(self):
        self.move = []
        self.create_snake = ()

    def create_snake(self):
        for jam in POSITION:
            ram = Turtle("square")
            ram.penup()
            ram.color("white")
            ram.goto(jam)
            self.move.append(ram)
        self.move[0].forward(MOVE_DIASTANCE)

    def seg(self):
        for seg_num in range(len(self.move) - 1, 0, -1):
            num_x = self.move[seg_num - 1].xcor()
            num_y = self.move[seg_num - 1].ycor()
            self.move[seg_num].goto(num_x, num_y)
