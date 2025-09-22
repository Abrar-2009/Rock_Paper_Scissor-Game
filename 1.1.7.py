#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]


for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  colors = turtle_colors.pop()
  t.fillcolor(colors)
  t.pencolor(colors)
  my_turtles.append(t)

# Moves the turtle position to (0, 0)
startx = 0
starty = 0
direction = 90
distance = 50 
# Moves the tutle by using the in turtle_shapes
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.setheading(direction)
  t.right(45)     
  t.forward(distance)
  direction += 10  # Increase the angle slightly to create a spiral effect
  distance += 10

#	Moves the turtle forward and add some shapes at the end
  startx = t.xcor()
  starty = t.ycor()
  direction = t.heading()

wn = trtl.Screen()
wn.mainloop()
