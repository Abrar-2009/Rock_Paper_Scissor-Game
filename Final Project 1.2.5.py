import turtle as trtl  # Import the turtle module
import random          # Import the random module




# Screen setup
wn = trtl.Screen()             # Create a new turtle screen  # Full-screen size
wn.bgcolor("tan")             # Set the background color to blue




# Create a turtle for displaying messages
display = trtl.Turtle()
display.hideturtle()
display.penup()
display.goto(0, 150)
display.write("Rock, Paper, Scissors Game", align="center", font=("Arial", 16, "bold"))
display.goto(0, 120)
display.write("Click anywhere to play", align="center", font=("Arial", 12, "normal"))




# Create a turtle for drawing shapes (rock, paper, scissors)
drawer = trtl.Turtle()
drawer.hideturtle()
drawer.penup()




# Global list to store game outcomes
score_list = []




def determine_winner(player, computer):
    # Expanded logic without inline conditions
    if player == computer:
        result = "Tie"
    else:
        if player == "rock":
            if computer == "scissors":
                result = "Win"
            else:
                result = "Lose"
        elif player == "paper":
            if computer == "rock":
                result = "Win"
            else:
                reslut = "Lose"
        elif player == "scissors":
            if computer == "paper":
                result = "Win"
            else:
                result = "Lose"
        else:
            result = "Lose"
    return result




def draw_shape(move, x, y):
    # Draw the appropriate shape for the move at (x, y) with fill colors.
    drawer.penup()
    drawer.goto(x, y)
    drawer.setheading(0)
   
    if move == "rock":
        # Draw a circle for rock with gray fill.
        drawer.fillcolor("gray")
        drawer.begin_fill()
        drawer.pendown()
        drawer.circle(30)
        drawer.end_fill()
        drawer.penup()
   
    elif move == "paper":
        # Draw a square for paper with white fill.
        drawer.fillcolor("white")
        drawer.begin_fill()
        drawer.pendown()
        for count in range(4):
            drawer.forward(50)
            drawer.left(90)
        drawer.end_fill()
        drawer.penup()
   
    elif move == "scissors":
        # Draw a triangle for scissors with red fill.
        drawer.fillcolor("red")
        drawer.begin_fill()
        drawer.pendown()
        for count in range(3):
            drawer.forward(50)
            drawer.left(120)
        drawer.end_fill()
        drawer.penup()




def play_game(x, y):
    # Clear previous drawings and messages.
    display.clear()
    drawer.clear()
   
    # Prompt for player's move using a text input.
    player_input = wn.textinput("Your Move", "Enter Rock, Paper, or Scissors:")
    if player_input:
        player = player_input.strip().lower()
    else:
        player = "rock"
   
    # Randomly choose the computer's move.
    computer = random.choice(["rock", "paper", "scissors"])
   
    # Determine the result.
    result1 = determine_winner(player, computer)
    score_list.append(result1)
   
    # Draw the moves: player's move on the left, computer's move on the right.
    draw_shape(player, -100, 0)
    draw_shape(computer, 100, 0)
   
    # Display the moves and result using simple string concatenation.
    display.goto(0, -50)
    message1 = "You: " + player + " , Computer: " + computer + " , Result: " + result1
    display.write(message1, align="center", font=("Arial", 14, "normal"))
   
    display.goto(0, -80)
    message2 = "Click anywhere to play again"
    display.write(message2, align="center", font=("Arial", 12, "normal"))


# Bind mouse clicks to the play_game function.
wn.onclick(play_game)


# Start the main event loop.
wn.mainloop()