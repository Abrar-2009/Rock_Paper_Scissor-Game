"""
Author: Satya, Abrar, David, Tyler
Date of completion : 3/7/2025
Description: This program creates an artistic scene using Turtle.
It draws a ground, road (with a yellow dotted line), houses with roofs and doors, trees with foliage, and an animated sun that moves from left to right and, upon reaching its final position, draws its rays. The scene demonstrates the use of loops, lists, and conditional statements etc..
"""

import turtle as trtl

# Set background and turtle
screen = trtl.Screen()                # Create screen
screen.setup(width=800, height=600)   # Set dimension
screen.bgcolor("skyblue")             # Set background

pen = trtl.Turtle()                   # Create turtle
pen.speed(0)                          # Set drawing speed to fastest

# Draw ground(rectangle)
pen.penup()
pen.goto(-400, -150)                  # Start at bottom left of ground
pen.setheading(0)                     # Set heading to 0 degrees
pen.color("green")                    # Set color to green for ground
pen.begin_fill()                      # Start filling ground shape
# Loop to draw a rectangle for the ground
for x in range(2):
    pen.forward(800)                  # Draw long side with width 800
    pen.right(90)                     # Turn right 90 degrees  
    pen.forward(150)                  # Draw short side with width 150
    pen.right(90)                     # Turn right 90 degrees
pen.end_fill()                        # stop filling the rectangle

# Draw road(rectangle)
pen.penup()
pen.goto(-400, -150)                  # Start at the same left position as the ground
pen.setheading(0)                     # Set heading to 0 degrees
pen.color("gray")                     # Set color to gray for the road
pen.begin_fill()                      # Begin filling rectangle
# Loop to draw a rectangle for the road                    
for x in range(2):
    pen.forward(800)                  # Draw road width(800)
    pen.right(90)                     # Turn right 90 degrees
    pen.forward(40)                   # Draw road height(40)
    pen.right(90)                     # Turn right 90 degrees
pen.end_fill()                        # stop filling the rectangle

# Draw yellow dotted line in between the road
pen.penup()
pen.goto(-400, -170)                  # Position near the roads center
pen.setheading(0)                     # Set heading to 0 degrees
pen.color("white")                   # Set pen color to yellow for drawing the dotted line
# Loop to draw dotted line(skip every 20 units)
for x in range(20):
    pen.pendown()                      
    pen.forward(20)                   # Draw a line for 20 units
    pen.penup()
    pen.forward(20)                   # Skip 20 units

# Draw houses with doors (using loop and if statement)
# List of house bottom left coordinates(each tuple represents a coordinate)
house = [(-250, -150), (70, -150)]
# Loop to set up coordinates, heading etc..(nested)
for (housex, housey) in house:
    pen.penup()
    pen.goto(housex, housey)           # Starting point is at the bottom left of the rectangle
    pen.setheading(0)                  # Set heading to 0 degrees
    pen.color("lightgrey")             # Set pen color to light grey
    pen.begin_fill()                   # start filling the rectangle part of the house
    # Loop to draw a rectangle for the house width 100 and height 60(2 iterations)
    for x in range(2):
        pen.forward(100)               # Move forward along the bottom and top edges with width 100
        pen.left(90)                   # turn left 90 degrees
        pen.forward(60)                # Move forward along the left and right edges with height 60
        pen.left(90)                   # turn left 90 degrees
    pen.end_fill()
   
    # Draw roof for the house(triangle)
    pen.penup()
    pen.goto(housex, housey + 60)      # goto the left top corner of house base to start drawing the triangle
    pen.pendown()
    pen.color("brown")                 # set pen color to brown
    pen.begin_fill()
    pen.goto(housex + 100, housey + 60)     # Move to the right top corner of house base
    pen.goto(housex + 50, housey + 120)     # Peak for the roof which is at the center and 60 units above the base
    pen.goto(housex, housey + 60)           # Move to the left top corner of the house base
    pen.end_fill()
   
    # Draw door (rectangle at the center of the house base)
    doorx = housex + 35               # Change door x position to center it with the houses rectangle
    pen.penup()
    pen.goto(doorx, housey)           # Position doors bottom edge to the bottom of the houses rectangle
    pen.setheading(0)                 # Set heading to 0 degrees
    pen.color("red")                  # Set pen color to red
    pen.begin_fill()
    # Loop for drawing one door in each house
    for x in range(2):
        pen.forward(30)              # Door with width 30
        pen.left(90)                 # turn left 90 degrees
        pen.forward(40)              # Door with height 40
        pen.left(90)                 # turn left 90 degrees
    pen.end_fill()                   # stop filling the door
   
    # Door knob using an if statement
    # If the house is located at one of the two positions, then add a door knob
    if housex == -250 or housex == 70:
        pen.penup()
        pen.goto(doorx + 25, housey + 20)  # Position the knob
        pen.color("gold")                  # Set pen color to gold
        pen.begin_fill()                   # start filling the door knob
        pen.circle(2)                      # Small circle radius for door knob
    pen.end_fill()                         # stop filling the door knob

# Draw 3 trees with foliage
# list for tree bottom left positions
treepositions = [(-330, -150), (-50, -150), (230, -150)]
# Loop for color, coordinates, heading etc..(nested)
for treex, treey in treepositions:
    pen.penup()
    pen.goto(treex, treey)                 # Start at bottom left of trunk
    pen.setheading(90)                     # set heading to 90 degrees
    pen.color("saddlebrown")               # set color to saddle brown
    pen.begin_fill()                       # Start filling the tree trunk
    # Loop for drawing the trunk(rectangle with width 20 and height 40)
    for x in range(2):
        pen.forward(40)                    # Trunk with height 40
        pen.right(90)                      # Turn right 90 degrees
        pen.forward(20)                    # Trunk with width 20
        pen.right(90)                      # Turn right 90 degrees
    pen.end_fill()                         # Stop filling the tree trunk
   
    # Draw foliage(circle of radius 30 and its bottom touches the trunk)
    pen.penup()
    pen.goto(treex + 10, treey + 35)      # Move to the top center of trunk
    pen.setheading(0)                     # set heading to 0 degrees
    pen.color("green")                    # set pen color to green
    pen.begin_fill()                      # start filling the foliage
    pen.circle(30)                        # Draw the foliage circle with radius 30
    pen.end_fill()                        # stop filling the foliage
pen.hideturtle()                          # Hide turtle

# Sun animation from left to right and draw rays at the end.
input = input("Animate sun from left to right? (yes/no): ") # Ask user whether to animate the sun
if input == "yes":                                          #Check if input was "yes"
    # New turtle creation for suns animation
    sun_anim = trtl.Turtle()                                #Initialize a turtle object
    sun_anim.speed(0)                                       # Set max speed
    sun_anim.penup()                                
    sun_anim.color("yellow")                                # set outline color for sun as yellow
    sun_anim.fillcolor("yellow")                            #fill yellow
    # start positioning the sun on the left
    sun_anim.goto(-400, 150)                                # Position sun at left edge at x = -400, y(original)
    sun_anim.pendown()
    sun_anim.begin_fill()                                   # start coloring suns shape
    sun_anim.circle(50)                                     # Draw sun as a circle with radius 50
    sun_anim.end_fill()                                     # Stop filling sun
   
    # Animate sun moving along x = -400 to x = 200
    # Loop until sun reaches x=200 position
    while sun_anim.xcor() < 200:
        sun_anim.clear()                                   # Clear previous sun
        sun_anim.penup()
        new_x = sun_anim.xcor() + 10                       #Calc the new x coordinate (10 right)
        sun_anim.goto(new_x, 150)                          # Move the sun to new position
        sun_anim.pendown()
        sun_anim.begin_fill()                              # start filling new sun
        sun_anim.circle(50)                                # Draw sun again at latest position
        sun_anim.end_fill()                                # stop filling sun
    final_sun_x = sun_anim.xcor()                          # Store final x after finishing
    # Loop to draw rays after sun reaches its final position
    for x in range(12):
        sun_anim.penup()
        sun_anim.goto(final_sun_x, 200)                   # start from the suns center
        sun_anim.setheading(x * 30)                       # Set heading at 30 degree intervals (0, 30, 60, ... 330)
        sun_anim.pendown()
        sun_anim.forward(80)                              # Move forward 80
    sun_anim.hideturtle()                             # Hide the turtle after finishing
else:                                                     # else statement for "no" input
    print("Animation skipped")                            # display that the animation is skipped

wn = trtl.Screen()                                        # END
wn.mainloop()