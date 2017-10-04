import turtle

def draw_rhombus(pointer):
    for i in range(0, 2):
        pointer.forward(50)
        pointer.left(39)
        pointer.forward(50)
        pointer.left(141)

def draw_flower():
    window = turtle.Screen()

    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("blue")
    bob.speed(10)
    for i in range(0, 36):
        draw_rhombus(bob)
        bob.left(10)

    bob.right(90)
    bob.forward(225)
    window.exitonclick()
draw_flower()
