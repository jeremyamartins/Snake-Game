#Simple snake game in Python3 for beginners
import turtle
import time


delay = 0.5

#set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Map The Coder √")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # This turns off screen updates

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Main Game Loop
while True:
    wn.update()
    

wn.mainloop()

