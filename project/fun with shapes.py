import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set background color
screen.title("Polygon Drawer")

# Create a turtle object
t = turtle.Turtle()
t.speed(2)  # Set drawing speed (1=slowest, 10=fastest)

# Function to draw equilateral triangle with fill color
def draw_triangle():
    t.fillcolor("orange")
    t.begin_fill()
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.end_fill()

# Function to draw rectangle with fill color
def draw_rectangle():
    t.fillcolor("green")
    t.begin_fill()
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

# Function to draw hexagon with fill color
def draw_hexagon():
    t.fillcolor("purple")
    t.begin_fill()
    for _ in range(6):
        t.forward(80)
        t.left(60)
    t.end_fill()

# Position turtle and draw shapes
t.penup()
t.goto(-200, 0)  # Position for triangle
t.pendown()
draw_triangle()

t.penup()
t.goto(0, 0)  # Position for rectangle
t.pendown()
draw_rectangle()

t.penup()
t.goto(200, 0)  # Position for hexagon
t.pendown()
draw_hexagon()

# Hide turtle and keep window open
t.hideturtle()
turtle.done()