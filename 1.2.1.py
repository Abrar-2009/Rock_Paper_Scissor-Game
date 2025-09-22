"""
Author: Abrar
Date of completion : 3/8/2025
Description: This program creates a game where the user has to click on a circle to gain points. The circle moves to a random position on the screen after each click. The game ends after 30 seconds. The score is displayed on the top right corner of the screen. The timer is displayed on the top left corner of the screen. if the timer reaches 0, the circle will disappear and the game will end.

"""

# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl #import turtle as trtl
import random as rand #import random as rand

#-----game configuration----
score = 0
def update_score():
    global score
    score += 1
    score_writer.clear()
    print(score_writer.write(score, font=font_setup))

font_setup = ("Arial", 20, "normal")
timer = 60
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
spot = trtl.Turtle() #create turtle
spot.shape("circle") #set shape to circle
spot.shapesize(2) #set the raius of the circle to 2
spot.fillcolor("pink") #set the color of the circle to pink

score_writer = trtl.Turtle()  
score_writer.penup()
score_writer.goto(100, 210)
score_writer.hideturtle()

counter =  trtl.Turtle()
counter.penup()
counter.goto(-200, 210)
counter.hideturtle()

#-----game functions--------
def spot_clicked(x, y):  # spot_clicked function with parameters x and y
    global timer_up  # Ensure timer_up is accessed from the global scope
    
    if timer_up is False:  # If timer_up is False (i.e., time is not up)
        spot.penup() #pen up
        spot.hideturtle() #hide circle
        update_score()  # Update the score
        change_position()  # Change the turtle's position
        spot.showturtle()  #show circle
        spot.pendown() #pen down
    else:  # If timer_up is True (i.e., time is up)
        spot.hideturtle()  # Hide the turtle


def change_position(): #change_position
    new_xpos = rand.randint(-200, 200) #random integer between -200 and 200
    new_ypos = rand.randint(-150, 150) #random integer between -150 and 150
    spot.goto(new_xpos, new_ypos) #Circle goes to new position

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
  
#-----events----------------
spot.onclick(spot_clicked) #when circle is clicked, spot_clicked function is called
wn = trtl.Screen() #create screen
wn.ontimer(countdown, counter_interval)
wn.bgcolor("lightblue")
wn.mainloop() #keep the window open


