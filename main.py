import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simple Space Visualizer")
screen.tracer(0)

stars = []

for _ in range(50):
    star = turtle.Turtle()
    star.shape("circle")
    star.color("white")
    star.penup()
    star.speed(0)
    star.shapesize(0.1, 0.1)

    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    star.goto(x, y)

    stars.append(star)


def move_stars():
    for star in stars:
        y = star.ycor()
        y -= random.randint(1, 5)

        if y < -300:
            y = 300
            star.setx(random.randint(-300, 300))

        star.sety(y)


def animate():
    move_stars()
    screen.update()
    screen.ontimer(animate, 30)


animate()
screen.mainloop()
