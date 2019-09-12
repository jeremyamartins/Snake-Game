#Simple snake game in Python3 for beginners
import turtle
import time
import random


delay = 0.1

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

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)



# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard Bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


# Main Game Loop
while True:
    wn.update()

    if head.distance(food) < 20:
        # Move the food to random location
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        food.goto(x, y)

    move()

    time.sleep(delay)
    

wn.mainloop()


