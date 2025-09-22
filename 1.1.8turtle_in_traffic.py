import turtle as trtl

# Create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []
# Use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

# Boundary for the turtles
BOUNDARY_X = 300
BOUNDARY_Y = 300

tloc = 50
for s in turtle_shapes:
    ht = trtl.Turtle(shape=s)
    horiz_turtles.append(ht)
    ht.penup()
    new_color = horiz_colors.pop()
    ht.fillcolor(new_color)
    ht.goto(-BOUNDARY_X, tloc)  # Start at left boundary
    ht.setheading(0)  # Move right

    vt = trtl.Turtle(shape=s)
    vert_turtles.append(vt)
    vt.penup()
    new_color = vert_colors.pop()
    vt.fillcolor(new_color)
    vt.goto(-tloc, BOUNDARY_Y)  # Start at top boundary
    vt.setheading(270)  # Move down

    tloc += 50

# Move turtles across and down screen, stopping for collisions or boundaries
speed = 3
full_speed = 10  # Max speed
increase_speed = 1

for step in range(50):
    remove_horiz = []
    remove_vert = []

    for ht in horiz_turtles:
        if ht.xcor() < BOUNDARY_X:  # Check if the turtle within the boundary
            ht.forward(speed)
        else:
            remove_horiz.append(ht)  # Remove if the turtle reached the boundary 

        for vt in vert_turtles:
            if vt.ycor() > -BOUNDARY_Y:  # Check if the turtle within the boundary
                vt.forward(speed)
            else:
                remove_vert.append(vt)  # Remove if turtle reached boundary

            if abs(ht.xcor() - vt.xcor()) < 20 and abs(ht.ycor() - vt.ycor()) < 20:
                ht.hideturtle()
                vt.hideturtle()
                remove_horiz.append(ht)
                remove_vert.append(vt)

    # Remove turtles that hit the boundary/collided
    for ht in remove_horiz:
        if ht in horiz_turtles:
            horiz_turtles.remove(ht)
    for vt in remove_vert:
        if vt in vert_turtles:
            vert_turtles.remove(vt)

    speed += increase_speed
    if speed > full_speed:
        speed = full_speed 

# Change remaining turtles colors to "Tan"
for ht in horiz_turtles:
    ht.fillcolor("Tan")
for vt in vert_turtles:
    vt.fillcolor("Tan")

# turtles are deactivated by changing their color to "gray"
for ht in horiz_turtles:
    ht.fillcolor("gray") 
for vt in vert_turtles:
    vt.fillcolor("gray")  


wn = trtl.Screen()
wn.mainloop()
