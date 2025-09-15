# Rock, Paper, Scissors Game with movement
# Created by: Satya, Abrar, Bharath, Tyler
# Date: 3/26/2025 (COMPLETED)
# Description:
# This program is a Rock, Paper, Scissors game using the Turtle module in Python. It allows the user to play against a computer with movements for each choice. The game keeps track of the score for five rounds before resetting it and displays the score.
# Sources used: Python Turtle documentation, random module documentation, AI tools to assist in animate_choices and play_game functions and overall coding, Python forurm and Geeks for geeks.
# Known Bugs/Features:
# The animation may appear laggy on slower computers.
# If the user enters an invalid input, he always loses the game.
# Clicking the screen again before the animation ends causes an unexpected behavior.

import turtle as trtl  # Turtle module
import random  # Random module for choices
import time  # Time module for animation:delay ( used AI)

# Screen setup
wn = trtl.Screen()  # Create a turtle screen
wn.bgcolor("blue")  # Set background color to blue
wn.tracer(0) 

# 2 Turtles for text and drawing
display = trtl.Turtle()  #Turtle for displaying text
display.hideturtle()  
display.penup()  

drawer = trtl.Turtle()  # Turtle for drawing shapes
drawer.hideturtle()  
drawer.penup()  

score_list = []  # list to store the results of each move

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "Tie"  # If both choices are the same then it is a tie
    if player == "rock" and computer == "scissors":
        return "Win"  # Rock beats Scissors
    if player == "paper" and computer == "rock":
        return "Win"  # Paper beats Rock
    if player == "scissors" and computer == "paper":
        return "Win"  # Scissors beats Paper
    return "Lose"  # If none of the above conditions are met then the player loses

# Function to draw the shape representing the players or computers choice
def draw_shape(move, x, y):
    drawer.penup()  
    drawer.goto(x, y) 
    drawer.setheading(0)  
    if move == "rock":
        drawer.fillcolor("gray")  
        drawer.begin_fill()  
        drawer.pendown()  
        drawer.circle(30)  # Draw circle to represent a rock
        drawer.end_fill() 
    elif move == "paper":
        drawer.fillcolor("white")  #Set paper color to white
        drawer.begin_fill()
        drawer.pendown()
        for x in range(4):  # Draw a square for paper
            drawer.forward(50)
            drawer.left(90)
        drawer.end_fill()
    elif move == "scissors":
        drawer.fillcolor("red")  #Set scissors color to red
        drawer.begin_fill()
        drawer.pendown()
        for x in range(3):  # Draw a triangle to represent scissors
            drawer.forward(50)
            drawer.left(120)
        drawer.end_fill()

    drawer.penup()  #lifting pen to prevent additional lines

# Function to animate the movement of player and computer choices (Used AI for this function)
def animate_choices(player_choice, computer_choice):
    player_x, computer_x = -400, 400  # Start player far left and computer far right (they are off the screen)
    target_player, target_computer = -100, 100  # Move towards these positions
    steps = 25  # Number of steps

    for x in range(steps):  # Loop through animation steps
        drawer.clear()  # Clear previous frame
        player_x += (target_player - player_x) * 0.2  # Move closer to target
        computer_x += (target_computer - computer_x) * 0.2
        draw_shape(player_choice, player_x, 0)  # Draw the player choice at new position
        draw_shape(computer_choice, computer_x, 0)  # Draw the computer choice
        wn.update()  # Refresh the screen
        time.sleep(0.02)  # Add Delay for smooth animation

    drawer.clear()  #clearing the last frame
    draw_shape(player_choice, target_player, 0)  # Draw final position of player choice
    draw_shape(computer_choice, target_computer, 0)  # Draw final position of computer choice
    wn.update()  # Refresh screen

# Handle game when user clicks (Used AI for some parts)
def play_game(x, y):
    display.clear() # Clear previous text
    drawer.clear()  # Clear previous drawings
    player = wn.textinput("Your Move", "Enter Rock, Paper, or Scissor:") # Get player input as a screen textbox
    # Process the inputs
    if player:  # Check if input exists
        player = player.strip().lower() #format the input
    else:  # Handle empty input
        player = "rock" #take rock as a default when input doesn't exist
    computer = random.choice(["rock", "paper", "scissor"])  #Random move selection for computer
    result = determine_winner(player, computer)  # Determine game outcome
    score_list.append(result)  #store the result
    # the player will have 5 rounds and display score at the end
    if len(score_list) >= 5:
        wins = score_list.count("Win")  # Count win
        losses = score_list.count("Lose")  # Count loss
        ties = score_list.count("Tie")  # Count tie
        # Final Score display
        display.goto(0, -110)
        display.write("Final Score - Wins: " + str(wins) + "  Losses: " + str(losses) + "  Ties: " + str(ties), align="center", font=("Arial", 12, "normal"))
        score_list.clear()  # Reset the score for the next 5 rounds
    animate_choices(player, computer)  #function call for animate_choices
    # Display result for each move
    display.goto(0, -50)
    display.write(f"You: {player}  Computer: {computer}  Result: {result}", align="center", font=("Arial", 14, "normal"))
    display.goto(0, -80)
    display.write("Click to play again", align="center", font=("Arial", 12, "normal"))
    wn.update() # Refresh screen

# Title display
display.goto(0, 150)
display.write("Rock, Paper, Scissors Game", align="center", font=("Arial", 16, "bold"))
display.goto(0, 120)
display.write("Click to play", align="center", font=("Arial", 12, "normal"))

wn.onclick(play_game)  # Bind mouse click to start game
wn.mainloop()  
