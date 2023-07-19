from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Sissss Gamme")

# ram = Turtle("square")
# ram.color("white")
# ram.goto(0, 0)
#
# tam = Turtle("square")
# tam.color("white")
# tam.goto(-20, 0)
#
# zam = Turtle("square")
# zam.color("white")
# zam.goto(-40, 0)

snake = Snake()

moving = True
while moving:
     screen.update()
     time.sleep(0.1)
     snake.seg()


screen.exitonclick()











