import turtle

def draw_rectangle():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    i = 0
    while i < 4:
        brad.forward(100)
        brad.left(90)
        i += 1

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("black")
    angie.speed(3)

    angie.circle(100)

def draw_triangle():
    bob = turtle.Turtle()
    bob.shape("arrow")
    bob.color("blue")
    bob.speed(4)

    i = 0
    while i < 3:
        bob.forward(100)
        bob.left(120)
        i += 1

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_rectangle()
    draw_circle()
    draw_triangle()

    window.exitonclick()

draw_shapes()
