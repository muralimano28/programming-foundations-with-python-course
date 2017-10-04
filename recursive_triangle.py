import turtle

def draw_recursively(marker, base_pos, count):
    x = base_pos[0]
    y = base_pos[1]
    z = base_pos[2]

    # Finding middle
    btw_x_y = find_mid(x, y)
    btw_y_z = find_mid(y, z)
    btw_z_x = find_mid(z, x)

    if (count == 0):
        draw_triangle(marker, [btw_x_y, btw_y_z, btw_z_x], 'white')
    else:
        draw_recursively(marker, [x, y, z], count - 1)
        draw_recursively(marker, [x, btw_x_y, btw_z_x], count - 1)
        draw_recursively(marker, [btw_z_x, btw_y_z, z], count - 1)
        draw_recursively(marker, [btw_x_y, y, btw_y_z], count - 1)

def find_mid(a, b):
    x = (a[0] + b[0])/2
    y = (a[1] + b[1])/2
    return [x, y]

def draw_triangle(marker, pos, color):
    x = pos[0]
    y = pos[1]
    z = pos[2]

    marker.penup()
    marker.setposition(x)
    marker.pendown()
    marker.fillcolor(color)
    marker.begin_fill()

    marker.goto(y)
    marker.goto(z)
    marker.goto(x)

    marker.end_fill()

def draw_shape(pos_arr, nos, fill_color):
    window = turtle.Screen()

    marker = turtle.Turtle()
    marker.color('blue')

    # 1. Draw base triangle
    draw_triangle(marker, pos_arr, fill_color)

    # 2. recursively draw inner triangle
    draw_recursively(marker, pos_arr, nos)

    window.exitonclick()

positions = [[-200, 0], [0, 200], [200, 0]]
no_of_inner_triangles = 2
base_triangle_color = 'green'

draw_shape(positions, no_of_inner_triangles, base_triangle_color)
