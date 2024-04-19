import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Set the speed of the turtle (0 is the fastest)
pen.width(2)  # Set the width of the lines

# Define a function to draw a colorful spiral
def draw_colorful_spiral(size, growth_rate):
    for _ in range(100):  # Repeat the pattern 100 times
        r = random.random()  # Generate a random value for the red component
        g = random.random()  # Generate a random value for the green component
        b = random.random()  # Generate a random value for the blue component
        pen.color(r, g, b)  # Set the pen color
        pen.forward(size)  # Move the turtle forward
        pen.left(10)  # Turn the turtle 10 degrees to the left
        size += growth_rate  # Increase the size for the next segment

# Move the turtle to the starting position
pen.penup()
pen.goto(0, 0)
pen.pendown()

# Set the initial size and growth rate of the spiral
initial_size = 10
growth_rate = 0.2

# Draw the colorful spiral
draw_colorful_spiral(initial_size, growth_rate)

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()
