from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.shape("arrow")


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def rotate_left():
    tim.left(180)


def rotate_right():
    tim.right(180)


def draw_circle():
    tim.circle(20)


def delete():
    tim.clear()


def turn_left():
    tim.left(90)


def turn_right():
    tim.right(90)

def cross_right():
    tim.right(45)

def cross_left():
    tim.left(45)
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="b", fun=backward)
screen.onkey(key="l", fun=rotate_left)
screen.onkey(key="r", fun=rotate_right)
screen.onkey(key="c", fun=draw_circle)
screen.onkey(key="d", fun=delete)
screen.onkey(key="<", fun=turn_left)
screen.onkey(key=">", fun=turn_right)
screen.onkey(key="/", fun=cross_right)
screen.onkey(key="(", fun=cross_left)

screen.exitonclick()
